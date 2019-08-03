import scrapy
from scrapy import Spider, Request

from sec_data.sec_data.items import SecDataItem


class SecSpider(Spider):
    # TODO: Distributed scrapy processes; rotate IPs, research commercial usage
    # TODO: Configure scrapy sub project; add settings conf file
    name = "sec_table"
    allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']

    def start_requests(self):
        for url in self.start_urls:
            # yield scrapy.Request(url=url, callback=self.parse)
            yield Request(url, self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class="list"]//tbody/tr'):
            item = SecDataItem()
            str = row.xpath('td[1]/a/text()').get()
            str.split()
            item['qtr'] = row.xpath('td[1]/a/text()').get()
            item['qtr'] = str[1]
            item['link'] = row.xpath('td[1]/a/@href').get()
            yield item
