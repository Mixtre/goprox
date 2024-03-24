import requests
from parsel import Selector
from fp.fp import FreeProxy
from .useragents import get_random_user_agent


class GoogleSearch:
    BASE_URL = "https://www.google.com/search"

    def __init__(self, query, num=5, region=None, language=None, proxy=False):
        self.query = query
        self.num = num
        self.region = region
        self.language = language
        self.proxy = proxy
        self.headers = {"User-Agent": get_random_user_agent()}
        self.proxy_url = self.get_proxy() if proxy else None

    def build_query_params(self):
        params = {"q": self.query, "num": self.num}
        if self.region:
            params["cr"] = self.region
        if self.language:
            params["lr"] = "lang_" + self.language
        return params

    def get_proxy(self):
        if self.proxy:
            return FreeProxy().get()
        else:
            return None

    def search(self):
        proxies = (
            {"http": self.proxy_url, "https": self.proxy_url}
            if self.proxy_url
            else None
        )
        response = requests.get(
            self.BASE_URL,
            params=self.build_query_params(),
            headers=self.headers,
            proxies=proxies,
        )
        response.raise_for_status()
        return self.parse_results(response.text)

    def parse_results(self, html):
        selector = Selector(text=html)
        results = []
        for result in selector.css("div.g"):
            title = result.css("h3::text").get()
            link = result.css("a::attr(href)").get()
            description_div = result.xpath(
                './/div[@style="-webkit-line-clamp:2"]/span//text()'
            ).getall()
            description = "".join(description_div) if description_div else None
            results.append({"title": title, "link": link, "description": description})
        return results
