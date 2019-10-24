from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class MySpider(scrapy.Spider):
    name = "sec_table"
    allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']

    # full working Python script running scrapy spider
    #  modified base parse method to print qualified links
    def parse(self, response):
        # for link in response.xpath("//tr[1]/td[1]/a[contains(@href, 'zip')]"):
        for link in response.xpath("//following::tr[1]/td[1]/a[contains(@href, 'zip')]"):
            # loader = ItemLoader(item=sItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            # loader.add_value('file_urls', absolute_url)
            # loader.add_xpath('file_name', ".//text()")
            # yield loader.load_item()
            yield print(absolute_url)

# uncomment to enable scrapy spider logging
# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()  # the script will block here until the crawling is finished
