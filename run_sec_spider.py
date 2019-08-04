# from twisted.internet import reactor
# from scrapy import Spider, Request
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from sec_data.sec_data.items import SecDataItem
#
#
# class SecSpider(Spider):
#     # TODO: Distributed scrapy processes; rotate IPs, research commercial usage
#     # TODO: Configure scrapy sub project; add settings conf file
#     name = "sec_table"
#     allowed_domains = ['sec.gov']
#     start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']
#
#     def start_requests(self):
#         for url in self.start_urls:
#             # yield scrapy.Request(url=url, callback=self.parse)
#             yield Request(url, self.parse)
#
#     def parse(self, response):
#         for row in response.xpath('//*[@class="list"]//tbody/tr'):
#             item = SecDataItem()
#             str = row.xpath('td[1]/a/text()').get()
#             s = str.split()
#             item['year'] = s[0]
#             item['qtr'] = s[1]
#             item['file_urls'] = row.xpath('td[1]/a/@href').get()
#             print(item)
#             yield item
#
#
# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
# runner = CrawlerRunner()
#
# d = runner.crawl(SecSpider)
# d.addBoth(lambda _: reactor.stop())
# reactor.run()  # the script will block here until the crawling is finished
#
# if __name__ == '__main__':
#     crawler = SecSpider()
#     print()