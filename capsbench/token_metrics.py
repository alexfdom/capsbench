import polars as pl
import tiktoken
from typing import Tuple

encoding = tiktoken.encoding_for_model("gpt-4")


def tokenize_with_tiktoken(text: str) -> list:
    if text is None or text.strip() == "":
        return []
    return encoding.encode(text)


def token_metrics(df_output: pl.DataFrame) -> Tuple[pl.DataFrame, pl.DataFrame]:
    df_output = df_output.with_columns(
        pl.col("candidate_caption")
        .map_elements(tokenize_with_tiktoken, return_dtype=pl.List(pl.Int64))
        .alias("tokenized_caption")
    )

    df_output = df_output.with_columns(
        [
            pl.col("tokenized_caption").list.len().alias("token_count"),
            pl.when(pl.col("tokenized_caption").list.len() > 0)
            .then(pl.col("tokenized_caption").list.unique().list.len())
            .otherwise(0)
            .alias("caption_vocabulary_size"),
        ]
    )

    total_tokens = df_output.explode("tokenized_caption")[
        "tokenized_caption"
    ].drop_nulls()
    global_vocab_size = total_tokens.unique().len()

    avg_token_count = df_output["token_count"].mean()

    df_output = df_output.drop(["tokenized_caption"])

    summary_metrics = pl.DataFrame(
        {
            "Metric": ["Average Token Length per Caption", "Vocabulary Size"],
            "Value": [avg_token_count, global_vocab_size],
        }
    )

    return summary_metrics, df_output


# --- Example of usage --- #

if __name__ == "__main__":
    df = pl.DataFrame(
        {
            "candidate_caption": [
                "just for fun a",
                None,
            ]
        }
    )
    summary, df_output = token_metrics(df)

    print("\nToken Metrics:\n")
    print(summary)
    print("\nProcessed DataFrame:\n")
    print(df_output)
