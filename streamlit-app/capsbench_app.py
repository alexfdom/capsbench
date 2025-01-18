import streamlit as st
import os
from capsbench.capsbench_cli import process_evaluation_logic
from capsbench.token_metrics import token_metrics
import polars as pl


st.set_page_config(
    page_title="CapsBench Evaluation Framework",
    layout="wide",
    initial_sidebar_state="expanded",
)


def local_css():
    st.markdown(
        """
        <style>
        :root {
            --background-color: #FFFFFF;
            --text-color: #333333;
            --header-color: #333333;
            --accent-color: #008080; /* Teal accent, visible on both light/dark */
            --link-color: #008080;
            --metric-value-color: #008080;
            --border-color: #DDDDDD;
        }

        @media (prefers-color-scheme: dark) {
          :root {
            --background-color: #1E1E1E;
            --text-color: #ECECEC;
            --header-color: #ECECEC;
            --accent-color: #00A6A6;
            --link-color: #58D1D1;
            --metric-value-color: #58D1D1;
            --border-color: #444444;
          }
        }

        body {
            background: var(--background-color);
            color: var(--text-color);
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: var(--background-color);
            border-right: 1px solid var(--border-color);
        }

        /* Headers */
        h1, h2, h3, h4, h5 {
            font-weight: 600;
            color: var(--header-color);
        }

        /* Metrics */
        .metric-title {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-color);
        }
        .metric-value {
            font-size: 20px;
            font-weight: bold;
            color: var(--metric-value-color);
        }
        .section-header {
            font-size: 20px;
            margin-top: 30px;
            margin-bottom: 15px;
            font-weight: 600;
            color: var(--header-color);
        }

        /* Buttons */
        div.stButton > button:first-child {
            background-color: var(--accent-color);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            padding: 0.5rem 1rem;
            cursor: pointer;
        }
        div.stButton > button:hover {
            background-color: var(--link-color);
        }

        /* Progress bar */
        [role="progressbar"] > div {
            background-color: var(--accent-color) !important;
        }

        /* Tooltips */
        .stTooltip > div {
            background-color: var(--accent-color);
            color: white;
            font-size: 14px;
        }

        /* Links */
        a {
            color: var(--link-color);
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }

        /* Inputs, labels, and general text */
        p, label {
            color: var(--text-color);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


local_css()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def toggle_description():
    st.session_state.show_description = not st.session_state.show_description


def display_metrics(result, baseline_key_metrics, caption_column):
    st.subheader("🖼️📃 → 📊 CapsBench")
    col1, _ = st.columns([1, 3])

    cas_mean = result["score"].mean()
    baseline_cas_mean = baseline_key_metrics.get("CapsBench Accuracy", 0.0)
    col1.metric(
        label=f"CapsBench Accuracy (%) for {caption_column}",
        value=f"{cas_mean:.2f}",
        delta=f"{cas_mean - baseline_cas_mean:.2f}%",
    )


def display_token_metrics(summary_metrics, baseline_token_metrics):
    st.subheader("📝 Token Metrics")
    col1, col2 = st.columns(2)

    avg_caption_length = summary_metrics["Value"][0]
    baseline_avg_caption_length = baseline_token_metrics.get(
        "Average Token Length per Caption", 0.0
    )
    col1.metric(
        label="Average Token Length",
        value=f"{avg_caption_length:.2f}",
        delta=f"{avg_caption_length - baseline_avg_caption_length:.2f}",
    )

    vocabulary_size = summary_metrics["Value"][1]
    baseline_vocabulary_size = baseline_token_metrics.get("Vocabulary Size", 0.0)
    col2.metric(
        label="Vocabulary Size",
        value=f"{vocabulary_size:.2f}",
        delta=f"{vocabulary_size - baseline_vocabulary_size:.2f}",
    )


# @st.cache_data(show_spinner=False)
def run_evaluation_logic(
    _progress_callback,
    input_file,
    img_bytes_column,
    caption_column,
    questions_column,
    start,
    end,
    step,
    openai_api_key,
    output_file,
):
    if _progress_callback:
        _progress_callback(0, 100)
    return process_evaluation_logic(
        input_file=input_file,
        img_bytes_column=img_bytes_column,
        caption_column=caption_column,
        questions_column=questions_column,
        start=start,
        end=end,
        step=step,
        openai_api_key=openai_api_key,
        output_file=output_file,
        progress_callback=_progress_callback,
    )


def main():
    st.title("🖼️📃 → 📊 CapsBench Benchmark")
    st.write(
        "A Benchmark for evaluating the accuracy of synthetic captions against the CapsBench dataset."
    )

    with st.sidebar:
        st.header("🔐 API Credentials")
        st.write("Enter or load your OpenAI API Key for evaluation:")
        openai_key = st.text_input(
            "Enter OpenAI API Key:",
            type="password",
            help="Your OpenAI API key is required for LLM-based reasoning.",
        )
        if openai_key:
            st.success("API key set successfully!")
            st.session_state["openai_key"] = openai_key

        if st.button("Load API Key from Environment"):
            api_from_env = os.getenv("OPENAI_API_KEY")
            if api_from_env:
                st.session_state["openai_key"] = api_from_env
                st.success("API key loaded from environment!")
            else:
                st.error("No API key found in environment variables.")

        # Baseline Metrics Configuration
        with st.expander("📊 Baseline Metrics Configuration", expanded=False):
            st.write(
                "Set baseline values to compare your evaluation results against these reference points."
            )
            # CapsBench Baseline
            st.subheader("🖼️📃 → 📊 CapsBench Accuracy Baseline")
            baseline_cas = st.number_input(
                "CapsBench Accuracy (%)",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=0.01,
                help="Baseline percentage for CapsBench Accuracy.",
            )

            # Token Metrics Baseline
            st.subheader("📝 Token Metrics")
            baseline_avg_caption_length = st.number_input(
                "Average Token Length per Caption",
                min_value=0.0,
                value=0.0,
                step=0.01,
                help="Baseline value for Average Token Length per Caption.",
            )
            baseline_vocabulary_size = st.number_input(
                "Vocabulary Size",
                min_value=0.0,
                value=0.0,
                step=1.0,
                help="Baseline value for Vocabulary Size.",
            )

        if "baseline_key_metrics" not in st.session_state:
            st.session_state.baseline_key_metrics = {"CapsBench Accuracy": baseline_cas}

        if "baseline_token_metrics" not in st.session_state:
            st.session_state.baseline_token_metrics = {
                "Average Token Length per Caption": baseline_avg_caption_length,
                "Vocabulary Size": baseline_vocabulary_size,
            }

        st.session_state.baseline_key_metrics["CapsBench Accuracy"] = baseline_cas
        st.session_state.baseline_token_metrics["Average Token Length per Caption"] = (
            baseline_avg_caption_length
        )
        st.session_state.baseline_token_metrics["Vocabulary Size"] = (
            baseline_vocabulary_size
        )

    st.markdown("---")

    with st.expander("ℹ️ Understanding the Evaluation", expanded=False):
        st.markdown(
            """
            The **CapsBench Evaluation Framework** measures how accurately generated captions
            answer a set of ground-truth questions derived from the CapsBench dataset.

            **Scoring Methodology**

            The score is calculated based on the following tasks to be accomplished for `gpt-4o-2024-08-06`:

            1. For each question, respond **"yes"**, **"no"**, or **"n/a"**, based only on the caption's content.
            2. Compare these answers to the reference ground truth answers.
            3. Compute the percentage of correct responses:
                $$
                \\text{Score} = \left( \\frac{\\text{Number of Correct Answers}}{\\text{Total Number of Questions}} \\right) \\times 100
                $$
            
            [View an Example DataFrame Output in .md format.](https://github.com/alexfdom/capsbench/blob/main/results/pg-captioner/results_gpt-4o-2024-08-06_pg-captioner_iter_1_.md)
            """
        )

    st.header("📤 Upload the CapsBench Dataset")
    st.write(
        "You can download `.parquet` or `.feather` files from [HuggingFace/playgroundai/CapsBench](https://huggingface.co/datasets/playgroundai/CapsBench)."
    )
    st.info(
        "**Recommendation:** Perform the evaluation at least three times and average the results for stable findings."
    )

    uploaded_file = st.file_uploader(
        "Choose a Parquet or Feather file", type=["parquet", "feather"]
    )

    if uploaded_file is not None:
        tmp_dir = "temp"
        os.makedirs(tmp_dir, exist_ok=True)
        tmp_file_path = os.path.join(tmp_dir, uploaded_file.name)
        with open(tmp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully.")
        try:
            df = pl.read_parquet(tmp_file_path)
        except Exception:
            try:
                df = pl.read_feather(tmp_file_path)
            except Exception as e:
                st.error(f"❌ Failed to read the dataset: {e}")
                df = None

        if df is not None:
            if df is not None:
                with st.expander("📊 Dataset Preview", expanded=True):
                    st.write("Below is an overview of the columns in your dataset.")

                    img_bytes_column = st.session_state.get("img_bytes_column", "image")

                    columns_info = []
                    num_rows_to_sample = 3
                    for col in df.columns:
                        dtype = str(df[col].dtype)
                        if col == img_bytes_column:
                            sample_val = f"({dtype}) Image bytes not displayed"
                        else:
                            sample = (
                                df[col].head(num_rows_to_sample).to_pandas().tolist()
                            )
                            sample_val = ", ".join([str(val) for val in sample])
                        columns_info.append(
                            {"Column": col, "Type": dtype, "Sample Values": sample_val}
                        )

                    st.dataframe(pl.DataFrame(columns_info), width=4500)
        st.markdown("---")

        # Input Parameters
        st.header("⚙️ Processing Parameters")
        with st.expander("Advanced Configuration", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                img_bytes_column = st.text_input(
                    "Image Bytes Column",
                    value="image",
                    help="Column containing image bytes in the uploaded file.",
                )
                caption_column = st.text_input(
                    "Caption Column",
                    value="pg-captioner",
                    help="Column of synthetic captions to evaluate (e.g., pg-captioner, sonnet, gpt-4o or any model column you add to the dataset).",
                )
                output_file = st.text_input(
                    "Output File Path",
                    value="results.parquet",
                    help="Local path to save the evaluation results.",
                )

            with col2:
                questions_column = st.text_input(
                    "Questions Column",
                    value="questions",
                    help="Column containing questions and reference ground truth answers.",
                )
                start = st.number_input(
                    "Start Index",
                    min_value=0,
                    value=0,
                    step=1,
                    help="Start index for subset evaluation.",
                )
                end = st.number_input(
                    "End Index (not inclusive)",
                    min_value=1,
                    value=200,
                    step=1,
                    help="End index for subset evaluation.",
                )
                step = st.number_input(
                    "Step Size",
                    min_value=1,
                    value=1,
                    step=1,
                    help="Evaluate every nth sample (subsampling).",
                )

        if st.button("🚀 Process File"):
            if "openai_key" not in st.session_state and OPENAI_API_KEY is None:
                st.error("❌ Please provide an OpenAI API key before processing.")
            else:
                with st.spinner("Processing the file, this may take a few moments..."):
                    try:
                        if not os.path.isfile(tmp_file_path):
                            st.error("❌ The uploaded file does not exist.")
                            return
                        progress_bar = st.progress(0)
                        status_text = st.empty()

                        def progress_callback(current, total):
                            progress_bar.progress(current / total)
                            progress = (current / total) * 100
                            status_text.text(f"Processing: {int(progress)}%")

                        result = run_evaluation_logic(
                            progress_callback,
                            input_file=tmp_file_path,
                            img_bytes_column=img_bytes_column,
                            caption_column=caption_column,
                            questions_column=questions_column,
                            start=start,
                            end=end,
                            step=step,
                            openai_api_key=st.session_state.get("openai_key")
                            or OPENAI_API_KEY,
                            output_file=output_file,
                        )

                        if result is not None:
                            st.success(
                                f"✅ Processing complete! Results saved to '{output_file}'."
                            )

                            with st.container():
                                progress_bar.progress(90)
                                # CapsBench Accuracy
                                display_metrics(
                                    result,
                                    st.session_state.baseline_key_metrics,
                                    caption_column,
                                )

                                st.subheader("📋 Snapshot of Evaluation Results")
                                st.write("Below are the first 10 evaluated entries:")
                                st.dataframe(
                                    result.drop(["image_bytes", "reasons"]).head(10)
                                )

                                # Token Metrics
                                summary_metrics, _ = token_metrics(result)
                                display_token_metrics(
                                    summary_metrics,
                                    st.session_state.baseline_token_metrics,
                                )

                                st.markdown("---")
                                ERROR_MESSAGE = "Error generating."
                                total_success = len(
                                    [
                                        answer
                                        for answer in result["openai_answers"]
                                        if answer != ERROR_MESSAGE
                                    ]
                                )
                                message = f"**Total Number of entries successfully processed** for CapsBench Accuracy: **{total_success}**"

                                if total_success == 0:
                                    st.error(
                                        "❌ No entries were successfully processed. Check your API key or parameters and try again."
                                    )
                                else:
                                    st.markdown(message)

                                progress_bar.progress(100)
                                st.success("✅ Evaluation completed successfully.")
                        else:
                            st.error(
                                "❌ No valid results were produced. Check input parameters and try again."
                            )

                    except Exception as e:
                        st.error(f"❌ Failed to process the file: {e}")

    st.markdown("---")
    st.markdown(
        "Developed by [alexfdom](https://github.com/alexfdom) | Enhanced by the community"
    )


if __name__ == "__main__":
    main()
