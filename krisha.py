# -*- coding: utf-8 -*-
import scrapy


class KrishaSpider(scrapy.Spider):
    name = 'krisha'
    allowed_domains = ['krisha.kz/pro/specialist']
    start_urls = ['http://krisha.kz/pro/specialist/']

    def parse(self, response):
        pass
