# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import os


# from secScrap.pipeline.SecscrapPipeline

class SecscrapPipeline(FilesPipeline):

    ### Overridable Interface
    def get_media_requests(self, item, info):
        return [Request(x, meta={'filename': item.get('file_name')}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        url = request.url
        media_ext = os.path.splitext(request.url)[1]
        v = '%s%s' % (request.meta['filename'], media_ext)
        v = v.replace(' ', '')
        return v

    # def process_item(self, item, spider):
    #     return item
