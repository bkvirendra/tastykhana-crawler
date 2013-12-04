# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TastykhanaItem(Item):
    # define the fields for your item here like:
    name = Field()
    address = Field()
    timings = Field()
    cuisine = Field()
    logo = Field()
    veg = Field()
    id = Field()
    non_veg = Field()
    pass
