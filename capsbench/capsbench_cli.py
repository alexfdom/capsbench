from capsbench import answers_pipeline as answers_pipe
import os
import typer
import pandas as pd
import numpy as np
from typing import Optional
import tqdm 
import polars as pl
from typing import List
import logging.config
from capsbench.token_metrics import token_metrics
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml
import sys

# Time required: less than 3 minutes
# The paper recommends performing three iterations of the evaluation process for each captioning model.
# Paper: https://arxiv.org/abs/2409.10695
""" 
Usage Example: pg-captioner iteration 1
python -m capsbench.capsbench_cli \
--input-file dataset/capsbench_dataset.parquet \
--img-bytes-column image \
--caption-column pg-captioner \
--questions-column questions \
--start 0 --end 200 --step 1 \
--openai-api-key <your_openai_api_key> \
--output-file results_gpt-4o-2024-08-06_pg-captioner_iter_1_.parquet
"""

with open("config/logger_config.yaml", "r") as f:
    log_config = yaml.safe_load(f)

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

app = typer.Typer(help="CLI CapsBench evaluation framework.")

def read_columns(path, columns):
    path_ext = os.path.splitext(path)[1].lower()

    readers = {
        ".parquet": lambda p, c: pd.read_parquet(p, columns=c),
        ".feather": lambda p, c: pl.read_ipc(p, columns=c).to_pandas(),
    }

    if path_ext not in readers:
        logger.error(f"Unsupported file type: {path_ext}")
        sys.exit(1)

    try:
        df = readers[path_ext](path, columns)
        logger.info(f"Successfully read columns: {columns}")
        return df
    except ValueError as ve:
        logger.error(f"Error reading file {path}: {ve}")
        sys.exit(1)
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error occurred while reading {path}: {e}")
        sys.exit(1)

def evaluation_output(df_output_pd: pd.DataFrame, caption_column) -> List[pl.DataFrame]:
    df_output_pd["candidate_caption"] = df_output_pd["candidate_caption"].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) > 0 else ""
    )
    df_candidate_caption_pl = pl.from_pandas(
        df_output_pd["candidate_caption"].to_frame()
    )

    df_accuracy_pl = pl.from_pandas(df_output_pd)
    summary, token_metrics_pl = token_metrics(df_candidate_caption_pl)

    print("\nToken Metrics:\n")
    print(summary)

    joined_df_pl = df_accuracy_pl.join(
        token_metrics_pl, on="candidate_caption", how="inner"
    )
    print("\nCapsBench Accuracy (%):\n")
    print(df_accuracy_pl["score"].describe())
    print(
        f"CapsBench Accuracy (%) for //{caption_column}// ---> {df_accuracy_pl['score'].mean()}"
    )

    return joined_df_pl


def process_row(
    index: int,
    row: pd.Series,
    img_bytes_column: str,
    caption_column: str,
    questions_column: Optional[str],
    answers_pipeline_app: answers_pipe.AnswersPipelineApp,
    logger,
) -> dict:
    image_bytes = None

    if img_bytes_column:
        image_data = row[img_bytes_column]
        if isinstance(image_data, dict):
            image_bytes = image_data.get("bytes") or image_data.get("data")
            if not image_bytes:
                logger.error(f"No image bytes found in dict at row {index}.")
                return {}
        elif isinstance(image_data, bytes):
            image_bytes = image_data
        else:
            logger.error(
                f"Unexpected type for image data at row {index}: {type(image_data)}"
            )
            return {}

    candidate_captions = row[caption_column]

    if not isinstance(candidate_captions, list):
        candidate_captions = [candidate_captions]
    if not isinstance(candidate_captions, (list, np.ndarray)):
        logger.warning(f"Invalid candidate_caption format at row {index}. Skipping.")
        return {}

    result = {
        "image_bytes": image_bytes,
        "candidate_caption": candidate_captions,
        "captioned_by": caption_column,
        "ground_truth": str(row[questions_column]),
        "scores": {},
    }

    formatted_captions = "\n".join([f"- {caption}" for caption in candidate_captions])

    try:
        if questions_column:
            ground_truth_info = {
                col: row[col].tolist() if isinstance(row[col], np.ndarray) else row[col]
                for col in questions_column.split(",")
            }
        else:
            ground_truth_info = "We do not have ground_truth information for this image."
        ground_truth_str = str(ground_truth_info)
        openai_answers = answers_pipeline_app.generate_answers(
            client_type="openai",
            candidate_caption=formatted_captions,
            ground_truth=ground_truth_str,
        )

        score_accuracy = answers_pipeline_app.generate_structured_outputs(
            client_type="openai",
            candidate_caption=formatted_captions,
            answers=openai_answers,
        )
        result["scores"] = {
            "openai_answers": openai_answers,
            "score": score_accuracy,
        }
    except Exception as e:
        logger.error(
            f"Exception processing model_answers for {candidate_captions}: {e}"
        )
        return {}

    return result


def process_evaluation_logic(
    input_file: str,
    img_bytes_column: str,
    caption_column: str,
    questions_column: Optional[str],
    start: int,
    end: int,
    step: int,
    openai_api_key: Optional[str],
    output_file: str,
    progress_callback: Optional[callable] = None
) -> str:

    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    else:
        openai_api_key = typer.prompt("Enter your OpenAI API key", hide_input=True)
        logger.error("OpenAI API key must be provided.")
        raise typer.Exit(code=1)
    if not input_file:
        typer.echo("Please provide an input file using --input-file option.", err=True)
        raise typer.Exit(code=1)

    input_ext = os.path.splitext(input_file)[1].lower()
    if input_ext == ".parquet":
        try:
            df_raw = pd.read_parquet(input_file)
        except Exception as e:
            typer.echo(f"Failed to read Parquet file: {e}", err=True)
            logger.error(f"Exception reading Parquet file {input_file}: {e}")
            raise typer.Exit(code=1)
    elif input_ext == ".feather":
        try:
            df_raw = pl.read_ipc(input_file).to_pandas()
        except Exception as e:
            typer.echo(f"Failed to read Feather file: {e}", err=True)
            logger.error(f"Exception reading Feather file {input_file}: {e}")
            raise typer.Exit(code=1)
    else:
        typer.echo(
            "Unsupported input file format. Please provide a .parquet file.", err=True
        )
        logger.error(f"Unsupported input file format: {input_ext}")
        raise typer.Exit(code=1)

    if img_bytes_column and caption_column:
        essential_columns = (
            [img_bytes_column, caption_column]
            if img_bytes_column and caption_column
            else None
        )

    if essential_columns is None:
        logger.info(
            f"{[(index, column) for index, column in enumerate(df_raw.columns)]}"
        )
        return logger.warning(
            "Please provide the columns corresponding to image_bytes and captions."
        )
    else:
        read_columns(input_file, essential_columns)

    if start > 0 or end > 1:
        if start < 0 or end < 0:
            typer.echo(
                "Error: --start and --end must be non-negative integers.", err=True
            )
            logger.error("--start and --end must be non-negative integers.")
            raise typer.Exit(code=1)
        if start > end:
            typer.echo("Error: --start must be less than or equal to --end.", err=True)
            logger.error("--start must be less than or equal to --end.")
            raise typer.Exit(code=1)
        if step <= 0:
            typer.echo("Error: --step must be a positive integer.", err=True)
            logger.error("--step must be a positive integer.")
            raise typer.Exit(code=1)
        df_selected = df_raw.iloc[start:end:step]
        typer.echo(f"--> Processing rows from {start} to {end} with step {step}")
        logger.info(f"Processing rows from {start} to {end} with step {step}")
    else:
        df_selected = df_raw.iloc[start:end]

    answers_pipeline_app = answers_pipe.AnswersPipelineApp()

    all_results = []
    futures = []
    max_workers = 10
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for index, row in df_selected.iterrows():
            future = executor.submit(
                process_row,
                index,
                row,
                img_bytes_column,
                caption_column,
                questions_column,
                answers_pipeline_app,
                logger,
            )
            futures.append(future)

        completed = 0
        for f in tqdm.tqdm(
            as_completed(futures), total=len(futures), desc="Processing"
        ):
            res = f.result()
            if res:
                all_results.append(res)
            completed += 1

            if progress_callback:
                progress_callback(completed, total = len(df_selected))

    output_ext = os.path.splitext(output_file)[1].lower()
    if output_ext == ".parquet":
        try:
            output_dir = os.path.dirname(os.path.abspath(output_file))
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            rows = []
            for res in all_results:
                rows.append(
                    {
                        "image_bytes": res["image_bytes"],
                        "candidate_caption": res["candidate_caption"],
                        "captioned_by": res["captioned_by"],
                        "ground_truth": res["ground_truth"],
                        "openai_answers": res["scores"]["openai_answers"],
                        "score": res["scores"]["score"][0],
                        "reasons": res["scores"]["score"][1],
                    }
                )

            df_output_pd = pd.DataFrame(rows)
            evaluation_results_pl = evaluation_output(df_output_pd, caption_column)
            evaluation_results_pl.write_parquet(output_file)
            typer.echo(
                f"\n--> All scores successfully saved to {output_file}.\n"
            )
            logger.info(f"All scores successfully saved to {output_file}.")
            return evaluation_results_pl

        except Exception as e:
            typer.echo(f"Failed to save scores to {output_file}: {e}")
            logger.error(f"Exception occurred while saving scores: {e}")
            raise typer.Exit(code=1)

    elif output_ext == ".feather":
        try:
            output_dir = os.path.dirname(os.path.abspath(output_file))
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            rows = []
            for res in all_results:
                rows.append(
                    {
                        "image_bytes": res["image_bytes"],
                        "candidate_caption": res["candidate_caption"],
                        "captioned_by": res["captioned_by"],
                        "ground_truth": res["ground_truth"],
                        "openai_answers": res["scores"]["openai_answers"],
                        "score": res["scores"]["score"][0],
                        "reasons": res["scores"]["score"][1],
                    }
                )

            df_output_pd = pd.DataFrame(rows)
            evaluation_results_pl = evaluation_output(df_output_pd, caption_column)
            evaluation_results_pl.write_ipc(output_file)
            typer.echo(
                f"\n--> All scores successfully saved to {output_file}.\n"
            )
            logger.info(f"--> All scores successfully saved to {output_file}.")
            return evaluation_results_pl

        except Exception as e:
            typer.echo(f"Failed to save scores to {output_file}: {e}", err=True)
            logger.error(f"Exception occurred while saving scores: {e}")
            raise typer.Exit(code=1)
    else:
        typer.echo("No output file specified. Results are not saved.", err=True)
        logger.info("No output file provided; results not saved.")


@app.command()
def process_evaluation_typer(
    input_file: str = typer.Option(
        None,
        "--input-file",
        "-i",
        help="Path to the input file in Parquet/Feather format containing image_byte column, candidate captions columuns generated by diverse models and question columns.",
    ),
    img_bytes_column: str = typer.Option(
        None,
        "--img-bytes-column",
        "-b",
        help="image_bytes column to select from the Parquet/Feather file.",
    ),
    caption_column: str = typer.Option(
        None,
        "--caption-column",
        "-C",
        help="caption column to select from the Parquet/Feather file.",
    ),
    questions_column: Optional[str] = typer.Option(
        None,
        "--questions-column",
        "-q",
        help="Questions column to select from the Parquet/Feather file.",
    ),
    start: Optional[int] = typer.Option(
        0, "--start", "-S", help="Starting index of the rows to process (inclusive)."
    ),
    end: Optional[int] = typer.Option(
        1, "--end", "-E", help="Ending index of the rows to process (exclusive)."
    ),
    step: int = typer.Option(
        1,
        "--step",
        "-P",
        help="Step size for processing rows.",
        show_default=True,
    ),
    openai_api_key: Optional[str] = typer.Option(
        os.getenv("OPENAI_API_KEY"),
        "--openai-api-key",
        "-k",
        help="Your OpenAI API key. Can also be set via the OPENAI_API_KEY environment variable.",
        show_default=False,
    ),
    output_file: str = typer.Option(
        "results.parquet",
        "--output-file",
        "-o",
        help="Path to save the scores.",
        show_default=True,
    ),
):
    process_evaluation_logic(
        input_file,
        img_bytes_column,
        caption_column,
        questions_column,
        start,
        end,
        step,
        openai_api_key,
        output_file,
        progress_callback=None
    )

    
def process_evaluation(
    input_file: str = typer.Option(
        None,
        "--input-file",
        "-i",
        help="Path to the input file in Parquet/Feather format containing image_byte column, candidate captions columuns generated by diverse models and question columns.",
    ),
    img_bytes_column: str = typer.Option(
        None,
        "--img-bytes-column",
        "-b",
        help="image_bytes column to select from the Parquet/Feather file.",
    ),
    caption_column: str = typer.Option(
        None,
        "--caption-column",
        "-C",
        help="caption column to select from the Parquet/Feather file.",
    ),
    questions_column: Optional[str] = typer.Option(
        None,
        "--questions-column",
        "-q",
        help="Questions column to select from the Parquet/Feather file.",
    ),
    start: Optional[int] = typer.Option(
        0, "--start", "-S", help="Starting index of the rows to process (inclusive)."
    ),
    end: Optional[int] = typer.Option(
        1, "--end", "-E", help="Ending index of the rows to process (exclusive)."
    ),
    step: int = typer.Option(
        1,
        "--step",
        "-P",
        help="Step size for processing rows.",
        show_default=True,
    ),
    openai_api_key: Optional[str] = typer.Option(
        os.getenv("OPENAI_API_KEY"),
        "--openai-api-key",
        "-k",
        help="Your OpenAI API key. Can also be set via the OPENAI_API_KEY environment variable.",
        show_default=False,
    ),
    output_file: str = typer.Option(
        "results.parquet",
        "--output-file",
        "-o",
        help="Path to save the scores.",
        show_default=True,
    ),
    progress_callback: Optional[callable] = None
):
    
    process_evaluation_logic(
        input_file,
        img_bytes_column,
        caption_column,
        questions_column,
        start,
        end,
        step,
        openai_api_key,
        output_file,
        progress_callback
    )

def main():
    app()

if __name__ == "__main__":
    main()
