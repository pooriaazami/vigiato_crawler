import scrapy
from scrapy import Spider

from vigiato.utils.redis_interface import RedisInterface
from vigiato.utils.utils import check_link


class VigiatoSpider(Spider):
    name = "vigiato"

    def __init__(self):
        self.__redis_interface = RedisInterface()
        self.__counter = 1

    start_urls = [
        'https://vigiato.net/'
    ]

    def page_parser(self, response):
        text = ""
        for tag in response.css('p'):
            for data in tag.css('::text').getall():
                text += data

        with open(f'data/{self.__counter}.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        self.__counter += 1

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if check_link(link) and self.__redis_interface.add_item(link):
                self.page_parser(response)
                yield scrapy.Request(response.urljoin(link))
