# -*- coding: utf-8 -*
import scrapy
import sys
sys.path.append("E:\www\dianping")
import mysql.connector
from scrapy.utils.project import get_project_settings



kindlist=["其他服饰鞋包",
"综合商场",
"珠宝饰品",
"运动户外",
"折扣店",
"服装",
"化妆品",
"眼镜店",
"母婴购物",
"数码产品",
"杂货礼品",
"鞋靴",
"内衣",
"箱包",
"居家日用",
"快时尚",
"轻奢",
"配饰",
"免税店",
"书店音像",
"特色集市"
]

class dianpingsipder(scrapy.Spider):
    name = "dp"
    allowed_domains = ["dianping.com"]
    start_urls =[
        "http://www.dianping.com/shanghai/ch20/g32739"
    ]



    def start_requests(self):
        pass

