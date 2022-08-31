import scrapy
from ..items import TestBakerItem

#Create a spider with the website to be crawled
class BakerSpider(scrapy.Spider):
    name = 'baker'
    allowed_domains = ['bakerhughes.com']
    start_urls = ['https://rigcount.bakerhughes.com/intl-rig-count']

    #Define where exactly to look on the page
    def parse(self, response):
        rig_data = response.css('div.file-link a::attr(href)').get()
        rig_data = response.urljoin(rig_data)
        item = TestBakerItem()
        item['file_urls'] = [rig_data]
        item['file_name'] = response.css('div.file-link a::attr(title)').get()
        yield item
