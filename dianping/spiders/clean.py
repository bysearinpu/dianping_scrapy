# -*- coding: utf-8 -*
import mysql.connector
from scrapy.utils.project import get_project_settings
import re
import webbrowser

""" webbrowser.open("http://www.dianping.com/shop/6137860")
exit() """

hz=[
"锡",
"潍",
"幸",
"县",
"乡",
"向",
"佛",
"冈",
"祥",
"清",
"夏",
"结",
"谊",
"保",
"设",
"辽",
"中",
"利",
"皇",
"开",
"洛",
]

dictaa = {
'<span class=\"fa-A1C4\"></span>':u'锡',
'<span class=\"fa-JQXE\"></span>':u'潍',
'<span class=\"fa-evoK\"></span>':u'幸',
'<span class=\"fa-IUb6\"></span>':u'县',
'<span class=\"fa-650U\"></span>':u'乡',
'<span class=\"fa-jHlv\"></span>':u'向',
'<span class=\"fa-y2Px\"></span>':u'佛',
'<span class=\"fa-B7A9\"></span>':u'冈',
'<span class=\"fa-2qhc\"></span>':u'祥',
'<span class=\"fa-KJRK\"></span>':u'清',
'<span class=\"fa-WWqM\"></span>':u'夏',
'<span class=\"fa-QB6X\"></span>':u'结',
'<span class=\"fa-O3VJ\"></span>':u'谊',
'<span class=\"fa-tgpv\"></span>':u'保',
'<span class=\"fa-5GEc\"></span>':u'设',
'<span class=\"fa-ZsjH\"></span>':u'辽',
'<span class=\"fa-KuAn\"></span>':u'中',
'<span class=\"fa-e2s4\"></span>':u'利',
'<span class=\"fa-E0G9\"></span>':u'皇',
'<span class=\"fa-Lfat\"></span>':u'开',
'<span class=\"fa-NM88\"></span>':u'洛',
}

class cleanobj():

  def __init__(self):
      conf = get_project_settings()
      self.conn= mysql.connector.connect(host=conf["MYSQL_HOST"],user=conf['MYSQL_USER'],password=conf['MYSQL_PWD'],database=conf['MYSQL_DB'],charset='utf8')
      self.cur = self.conn.cursor()
      self.cur.execute("select shopId,address,tel,star from shop limit 10000000")
      self.res = self.cur.fetchall()

      
      tag=[]
      for row in self.res:
        if row[1]:
            tagls=re.findall(r'class=\"([a-zA-Z0-9-]{7})\"',row[1])
            tag=tag+tagls
        #new_addr= re.sub(r'\<span class=\"([a-zA-Z0-9-]{7})\"\>\<\/span\>',th,row[1].encode("utf-8"))
        #cur.execute("update shop set address=%s where shopId=%s",(new_addr,row[0]))
      #exit()
      self.tag = list(set(tag))
      
  def  __del__(self):
      self.cur.close()
      self.conn.close()

  def showtag(self):
    
    s=''
    for r in self.tag:
        s=s+'<span class="'+r+'"></span>'
    print s

  def printDict(self,hz):
       i=0
       for r in self.tag:
          print "'<span class=\\\"" + r.encode("utf-8") +"\\\"></span>\':'"+hz[i]+"',"
          i=i+1

  def updateDb(self,dictvar):
      def th(m):
         v = m.group().encode("utf-8")
         if v in dictvar:
            return dictvar[v].encode("utf-8")

      for row in self.res:
          if row[1]:
             new_addr= re.sub(r'\<span class=\"([a-zA-Z0-9-]{7})\"\>\<\/span\>',th,row[1].encode("utf-8"))
             #print new_addr
             self.cur.execute("update shop set address=%s where shopId=%s",(new_addr,row[0]))

  def updateTel(self):
      for row in self.res:
          id=0
          content=""
          if row[2] and re.findall(u"无".encode("utf-8"),row[2].encode("utf-8")):
              id = row[0]
              
          if row[2] and re.findall("<span class=\"item\" itemprop=\"tel\">",row[2]):
              n1=row[2].replace("<span class=\"item\" itemprop=\"tel\">","")
              n2=n1.replace("</span>",",")
              id = row[0]
              content = n2
          if id :
             self.cur.execute("update shop set tel=%s where shopId=%s",(content,id))

  def updateStar(self):
      starmap={
          "mid-rank-stars mid-str0":"该商户暂无星级",
          "mid-rank-stars mid-str50":"五星商户",
          "mid-rank-stars mid-str45":"准五星商户",
          "mid-rank-stars mid-str40":"四星商户",
          "mid-rank-stars mid-str35":"准四星商户",
          "mid-rank-stars mid-str30":"三星商户",
          "mid-rank-stars mid-str25":"准三星商户",
          "mid-rank-stars mid-str20":"二星商户",
          "mid-rank-stars mid-str15":"准二星商户",
          "mid-rank-stars mid-str10":"一星商户",
          "mid-rank-stars mid-str05":"准一星商户",
      }
      for row in self.res:
        if row[3]:
          s=row[3].strip()
          if s in starmap:
              self.cur.execute("update shop set star=%s where shopId=%s",(starmap[s],row[0]))
          
      

if __name__=="__main__":
    obj = cleanobj()
    #找出地址字段中有span标签并连接打印
    #obj.showtag()
    #打印出字典格式
    #obj.printDict(hz)
    #更新到数据库中
    #obj.updateDb(dictaa)
    #更正部分联系方式
    #obj.updateTel()
    #更正部分星级显示
    #obj.updateStar()
