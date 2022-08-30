# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import hashlib

class TestBakerPipeline(FilesPipeline):
#    def get_media_request(self, item, info):
        

    def file_path(self, request, response=None, info=None, *, item):
#       file_url_hash = hashlib.shake_256(request.url.encode()).hexdigest(5)
#       file_perspective = request.url.split('/')[-2]
#       xcel_filename = f'{file_url_hash}_{file_perspective}.{}'
        file_name = item['file_name']
        return f'{file_name}.xlsx'
