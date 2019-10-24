from scrapy import Spider
from scrapy.loader import ItemLoader
from secScrap.items import SecDataItem


class SecSpider(Spider):
    # TODO: Distributed scrapy processes; rotate IPs, research commercial usage
    # TODO: Configure scrapy sub project; add settings conf file
    name = "sec_table"
    allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/dera/data/financial-statement-data-sets.html']

    def parse(self, response):
        for link in response.xpath("//following::tr[1]/td[1]/a[contains(@href, 'zip')]"):
            # for link in response.xpath("//tr[1]/td[1]/a[contains(@href, 'zip')]"):
            loader = ItemLoader(item=SecDataItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            loader.add_xpath('file_name', ".//text()")
            yield loader.load_item()
