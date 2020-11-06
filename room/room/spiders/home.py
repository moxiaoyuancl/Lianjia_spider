import re
from os.path import join

import scrapy
from room.items import RoomItem


class HomeSpider(scrapy.Spider):
    name = 'home'

    allowed_domains = ['su.lianjia.com']

    start_urls = ['http://su.lianjia.com/']
    def start_requests(self):
        for i in range(1, 2):
            url = 'https://su.lianjia.com/ershoufang/pg{}/'.format(str(i))
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        selector_list = response.xpath('//ul[@class="sellListContent"]/li')
        for selector in selector_list:
            item = RoomItem()
            item['name'] = selector.xpath('//div[@class="title"]/a/text()').extract()[0]  # 房间标题
            addres1=selector.xpath('//div[@class="positionInfo"]/a[1]/text()').extract()[0]
            addres2=selector.xpath('//div[@class="positionInfo"]/a[2]/text()').extract()[0]
            item['address'] = addres1+addres2  # 房间地址
            item['total_price'] = selector.xpath('//div[@class="totalPrice"]/span/text()').extract()[0]  # 房屋总价
            item['unit_price'] = selector.xpath('//div[@class="unitPrice"]/span/text()').extract()[0]  # 房屋单价
            attention =(selector.xpath('//div[@class="followInfo"]/text()').extract()[0]).split('/')

            item['attention']=attention[0]     #多少人关注
            item['issue'] =attention[1]        #发布时间
            messages=selector.xpath('//div[@class="tag"]').extract()[0]
            # print(messages)
            # print(messages)
            # item['message'] = re.findall(messages, '[\u4e00-\u9fa5]+')[0]


            a=re.findall('[\u4e00-\u9fa5]+|\w+[\u4e00-\u9fa5]+',messages)



            # item['message']=a[0]
            # print(a)

            item['message']=''.join(a)


            next_urls = selector.xpath('//a[@class="noresultRecommend img LOGCLICKDATA"]/@href').extract()
            print(next_urls,'-------------------------------------------------------')
        for next_url in next_urls:
            yield scrapy.Request(url=next_url, callback=self.parse2, meta={'items':item})

    def parse2(self, response):
        item = response.meta['items']
        print(item)
        selector_list_two = response.xpath('//div[@class="base"]/div[@class="content"]')  # 基本属性
        for selector_two in selector_list_two:
            item['type'] = selector_two.xpath('ul/li[1]/text()').extract()[0]  # 房屋户型
            item['floor'] = selector_two.xpath('ul/li[2]/text()').extract()[0]  # 楼层数
            item['area'] = selector_two.xpath('ul/li[3]/text()').extract()[0]  # 建筑面积
            item['inner_area'] = selector_two.xpath('ul/li[5]/text()').extract()[0]  # 套内面积
            item['family_structure'] = selector_two.xpath('ul/li[6]/text()').extract()[0]  # 户型楼层
            item['direction'] = selector_two.xpath('ul/li[7]/text()').extract()[0]  # 房型朝向
            item['architectural_structure'] = selector_two.xpath('ul/li[8]/text()').extract()[0]  # 建筑结构
            item['fitment'] = selector_two.xpath('ul/li[9]/text()').extract()[0]  # 装修情况
            item['Ladder_household_proportion'] = selector_two.xpath('ul/li[10]/text()').extract()[0]  # 梯户比例
            item['Ladder_household_proportion'] = selector_two.xpath('ul/li[10]/text()').extract()[0]  # 梯户比例
            item['elevator'] = selector_two.xpath('ul/li[11]/text()').extract()[0]  # 有无电梯
            yield item
