# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RoomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name =scrapy.Field()            #房间标题
    address=scrapy.Field()          #房间地址
    type =scrapy.Field()            #房间户型
    area=scrapy.Field()             #房间建筑面积
    inner_area=scrapy.Field()       #房间内面积
    direction=scrapy.Field()        #房间朝向
    fitment=scrapy.Field()         #装修情况
    elevator=scrapy.Field()         #房间有无电梯
    total_price=scrapy.Field()      # 房间总价
    unit_price=scrapy.Field()       #房间单价
    pro=scrapy.Field()              #产权信息
    attention=scrapy.Field()        #多少人关注
    issue=scrapy.Field()            #发布时间
    message=scrapy.Field()          #详细信息
    floor=scrapy.Field()            #楼层数
    family_structure=scrapy.Field() #户型结构
    architectural_structure=scrapy.Field()  #建筑结构
    Ladder_household_proportion=scrapy.Field()  #梯户比例

