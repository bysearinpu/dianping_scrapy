# -*- coding: utf-8 -*
import scrapy
import sys
sys.path.append("E:\www\dianping")
import mysql.connector
from scrapy.utils.project import get_project_settings



kindlist=[u"其他服饰鞋包",
u"综合商场",
u"珠宝饰品",
u"运动户外",
u"折扣店",
u"服装",
u"化妆品",
u"眼镜店",
u"母婴购物",
u"数码产品",
u"杂货礼品",
u"鞋靴",
u"内衣",
u"箱包",
u"居家日用",
u"快时尚",
u"轻奢",
u"配饰",
u"免税店",
u"书店音像",
u"特色集市"
]

class dianpingsipder(scrapy.Spider):
    name = "dp"
    allowed_domains = ["dianping.com"]
    start_urls =[
        "http://www.dianping.com/shanghai/ch20/g32739"
    ]



    def start_requests(self):
        pass

