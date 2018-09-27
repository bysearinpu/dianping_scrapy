




TRUNCATE TABLE shop
SELECT * FROM cat WHERE kindName='服装' AND catId NOT IN(102,128)

UPDATE shop SET catId=128 WHERE catId=1

SELECT * FROM shop WHERE shopName LIKE '%遇见%'

DELETE FROM shop WHERE catId IN (SELECT catId FROM cat WHERE kindName='母婴购物' )

SELECT * FROM shop WHERE catId IN (SELECT catId FROM cat WHERE kindName='数码产品' ) LIMIT 10000

SELECT COUNT(1) FROM shop WHERE catId IN (213)

SELECT * FROM shop WHERE address IS NULL

SELECT 
t1.shopName AS 店铺名,
t1.alias AS 别名,
CONCAT_WS(' ',t1.district,t2.regionName) AS 地区,
t2.kindName AS 行业,
t1.star AS 星级,
t1.address AS 地址,
t1.tel AS 联系方式,
t1.businessHours AS 营业时间,
t1.other AS 其他信息,
t1.shopUrl AS 店铺链接 
FROM shop t1,cat t2 WHERE t1.catId=t2.catId LIMIT  100000
 
SELECT t1.shopName ,t1.shopId,t2.shopId ,t1.address,t2.address,t1.catId,t2.catId FROM shop t1,shop t2 WHERE t1.shopName=t2.shopName AND t1.address=t2.address AND t1.shopId<>t2.shopId

SELECT t1.*,t2.kindName FROM shop t1,cat t2 WHERE t1.catId=t2.catId LIMIT 100000

DELETE FROM shop WHERE catId IN(88,89,90,63,64)

SELECT SUM(pageCount)*15 FROM cat  WHERE catId IN(73,97,98,99)

SELECT * FROM cat WHERE kindName ='母婴购物'

SELECT t1.* FROM shop t1,cat t2 WHERE t1.catId=t2.catId AND t2.kindName='母婴购物' LIMIT 100000  AND t2.catId NOT IN(257,225,151) 
SELECT SUM(pageCount)*15 FROM cat WHERE kindName='母婴购物' AND catId NOT IN(257,225,151)

SELECT SUM(pageCount)*15 FROM cat WHERE  catId  IN(49,51,53,70,71)

SELECT * FROM shop WHERE catId IN (73,97,98,99) LIMIT 10000 (SELECT catId FROM cat WHERE kindName='其他服饰鞋包' )

SELECT * FROM cat WHERE kindName='珠宝饰品'  AND catId NOT IN(257,225,151)

SELECT COUNT(1) FROM shop

SELECT shopId,address,tel FROM shop LIMIT 1000000








