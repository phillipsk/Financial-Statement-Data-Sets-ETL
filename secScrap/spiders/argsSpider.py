from scrapy import Spider
from scrapy.loader import ItemLoader
from secScrap.items import SecDataItem


class SecSpider(Spider):
    name = "args_spider"
    allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, self.parse)

    # when passing arguements to a spider, the __init__ method binds the value to self
    # def __init__(self, year=None, *args, **kwargs):
    #     super(SecSpider, self).__init__(*args, **kwargs)
    #     # self.start_urls = ['http://www.example.com/categories/%s' % year]
    #     # self.start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']
    #     self.year = year

    def parse(self, response):
        # sample code debugging various python String concatenation methods
        # z = '//following::tr[1]/td[1]/a[contains(@href, {})]/a[contains(@href, {self.year})]'.format("'zip'", "'2016'")
        # z = '//following::tr[1]/td[1]/a[contains(@href, {})]/a[contains(@href, {''})]'.format(self.year)
        # for link in response.xpath("//following::tr[1]/td[1]/a[contains(@href, 'zip')]"):
        # for link in response.xpath("//tr[1]/td[1]/a[contains(@href, 'zip')]"):
        # t = '//following::tr[1]/td[1]/a[contains(@href,' + str(self.year) + ')]'
        # for link in response.xpath(t):

        for link in response.xpath('//following::tr[1]/td[1]/a[contains(@href,' + str(self.year) + ')]'):
            loader = ItemLoader(item=SecDataItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            loader.add_xpath('file_name', ".//text()")
            yield loader.load_item()
