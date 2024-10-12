import re
import requests
from bs4 import BeautifulSoup


class TurnBackHoaxScraper:
    BASE_URL = "https://turnbackhoax.id"
    
    def __init__(self):
        self.session = requests.Session()

    def get(self, url:str, *args, **kwargs):
        return self.session.get(url, *args, **kwargs)

    def news_list(self, page):
        url = self.BASE_URL + "/page/" + str(page)
        content = self.get(url, allow_redirects=True).content
        page = BeautifulSoup(content, features="lxml")
        links = page.select("h3.entry-title > a")
        return [link["href"] for link in links]

    def news_detail(self, url):
        content = self.get(url).content
        page = BeautifulSoup(content, features="lxml")
        title = page.select("h1.entry-title")[0].text
        timestamp = page.select("span.entry-meta-date > a")[0].text
        author = page.select("span.entry-meta-author > a")[0].text
        tags = page.select("span.entry-meta-categories > a")[0].text
        paragraphs = page.select("div.entry-content > p")
        full_text = "\n".join([p.text for p in paragraphs])

        return dict(
            Title=title,
            Timestamp=timestamp,
            FullText=full_text,
            Tags=tags,
            Author=author,
            Url=url
        )
    