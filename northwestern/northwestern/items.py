# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NorthwesternItem(scrapy.Item):
    # define the fields for your item here like:
    urlvalue = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    email = scrapy.Field()
    program_id = scrapy.Field()
    school_id = scrapy.Field()
    research_area = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()