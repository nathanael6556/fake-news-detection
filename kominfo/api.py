import requests
import json


class KominfoAPI:
    BASE_API_URL = "https://web.kominfo.go.id/api/v1"
    BASE_URL = "https://www.kominfo.go.id"
    HOAX_NEWS_LIST_URL = BASE_API_URL + "/contents/category/berita-hoaks"
    DEFAULT_HEADERS = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Cache-Control": "no-cache",
        "Dnt": "1",
        "Origin": BASE_URL,
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        'Referer': BASE_URL + "/",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "Sec-Ch-Ua-mobile": "?0",
        "Sec-Ch-Ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.DEFAULT_HEADERS)

    def get(self, url:str, *args, **kwargs):
        return self.session.get(url, *args, **kwargs)

    def news_list(self, page, per_page=12, keyword=""):
        params = dict(
            perPage=per_page,
            page=page,
            keyword=keyword
        )
        content = self.get(self.HOAX_NEWS_LIST_URL, params=params).content
        news_list = json.loads(content)["response"]["data"]
        return news_list

    def news_detail(self, slug):
        url = self.BASE_API_URL + "/content/detail/" + slug
        content = self.get(url).content
        return json.loads(content)["data"]
    