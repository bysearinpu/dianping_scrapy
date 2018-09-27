SELECT 
t1.shopName AS 店铺名,
t1.alias AS 别名,
t2.regionName AS 地区,
t2.kindName AS 行业,
t1.star AS 星级,
t1.address AS 地址,
t1.tel AS 联系方式,
t1.businessHours AS 营业时间,
t1.other AS 其他信息,
t1.shopUrl AS 店铺链接
FROM shop t1,cat t2 WHERE t1.catId=t2.catId 