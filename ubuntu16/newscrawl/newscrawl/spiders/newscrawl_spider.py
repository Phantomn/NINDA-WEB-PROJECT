# -*- coding: utf-8 -*-
import scrapy
import sys
from newscrawl.items import NewscrawlItem
from scrapy.selector import HtmlXPathSelector
from scrapy import Request
from urllib.parse import urljoin, quote

class NewscrawlSpider(scrapy.Spider):
	name = "newscrawl"

	def __init__(self, page=1, keyword=None, *args, **kwargs):
		super(NewscrawlSpider, self).__init__(*args, **kwargs)
		self.start_urls = ["http://www.boannews.com/search/news_list.asp?Page=%s&search=media&find=%s" %(page, quote(keyword, encoding='euc-kr'))]

	def start_requests(self):
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		for url in self.start_urls:
			yield Request(url, headers=headers)

	def parse(self, response):
		item = NewscrawlItem()
		response.selector.remove_namespaces()
		for sel in response.xpath('//div[@id="media"]/table[2]//table//tr/td/a[1]'):
			item['title'] = sel.select('span/text()').extract()
			link = urljoin("http://www.boannews.com" , sel.select('@href').extract()[0])
			item['link'] = link
			yield item