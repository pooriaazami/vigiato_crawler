import scrapy
from jsonschema._types import is_any
from scrapy import Spider

from vigiato.utils.redis_interface import RedisInterface
from vigiato.utils.utils import check_link


class VigiatoSpider(Spider):
    name = "vigiato"

    def __init__(self):
        self.__redis_interface = RedisInterface()

    start_urls = [
        'https://vigiato.net/'
    ]

    def page_parser(self, response):
        text = ""
        for tag in response.css('p'):
            for data in tag.css('::text').getall():
                text += data

        with open('text.txt', 'a', encoding='utf-8') as file:
            file.write(text)

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if check_link(link) and self.__redis_interface.add_item(link):
                self.page_parser(response)
                yield scrapy.Request(response.urljoin(link))
            else:
                print(check_link(link))
