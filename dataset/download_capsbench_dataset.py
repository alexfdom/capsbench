import pandas as pd

df = pd.read_parquet("hf://datasets/playgroundai/CapsBench/data/train-00000-of-00001.parquet")
df.to_parquet("dataset/capsbench_dataset.parquet")