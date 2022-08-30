# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

def remove_extension(value):
    return value.split('.')[0]

class TestBakerItem(scrapy.Item):
    # define the fields for your item here like:
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field(input_processor = MapCompose(remove_extension), output_processor = TakeFirst())
