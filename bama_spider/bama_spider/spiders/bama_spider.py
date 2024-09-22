import scrapy

from bama_spider.items import BamaItem

class BamaSpider(scrapy.Spider):
    name = 'bama'
    allowed_domains = ['bama.ir']
    start_urls = ['https://bama.ir/truck']

    def parse(self, response):
        listings = response.css('.bama-ad-holder')
        for listing in listings:
            item = BamaItem()
            item['title'] = listing.css('.bama-ad__title::text').get()
            item['price'] = listing.css('.bama-ad__price::text').get()
            item['description'] = listing.css('.bama-ad__detail-row::text').get()
            item['location'] = listing.css('.bama-ad__address::text').get()
            yield item
