import scrapy

class BookSpider(scrapy.Spider):
    name = 'qidian'
    def start_requests(self):
        for i in range(1,2):

            url='https://www.qidian.com/rank/hotsales?page=2'

            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response, **kwargs):
        chen=response.text
        print(chen)