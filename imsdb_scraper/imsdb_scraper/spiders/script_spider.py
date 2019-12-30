from __future__ import absolute_import

import re
import string
from html.parser import HTMLParser

import scrapy
from bs4 import BeautifulSoup
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, Spider

from ..items import ImsdbScraperItem

class Scripts(Spider):
    name = "scriptSpider"
    BASE_URL = 'http://www.imsdb.com/'


    def start_requests(self):
        url = 'http://www.imsdb.com/all%20scripts/' 
        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        imsdb_item  = ImsdbScraperItem()
        links = response.xpath("//td//p//a/@href").extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            request = scrapy.Request(absolute_url,callback=self.parse_script_link)
            request.meta['item'] = imsdb_item
            yield request

    def parse_script_link(self, response):
        
        # link to script html is the last in the list
        imsdb_item = response.meta['item']
        script_data = response.xpath('//table[@class = "script-details"]//tr//a/@href').extract()
        script_link = script_data.pop(-1)
        genre = []
        for info in script_data:
            if '/genre/' in info:
                genre.append(info.replace('/genre/',''))
        absolute_url = self.BASE_URL + script_link


        request = scrapy.Request(absolute_url,callback=self.parse_script_html)
        request.meta['item'] = imsdb_item

        yield request
    
    def parse_script_html(self,response):
        imsdb_item = response.meta['item']
        imsdb_item['source_url'] = response.url
        imsdb_item['title'] = response.xpath('//table//tr//table[@class = "body"]//h1/text()').extract()[0]
        a_tags = response.css('.scrtext > table:nth-child(3) a ').extract()
        parser =  HTMLParser()
        genre = []
        for tag in a_tags:
            if '/genre/' in tag:
                soup = BeautifulSoup(tag, 'html.parser')
                genre.append(soup.getText('a'))
        imsdb_item['genre'] = genre
           

        imsdb_item['script_text'] = response.xpath('//table//tr//pre').extract()

        yield imsdb_item
