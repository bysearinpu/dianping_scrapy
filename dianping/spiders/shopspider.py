# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("E:\www\dianping")
from dianping.items import ShopItem
import mysql.connector
from scrapy.utils.project import get_project_settings
import json
import re
from scrapy import log

""" print re.search('营业间', '营业时间：',re.I)  # 在起始位置匹配
exit  """


dt={
            '<span class=\"fa-nYDU\"></span>':'园',
            '<span class=\"fa-uFo2\"></span>':'路',
            '<span class=\"fn-JgAR\"></span>':'6',
            '<span class=\"fn-z7mV\"></span>':'8',
            '<span class=\"fa-v4H9\"></span>':'号',
            '<span class=\"fa-roqL\"></span>':'广',
            '<span class=\"fa-fyHj\"></span>':'场',
            '<span class=\"fn-8sO4\"></span>':'0',
            '<span class=\"fn-fBCW\"></span>':'2',
            '<span class=\"fn-9HQC\"></span>':'3',
            '<span class=\"fn-YkOs\"></span>':'7',
            '<span class=\"fn-mLCm\"></span>':'9',
            '<span class=\"fn-ehy5\"></span>':'5',
            '<span class=\"fn-M2MZ\"></span>':'4',
            '<span class=\"fa-rWSg\"></span>':'安',
            '<span class=\"fa-1E3W\"></span>':'福',
            '<span class=\"fa-EMWp\"></span>':'泉',
            '<span class=\"fa-gtFC\"></span>':'金',
            '<span class=\"fa-nNvy\"></span>':'南',
            '<span class=\"info-name\">电话：</span>':'',
            '<span class=\"fa-qGEh\"></span>':'街',
            '<span class=\"fa-xlWa\"></span>':'阳',
'<span class=\"fa-Vd5r\"></span>':'武',
'<span class=\"fa-PkWO\"></span>':'北',
'<span class=\"fa-nkl1\"></span>':'兴',
'<span class=\"fa-IKB1\"></span>':'区',
'<span class=\"fa-BP9P\"></span>':'家',
'<span class=\"fa-kBCT\"></span>':'珠',
'<span class=\"fa-zZW8\"></span>':'木',
'<span class=\"fa-hEEN\"></span>':'城',
'<span class=\"fa-Sw7Y\"></span>':'源',
'<span class=\"fa-FTN1\"></span>':'新',
'<span class=\"fa-TyL3\"></span>':'内',
'<span class=\"fa-Sf2D\"></span>':'远',
'<span class=\"fa-AIUV\"></span>':'石',
'<span class=\"fa-8kT9\"></span>':'齐',
'<span class=\"fa-fxtZ\"></span>':'光',
'<span class=\"fa-cI7F\"></span>':'华',
'<span class=\"fa-YOUz\"></span>':'心',
'<span class=\"fa-ZByg\"></span>':'一',
'<span class=\"fa-LuI3\"></span>':'乌',
'<span class=\"fa-qsmS\"></span>':'东',
'<span class=\"fa-OCiZ\"></span>':'德',
'<span class=\"fa-og0e\"></span>':'厦',
'<span class=\"fa-oI6a\"></span>':'沿',
'<span class=\"fa-4sKr\"></span>':'长',
'<span class=\"fa-ERb1\"></span>':'临',
'<span class=\"fa-uPoC\"></span>':'威',
'<span class=\"fa-dQ14\"></span>':'古',
'<span class=\"fa-QVYJ\"></span>':'都',
'<span class=\"fa-8SVR\"></span>':'康',
'<span class=\"fa-YNkj\"></span>':'香',
'<span class=\"fa-JDAi\"></span>':'乐',
'<span class=\"fa-3AFy\"></span>':'名',
'<span class=\"fa-oJuw\"></span>':'宾',
'<span class=\"fa-KuAn\"></span>':'中',
'<span class=\"fa-6elk\"></span>':'弄',
'<span class=\"fa-wqp9\"></span>':'襄',
'<span class=\"fa-YXVa\"></span>':'茂',
'<span class=\"fa-3Wir\"></span>':'门',
'<span class=\"fa-SKi4\"></span>':'嘉',
'<span class=\"fa-PU6K\"></span>':'宁',
'<span class=\"fa-gWDA\"></span>':'村',
'<span class=\"fa-cmaR\"></span>':'泰',
'<span class=\"fa-xj9n\"></span>':'鲁',
'<span class=\"fa-SGc9\"></span>':'常',
'<span class=\"fa-iFuW\"></span>':'民',
'<span class=\"fa-4NqU\"></span>':'湾',
'<span class=\"fa-CK4H\"></span>':'站',
'<span class=\"fa-EnVA\"></span>':'环',
'<span class=\"fa-s45m\"></span>':'业',
'<span class=\"fa-T5U3\"></span>':'永',
'<span class=\"fa-gMzY\"></span>':'海',
'<span class=\"fa-pqMD\"></span>':'平',
'<span class=\"fa-wrhM\"></span>':'梅',
'<span class=\"fa-zRN5\"></span>':'大',
'<span class=\"fa-RR7c\"></span>':'江',
'<span class=\"fa-umRL\"></span>':'西',
'<span class=\"fa-l0op\"></span>':'创',
'<span class=\"fa-5iqW\"></span>':'银',
'<span class=\"fa-5MeR\"></span>':'定',
'<span class=\"fa-h3ZF\"></span>':'州',
'<span class=\"fa-6Fz9\"></span>':'道',
'<span class=\"fa-maxF\"></span>':'京',
'<span class=\"fa-sbZN\"></span>':'太',
'<span class=\"fa-KUsC\"></span>':'山',
'<span class=\"fa-2iI9\"></span>':'陕',
'<span class=\"fa-vFdl\"></span>':'镇',
'<span class=\"fa-caVI\"></span>':'龙',
'<span class=\"fa-EP5X\"></span>':'明',
'<span class=\"fa-ch5G\"></span>':'交',
'<span class=\"fa-fEZK\"></span>':'四',
'<span class=\"fa-CobC\"></span>':'上',
'<span class=\"fa-NMDA\"></span>':'隆',
'<span class=\"fa-PIcv\"></span>':'信',
'<span class=\"fa-g7k2\"></span>':'富',
'<span class=\"fa-QlAG\"></span>':u'工',
'<span class=\"fa-0Ye1\"></span>':u'贵',
'<span class=\"fa-vw9C\"></span>':u'健',
'<span class=\"fa-akSw\"></span>':u'文',
'<span class=\"fa-atkG\"></span>':u'学',
'<span class=\"fa-UHI0\"></span>':u'进',
'<span class=\"fa-X5v8\"></span>':u'红',
'<span class=\"fa-rWXC\"></span>':u'林',
'<span class=\"fa-HtQ6\"></span>':u'宜',
'<span class=\"fa-DJLr\"></span>':u'市',
'<span class=\"fa-qgi0\"></span>':u'扬',
'<span class=\"fa-v5ae\"></span>':u'川',
'<span class=\"fa-k6E0\"></span>':u'温',
'<span class=\"fa-ow9z\"></span>':u'浙',
'<span class=\"fa-CkGW\"></span>':u'友',
'<span class=\"fa-BXP1\"></span>':u'春',
'<span class=\"fa-A4Uv\"></span>':u'桂',
'<span class=\"fa-C497\"></span>':u'无',
'<span class=\"fa-1Zxs\"></span>':u'滨',
'<span class=\"fa-P5JU\"></span>':u'尔',
'<span class=\"fa-xZfp\"></span>':u'义',
'<span class=\"fa-24iC\"></span>':u'汉',
'<span class=\"fa-QIEU\"></span>':u'府',
'<span class=\"fa-7SPt\"></span>':u'治',
'<span class=\"fa-RKdi\"></span>':u'博',
'<span class=\"fa-1THP\"></span>':u'肇',
'<span class=\"fa-qmn2\"></span>':u'湖',
'<span class=\"fa-auNX\"></span>':u'锦',
'<span class=\"fa-uV9t\"></span>':u'体',
'<span class=\"fa-jbS0\"></span>':u'九',
'<span class=\"fa-hKg0\"></span>':u'汾',
'<span class=\"fa-CNMl\"></span>':u'遵',
'<span class=\"fa-Z6xm\"></span>':u'衡',
'<span class=\"fa-TTdP\"></span>':u'化',
'<span class=\"fa-I3Sz\"></span>':u'建',
'<span class=\"fa-mJs6\"></span>':u'庆',
'<span class=\"fa-KuAn\"></span>':u'中',
'<span class=\"fa-IYeY\"></span>':u'昌',
'<span class=\"fa-vQi7\"></span>':u'前',
'<span class=\"fa-OJdm\"></span>':u'凤',
'<span class=\"fa-vZ5R\"></span>':u'公',
'<span class=\"fa-JvRr\"></span>':u'风',
'<span class=\"fa-5KhO\"></span>':u'青',
'<span class=\"fa-QmOV\"></span>':u'吉',
'<span class=\"fa-Y45h\"></span>':u'花',
'<span class=\"fa-LPi8\"></span>':u'坊',
'<span class=\"fa-OM3l\"></span>':u'生',
'<span class=\"fa-hwaN\"></span>':u'云',
'<span class=\"fa-vdG1\"></span>':u'河',
'<span class=\"fa-qD7S\"></span>':u'八',
'<span class=\"fa-DrPP\"></span>':u'人',
'<span class=\"fa-Ca71\"></span>':u'淮',
'<span class=\"fa-3gbK\"></span>':u'惠',
'<span class=\"fa-LRnl\"></span>':u'通',
'<span class=\"fa-RAiK\"></span>':u'旗',
'<span class=\"fa-1miw\"></span>':u'胜',
'<span class=\"fa-EF0j\"></span>':u'波',
'<span class=\"fa-8Y9j\"></span>':u'爱',
'<span class=\"fa-Penx\"></span>':u'成',
'<span class=\"fa-6dIi\"></span>':u'津',
'<span class=\"fa-ZUq1\"></span>':u'肥',
'<span class=\"fa-TZWV\"></span>':u'港',
'<span class=\"fa-rF1H\"></span>':u'绍',
'<span class=\"fa-D9QB\"></span>':u'苏',
'<span class=\"fa-FNWi\"></span>':u'重',
'<span class=\"fa-iE2v\"></span>':u'徐',
'<span class=\"fa-QoiS\"></span>':u'岛',
'<span class=\"fa-s6Ou\"></span>':u'年',
'<span class=\"fa-7SQx\"></span>':u'济',
'<span class=\"fa-fdkT\"></span>':u'黄',
'<span class=\"fa-q4sw\"></span>':u'合',
'<span class=\"fa-56qX\"></span>':u'育',
'<span class=\"fa-IUTi\"></span>':u'天',
'<span class=\"fa-n8Xb\"></span>':u'和',
'<span class=\"fa-YLIR\"></span>':u'黑',
'<span class=\"fa-3TLD\"></span>':u'台',
'<span class=\"fa-y9oU\"></span>':u'庄',
'<span class=\"fa-fgcj\"></span>':u'烟',
'<span class=\"fa-PftN\"></span>':u'关',
'<span class=\"fa-nYRf\"></span>':u'藏',
'<span class=\"fa-RblF\"></span>':u'农',
'<span class=\"fa-vtnI\"></span>':u'沙',
'<span class=\"fa-9NXi\"></span>':u'蒙',
'<span class=\"fa-s67U\"></span>':u'肃',
'<span class=\"fa-c7Sd\"></span>':u'迎',
'<span class=\"fa-wk9q\"></span>':u'头',
'<span class=\"fa-04AP\"></span>':u'教',
'<span class=\"fa-NqTB\"></span>':u'曙',
'<span class=\"fa-aRMf\"></span>':u'连',
'<span class=\"fa-i65F\"></span>':u'汕',
'<span class=\"fa-NNij\"></span>':u'机',
'<span class=\"fa-z7tb\"></span>':u'鞍',
'<span class=\"fa-YM25\"></span>':u'澳',
'<span class=\"fa-iJ7K\"></span>':u'才',
'<span class=\"fa-KuAn\"></span>':u'中',
'<span class=\"fa-VjJz\"></span>':u'廊'
        }

class shopsipder(scrapy.Spider):
    name = "shop"
    allowed_domains = ["dianping.com"]
    start_urls =[
        "http://www.dianping.com/shanghai/ch20/"
    ]

    def start_requests(self):
        settings=get_project_settings()
        conn=mysql.connector.connect(host=settings['MYSQL_HOST'],user=settings['MYSQL_USER'],password=settings['MYSQL_PWD'],database=settings['MYSQL_DB'],charset='utf8')
        cursor = conn.cursor()
        #SELECT * FROM cat WHERE kindName='服装' and catId not in(43,60,59,39,25)
        cursor.execute("SELECT * FROM cat WHERE kindName='轻奢'  ")
        res=cursor.fetchall()
        cursor.close()
        conn.close()
        for row in res:
            url = self.start_urls[0]+"g"+str(row[2])+"r"+str(row[4])
            request = scrapy.Request(url,callback=self.parse)
            para={
                'catId':row[0],
                'url':url
            }
            request.meta['para']=para
            yield request

    def parse(self,response):
        maxpage = response.xpath("//div[@class='page']/a[last()-1]/text()").extract_first() 
        para = response.meta['para']
        if not maxpage:
           maxpage=1 

        #maxpage=1
        for pagenum in range(int(maxpage)):
            request = scrapy.Request(para['url']+"p"+str(pagenum+1),callback=self.parse_pagelist)
            request.meta['para']=para
            yield request

    def parse_pagelist(self,response):
        
        for shopurl in response.xpath("//div[@id='shop-all-list']/ul/li/div[@class='pic']/a/@href").extract():
            item=ShopItem()
            item['shopUrl']=shopurl
            request = scrapy.Request(shopurl,callback=self.parse_shop) 
            request.meta['item']=item
            request.meta['para']=response.meta['para']
            yield request

    def parse_shop(self,response):
        item=response.meta['item']
        basic = response.xpath("//div[@id='basic-info']")
        item['shopName'] = basic.xpath("h1[@class='shop-name']/child::text()").extract_first()

        item['catId'] = response.meta['para']['catId']

        item['star'] = basic.xpath("div[@class='brief-info']/span[contains(@class,'mid-rank-stars')]/@title").extract_first()
        if not item['star']:
            item['star'] = basic.xpath("div[@class='brief-info']/span[contains(@class,'mid-rank-stars')]/@class").extract_first()

        item['other'] = self.trancate(basic.xpath("div[@class='brief-info']//span[@class='item']/child::node()").extract())
        
        address = self.trancate(basic.xpath("//span[@id='address']/child::node()").extract())
        if not address:
           address=self.trancate(basic.xpath("//span[@itemprop='street-address']/child::node()").extract())
        item['address'] = address
        
        item['tel'] = self.trancate(basic.xpath("p[@class='expand-info tel']/child::node()").extract())


        item['district'] = response.xpath("//div[@class='breadcrumb']/a[2]/text()").extract_first()
        
        if item['district'] and (not re.search(u"区".decode('utf-8'),item['district'],re.I)):
             item['district'] = response.xpath("//div[@class='breadcrumb']/a[3]/text()").extract_first()
        
        item['businessHours'] = item['alias'] =None
        els=basic.xpath("//div[contains(@class,'J-other')]/p[contains(@class,'info-indent')]/span[@class='item']/text()").extract()
        
        if len(els)==1:
           item['businessHours']=self.trancate(els[0])
        elif len(els)==2:
           item['alias']=self.trancate(els[0])
           item['businessHours'] =self.trancate(els[1])
        else :
           log.msg("被ban啦哈哈")
           #exit('被ban,'+item['shopUrl'])
        yield item
        #print json.dumps(item,encoding="UTF-8",ensure_ascii=False)
    
    """专用于母婴购物行业的商店 
    def parse_shop(self,response):
        item=response.meta['item']
        basic = response.xpath("//div[contains(@class,'shop-info-inner')]")
        item['shopName'] = basic.xpath("//h1[@class='shop-title']/text()").extract_first()

        item['catId'] = response.meta['para']['catId']

        item['star'] = basic.xpath("//span[contains(@class,'item-rank-rst')]/@title").extract_first()
     

        item['other'] =""
        

        address=basic.xpath("//span[@itemprop='street-address']/text()").extract_first()
        item['address'] = address
        
        item['tel'] = basic.xpath("//a[@id='J-showPhoneNumber']/@data-real").extract_first()


        item['district'] = response.xpath("//div[@class='breadcrumb']/a[2]/text()").extract_first()
        
        if item['district'] and (not re.search(u"区".decode('utf-8'),item['district'],re.I)):
             item['district'] = response.xpath("//div[@class='breadcrumb']/a[3]/text()").extract_first()
        
        item['businessHours'] = item['alias'] =""
      
           #exit('被ban,'+item['shopUrl'])
        yield item
        #print json.dumps(item,encoding="UTF-8",ensure_ascii=False) """
    
    def trancate(self,ls_var):
        """ res = []
        tempstr=''
        for i in ls_var:
            varstr = i.strip()
            if varstr=='':
                continue
            else:
               if varstr in dt:
                   tempstr += dt[varstr]
               else:
                  if tempstr != '':
                      res.append(tempstr)
                      tempstr=''
                  res.append(varstr)

        if tempstr != '':
            res.append(tempstr) """
        def ignoreCheck(var):
            if var=='' :
                return True
            elif re.search('class=\"info-name\"',var,re.I):
                return True
            elif re.search('data-click-name=',var,re.I):
                return True
            else:
                return False
             
        tempstr=''
        for i in ls_var:
            varstr = i.strip()
            if ignoreCheck(varstr):
                continue
            else:
               if varstr in dt:
                   tempstr += dt[varstr]
               else:
                   tempstr += str(varstr)
        return tempstr
                

                

        