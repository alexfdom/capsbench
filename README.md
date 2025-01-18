# CapsBench

The CapsBench Toolkit is an open-source software solution for quantifying the accuracy of AI-generated captions. It extends and clarifies the original CapsBench concept from the paper [*Playground v3: Improving Text-to-Image Alignment with Deep-Fusion Large Language Models*](https://arxiv.org/pdf/2409.10695).

**Table of Contents**
- [CapsBench](#capsbench)
  - [APP](#app)
    - [Option 1: Cloud Server](#option-1-cloud-server)
    - [Option 2: Run Locally](#option-2-run-locally)
  - [Understanding the Evaluation](#understanding-the-evaluation)
  - [CLI](#cli)
    - [Example of Usage](#example-of-usage)
    - [Sample Terminal Output](#sample-terminal-output)
  - [Research: How to Optimize the Evaluation](#research-how-to-optimize-the-evaluation)
  - [References](#references)

## APP

### Option 1: Cloud Server

Access the CapsBench app directly on Streamlit Community Cloud:

🔗 https://capsbench.streamlit.app

*No setup required—start using the framework immediately.*

### Option 2: Run Locally

To run the CapsBench Evaluation Framework Streamlit app:

```shell
pip install -r requirements.txt
```

```shell
streamlit run streamlit-app/capsbench_app.py --server.maxUploadSize=500
```

To download the **CapsBench** dataset:
```shell
python dataset/download_capsbench_dataset.py
```

<details>
  <summary>APP Overview</summary>

  ![img](./streamlit-app/CapsBench_Evaluation_Framework.png)

</details>

## Understanding the Evaluation

The **CapsBench Evaluation Framework** measures how accurately generated captions answer a set of **ground truth questions derived from the CapsBench dataset**. 

**Scoring Methodology**

The score is calculated based on the following tasks to be accomplished for `gpt-4o-2024-08-06`:

1. For each question, respond with one of the following options based solely on the information present in the candidate caption:

    - **"yes"** if the answer is affirmative.
    - **"no"** if the answer is negative.
    - **"n/a"** (not applicable) if the information required to answer the question is not available in the caption.

2. Compare these answers to the reference **ground truth answers**.
3. **Calculate Score.** Compute the percentage of correct responses:

    $$
    \text{Score} = \left( \frac{\text{Number of Correct Answers}}{\text{Total Number of Questions}} \right) \times 100
    $$

    - The resulting score reflects the percentage of questions accurately addressed in the candidate captions.

Output: [Example of the DataFrame obtained as output in Markdown format](https://github.com/alexfdom/capsbench/blob/main/results/pg-captioner/results_gpt-4o-2024-08-06_pg-captioner_iter_1_.md).

We used GPT-4o-2024-08-06 for its ability to produce structured output instead of Claude 3.5 Sonnet, as the paper suggests. Nonetheless, after computing the mean of three evaluations following the paper's guidelines, **we obtained the same ranking as the [paper](https://arxiv.org/abs/2409.10695)** for the comparison between PG-Captioner, Sonnet, and GPT-4o. It's up to you to tweak the code to incorporate Claude 3.5 Sonnet, or another model, to perform the evaluation.

The following table provides a detailed comparison of the performance metrics, differences, rankings, and evaluation models for each of the three captioning models in the [CapsBench Dataset (Hugging Face)](https://huggingface.co/datasets/playgroundai/CapsBench): **PG-Captioner**, **Sonnet**, and **GPT-4o** using **CapsBench Evaluation Framework** after computing the mean of three evaluations.

------

| **Model**        | **Paper (%)** | **Code Release (%)** | **Difference (%)** | **Difference to PG-Captioner (%)**   | **Rank (Paper)** | **Rank (Code Release)** | **Evaluation Model (Paper)** | **Evaluation Model (Code Release)** |
| ---------------- | ------------- | -------------------- | ------------------ | ------------------------------------ | ---------------- | ----------------------- | ---------------------------- | ----------------------------------- |
| **PG-Captioner** | 72.19         | 76.57                | **+4.38**          | **0.00**                             | **1**            | **1**                   | Claude-3.5 Sonnet            | GPT-4o-2024-08-06                   |
| **Sonnet**       | 71.78         | 75.83                | +4.05              | -0.41 (Paper) / -0.74 (Code Release) | 2                | 2                       | Claude-3.5 Sonnet            | GPT-4o-2024-08-06                   |
| **GPT-4o**       | 70.66         | 72.67                | +2.01              | -1.53 (Paper) / -3.90 (Code Release) | 3                | 3                       | Claude-3.5 Sonnet            | GPT-4o-2024-08-06                   |

> Note: The results highlight how the evaluation models influence the reported metrics. In the paper, evaluations were conducted using the Claude-3.5 Sonnet model, while in the implementation, the GPT-4o-2024-08-06 model was used. Differences in evaluation methodology and implementation settings account for the observed variations in results.
> 
## CLI

A Benchmark for evaluating the **accuracy of synthetic captions** against the [CapsBench Dataset (Hugging Face)](https://huggingface.co/datasets/playgroundai/CapsBench).
    
### Example of Usage

First, please download the CapsBench dataset:
```shell
python dataset/download_capsbench_dataset.py
```

```shell
capsbench \
--input-file dataset/capsbench_dataset.parquet \
--img-bytes-column image \
--caption-column pg-captioner \
--questions-column questions \
--start 0 --end 200 --step 1 \
--openai-api-key <your_openai_api_key> \
--output-file results_gpt-4o-2024-08-06_pg-captioner_iter_1_.parquet

```

<details>
  <summary>CapsBench Evaluation Framework CLI Parameters</summary>

  ```
  CapsBench Evaluation Framework CLI Features
  ```



| **Parameter**        | **Short Option** | **Type** | **Description**                                              | **Default** |
| -------------------- | ---------------- | -------- | ------------------------------------------------------------ | ----------- |
| `--input-file`       | `-i`             | TEXT     | Path to the input file in Parquet/Feather format containing `image_byte` column, candidate captions columns generated by diverse models, and question columns. | None        |
| `--img-bytes-column` | `-b`             | TEXT     | `image_bytes` column to select from the Parquet/Feather file. | None        |
| `--caption-column`   | `-C`             | TEXT     | Caption column to select from the Parquet/Feather file.      | None        |
| `--questions-column` | `-q`             | TEXT     | Questions column to select from the Parquet/Feather file.    | None        |
| `--start`            | `-S`             | INTEGER  | Starting index of the rows to process (inclusive).           | 0           |
| `--end`              | `-E`             | INTEGER  | Ending index of the rows to process (exclusive).             | 1           |
| `--step`             | `-P`             | INTEGER  | Step size for processing rows.                               | 1           |
| `--openai-api-key`   | `-k`             | TEXT     | Your OpenAI API key. Can also be set via the `OPENAI_API_KEY` environment variable. | None        |


​    

  For additional documentation:
  ```shell
  capsbench --help
  ```

</details>

### Sample Terminal Output

After executing the CLI, the terminal will display real-time progress updates and summary statistics for the evaluation, including token metrics and CapsBench accuracy.
Below is an example of the output:

```markdown
Processing: 100%|████████████████████████████████████| 200/200 [01:36<00:00,  2.07it/s]

Token Metrics:

shape: (2, 2)
┌─────────────────────────────────┬────────┐
│ Metric                          ┆ Value  │
│ ---                             ┆ ---    │
│ str                             ┆ f64    │
╞═════════════════════════════════╪════════╡
│ Average Token Length per Capti… ┆ 357.04 │
│ Vocabulary Size                 ┆ 6456.0 │
└─────────────────────────────────┴────────┘

CapsBench Accuracy (%):

shape: (9, 2)
┌────────────┬───────────┐
│ statistic  ┆ value     │
│ ---        ┆ ---       │
│ str        ┆ f64       │
╞════════════╪═══════════╡
│ count      ┆ 200.0     │
│ null_count ┆ 0.0       │
│ mean       ┆ 76.5862   │
│ std        ┆ 13.671797 │
│ min        ┆ 30.0      │
│ 25%        ┆ 69.23     │
│ 50%        ┆ 76.92     │
│ 75%        ┆ 85.71     │
│ max        ┆ 100.0     │
└────────────┴───────────┘
CapsBench Accuracy (%) for //pg-captioner// ---> 76.5862

--> All scores successfully saved to results_gpt-4o-2024-08-06_pg-captioner_iter_1_.parquet.
```

## Research: How to Optimize the Evaluation

The evaluation process can be improved by modifying the dataset to include captions generated by other models. Additionally, the questions can be adjusted to cover aspects that are not currently addressed in the CapsBench dataset. A more detailed, granular evaluation can be designed to differentiate between specific aspects.

## References

- [Playground v3: Improving Text-to-Image Alignment with Deep-Fusion Large Language Models (Playground Research)](https://arxiv.org/abs/2409.10695)


  ```
  @misc{liu2024playgroundv3improvingtexttoimage,
        title={Playground v3: Improving Text-to-Image Alignment with Deep-Fusion Large Language Models}, 
        author={Bingchen Liu, Ehsan Akhgari, Alexander Visheratin, Aleks Kamko, Linmiao Xu, Shivam Shrirao, Joao Souza, Suhail Doshi, Daiqing Li},
        year={2024},
        eprint={2409.10695},
        archivePrefix={arXiv},
        primaryClass={cs.CV},
        url={https://arxiv.org/abs/2409.10695}, 
  }
  ```

- [CapsBench Dataset (Hugging Face)](https://huggingface.co/datasets/playgroundai/CapsBench)
