from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class SecSpider(scrapy.Spider):
    name = "sec_table"

    def start_requests(self):
        urls = [
            'https://www.sec.gov/dera/data/financial-statement-data-sets.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class="list"]//tbody/tr'):
            yield {
                'https://www.sec.gov': row.xpath('td[1]/a/@href').extract()
            }


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(SecSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
