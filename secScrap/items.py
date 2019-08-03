# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
import os

def remove_extension(value):
    return os.path.splitext(value)[0]

class SecDataItem(scrapy.Item):
    # collection = table = 'zip_files'

    id = scrapy.Field()
    qtr = scrapy.Field()
    year = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field(
        input_processor = MapCompose(remove_extension),
        output_processor = TakeFirst()
    )
