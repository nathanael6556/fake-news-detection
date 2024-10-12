import json
from config import NEWS_LIST_PATH
from api import KominfoAPI


def get_news_list(start_index, end_index, per_page=12):
    api = KominfoAPI()
    result = []
    for page in range(start_index, end_index+1, per_page):
        if page + per_page > end_index:
            per_page = end_index - page + 1
        result += [data["slug"] for data in api.news_list(page, per_page)]
    return result


def retrieve(start_index, end_index, per_page=12):
    news_list = get_news_list(start_index, end_index, per_page)
    json_object = json.dumps(news_list, indent=4)
    with open(NEWS_LIST_PATH, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    retrieve(1, 3)
    print("Done!")
