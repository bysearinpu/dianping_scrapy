# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kindId = scrapy.Field()
    kindName = scrapy.Field()
    regionId = scrapy.Field()
    regionName = scrapy.Field()

class ShopItem(scrapy.Item):
    catId = scrapy.Field()
    shopName = scrapy.Field()
    alias = scrapy.Field()
    star = scrapy.Field()
    district = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    businessHours = scrapy.Field()
    other = scrapy.Field()
    shopUrl = scrapy.Field()
    addTime = scrapy.Field()