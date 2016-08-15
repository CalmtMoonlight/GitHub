#coding:utf8
from gome.items import NewsItem
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector


class GomeSpider(CrawlSpider):


    name = "gome_spider"
    start_urls = [
        'http://www.sina.com/',

    ]

    def parse(self, response):

        print response.body
        item = NewsItem()

        selector = Selector(response)
        item['html'] = response.body
        item['link'] = response.url

        print response.url

        print response.body

        return item

