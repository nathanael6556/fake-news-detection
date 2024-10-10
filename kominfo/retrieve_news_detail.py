import json
from config import NEWS_LIST_PATH, NEWS_DETAIL_PATH
from api import KominfoAPI


def get_news_details(slug_list:list) -> dict:
    api = KominfoAPI()
    news_details = []
    for slug in slug_list:
        news_details.append(api.news_detail(slug))
    return news_details


def load_news_list() -> dict:
    with open(NEWS_LIST_PATH, "r") as f:
        return json.loads(f.read())


def retrieve():
    slug_list = load_news_list()
    news_details = get_news_details(slug_list)
    json_object = json.dumps(news_details, indent=4)
    with open(NEWS_DETAIL_PATH, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    retrieve()
    print("Done!")
