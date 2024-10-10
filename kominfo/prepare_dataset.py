import re
import json
from config import NEWS_DETAIL_PATH, DATASET_PATH
import pandas as pd
from bs4 import BeautifulSoup


def parse(news_detail:dict) -> dict:
    title = news_detail["title"]
    category = re.match("\[([A-Z]+)\]", title).group(1).lower()
    title = title[len(category) + 3:]
    title = title.strip()

    body = news_detail["body"]
    body = BeautifulSoup(body, features="lxml").text
    body = body.strip("Penjelasan: ")
    body = body[:body.rfind("Kategori: ")]
    body = body.strip()

    return dict(
        title=title,
        category=category,
        body=body
    )


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
