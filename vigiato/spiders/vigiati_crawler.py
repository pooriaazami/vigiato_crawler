import scrapy
from scrapy import Spider

from vigiato.utils.redis_interface import RedisInterface


class VigiatoSpider(Spider):

    def __init__(self):
        self.__redis_interface = RedisInterface()

    start_urls = [
        'https://vigiato.net/'
    ]

    def parse(self, response):
        ...
