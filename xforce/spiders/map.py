# -*- coding: utf-8 -*-
import scrapy


class MapSpider(scrapy.Spider):
    name = 'map'
    allowed_domains = ['https://exchange.xforce.ibmcloud.com']
    start_urls = ['http://https://exchange.xforce.ibmcloud.com/']

    def parse(self, response):
        pass
