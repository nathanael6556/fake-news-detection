import json
from config import NEWS_LIST_PATH
from scraper import TurnBackHoaxScraper


def get_news_list(start_index, end_index, per_page):
    scraper = TurnBackHoaxScraper()
    result = []
    for page in range(start_index, end_index+1, per_page):
        if page + per_page > end_index:
            per_page = end_index - page + 1
        result += scraper.news_list(page)
    return result


def retrieve(start_index, end_index):
    news_list = get_news_list(start_index, end_index, per_page=20)
    json_object = json.dumps(news_list, indent=4)
    with open(NEWS_LIST_PATH, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    retrieve(1, 800)
    print("Done!")
