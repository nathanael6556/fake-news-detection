import re
import json
from config import NEWS_DETAIL_PATH, DATASET_PATH
import pandas as pd


def parse(news_detail:dict) -> dict:
    narasi_match = re.search(r"\[?NARASI\]?\s*\:(.+?)\[?PENJELASAN\]?", news_detail["FullText"], flags=re.MULTILINE|re.IGNORECASE|re.DOTALL)
    if narasi_match is not None:
        narasi = narasi_match.group(1)
        narasi = narasi.strip()
        narasi = narasi.strip("=")
        narasi = narasi.strip()
    else:
        narasi = None
    news_detail["Narasi"] = narasi
    news_detail["hoax"] = 1
    return news_detail


def prepare() -> None:
    with open(NEWS_DETAIL_PATH, "r") as f:
        news_details = json.loads(f.read())
    
    dataset = []
    for news_detail in news_details:
        cleaned_data = parse(news_detail)
        dataset.append(cleaned_data)
    
    df = pd.DataFrame(dataset)
    df.to_csv(DATASET_PATH)


if __name__ == "__main__":
    prepare()
    print("Done!")
