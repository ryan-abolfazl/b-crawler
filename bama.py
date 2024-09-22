import scrapy


class BamaSpider(scrapy.Spider):
    name = "bama"
    allowed_domains = ["bama.ir"]
    start_urls = ["https://bama.ir"]

    def parse(self, response):
        pass
