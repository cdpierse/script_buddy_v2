from __future__ import absolute_import

import string

import scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, Spider

from ..items import ImsdbScraperItem

# from fight_scraper.items import FightScraperItem

class Scripts(Spider):
    name = "scriptSpider"
    BASE_URL = 'http://www.imsdb.com/'

    def start_requests(self):
        url = 'http://www.imsdb.com/all%20scripts/' 
        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath("//td//p//a/@href").extract()
        print(links)
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_script_link)

    def parse_script_link(self, response):
        
        imsdb_item = ImsdbScraperItem()
        script_link = response.xpath("//table[@class = 'script-details']//tr//td/a").extract()
        print(script_link)
        # print(sel.xpath("//a/text()").extract())
        

   



