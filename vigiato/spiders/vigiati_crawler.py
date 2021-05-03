import scrapy
from scrapy import Spider


class VigiatoSpider(Spider):
    start_urls = [
        'https://vigiato.net/'
    ]
