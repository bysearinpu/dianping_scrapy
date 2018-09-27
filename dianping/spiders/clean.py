# -*- coding: utf-8 -*
import mysql.connector
from scrapy.utils.project import get_project_settings
import re
import webbrowser

""" webbrowser.open("http://www.dianping.com/shop/6137860")
exit() """

hz=[
    "工",
"贵",
"健",
"文",
"学",
"进",
"红",
"林",
"宜",
"市",
"扬",
"川",
"温",
"浙",
"友",
"春",
"桂",
"无",
"滨",
"尔",
"义",
"汉",
"府",
"治",
"博",
"肇",
"湖",
"锦",
"体",
"九",
"汾",
"遵",
"衡",
"化",
"建",
"庆",
"中",
"昌",
"前",
"凤",
"公",
"风",
"青",
"吉",
"花",
"坊",
"生",
"云",
"河",
"八",
"人",
"淮",
"惠",
"通",
"旗",
"胜",
"波",
"爱",
"成",
"津",
"肥",
"港",
"绍",
"苏",
"重",
"徐",
"岛",
"年",
"济",
"黄",
"合",
"育",
"天",
"和",
"黑",
"台",
"庄",
"烟",
"关",
"藏",
"农",
"沙",
"蒙"
]

dictaa = {
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
'<span class=\"fa-9NXi\"></span>':u'蒙'
}

class cleanobj():

  def __init__(self):
      conf = get_project_settings()
      self.conn= mysql.connector.connect(host=conf["MYSQL_HOST"],user=conf['MYSQL_USER'],password=conf['MYSQL_PWD'],database=conf['MYSQL_DB'],charset='utf8')
      self.cur = self.conn.cursor()
      self.cur.execute("select shopId,address from shop")
      self.res = self.cur.fetchall()
      
      tag=[]
      for row in self.res:
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
         new_addr= re.sub(r'\<span class=\"([a-zA-Z0-9-]{7})\"\>\<\/span\>',th,row[1].encode("utf-8"))
         #print new_addr
         self.cur.execute("update shop set address=%s where shopId=%s",(new_addr,row[0]))
      

if __name__=="__main__":
    obj = cleanobj()
    #obj.showtag()
    #obj.printDict(hz)
    obj.updateDb(dictaa)
