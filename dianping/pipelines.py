# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
from scrapy.utils.project import get_project_settings


class DianpingPipeline(object):
    def __init__(self):
        settings=get_project_settings()
        self.conn=mysql.connector.connect(host=settings['MYSQL_HOST'],user=settings['MYSQL_USER'],password=settings['MYSQL_PWD'],database=settings['MYSQL_DB'])
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        insert_sql ="""
           insert into cat(city,kindId,kindName,regionId,regionName) values('上海',%s,%s,%s,%s);
        """
        self.cursor.execute(insert_sql,(item.get('kindId'),item.get('kindName'),item.get('regionId'),item.get('regionName')))
        self.conn.commit()
        return item

class ShopPipeline(object):
    def __init__(self):
        settings=get_project_settings()
        self.conn=mysql.connector.connect(host=settings['MYSQL_HOST'],user=settings['MYSQL_USER'],password=settings['MYSQL_PWD'],database=settings['MYSQL_DB'])
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        insert_sql ="""
           insert into shop(catId,shopName,alias,star,district,address,tel,businessHours,other,shopUrl) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """
        try:
            self.cursor.execute(insert_sql,(
            item.get('catId'),
            item.get('shopName'),
            item.get('alias'),
            item.get('star'),
            item.get('district'),
            item.get('address'),
            item.get('tel'),
            item.get('businessHours'),
            item.get('other'),
            item.get('shopUrl')
            ))
            self.conn.commit()
        except:
            print 11111111111111111111111111111111111111111,'db op error'
        
