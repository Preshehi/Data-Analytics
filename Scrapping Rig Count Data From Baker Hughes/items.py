# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

#Remove the extension of the file to capture just the file name
def remove_extension(value):
    return value.split('.')[0]

#Define an item that will hold the scraped data
class TestBakerItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field(input_processor = MapCompose(remove_extension), output_processor = TakeFirst())
