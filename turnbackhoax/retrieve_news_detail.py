import json
from config import NEWS_LIST_PATH, NEWS_DETAIL_PATH
from scraper import TurnBackHoaxScraper


def get_news_details(urls:list) -> dict:
    scraper = TurnBackHoaxScraper()
    news_details = []
    for url in urls:
        news_details.append(scraper.news_detail(url))
    return news_details


def load_news_list() -> dict:
    with open(NEWS_LIST_PATH, "r") as f:
        return json.loads(f.read())


def retrieve():
    urls = load_news_list()
    news_details = get_news_details(urls)
    json_object = json.dumps(news_details, indent=4)
    with open(NEWS_DETAIL_PATH, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    retrieve()
    print("Done!")
