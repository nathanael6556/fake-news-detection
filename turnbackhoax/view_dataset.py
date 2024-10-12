import pandas as pd
from config import DATASET_PATH


if __name__ == "__main__":
    df = pd.read_csv(DATASET_PATH)
    print(df.info())
    print(df)
