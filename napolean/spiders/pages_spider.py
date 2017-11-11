# coding:utf-8


from scrapy import Selector
from scrapy.spiders import Spider

from napolean.Global import topic
from napolean.items import PagesItem


class PagesSpider(Spider):
	name = 'pages'
	allowed_domains = ['tieba.baidu.com']
	
	start_urls = [
		'https://tieba.baidu.com/f?ie=utf-8&kw={}&fr=search'.format(topic),
	]
	
	def parse(self, response):
		hxs = Selector(response)
		last_page_number_str = hxs.xpath(
				'//a[contains(@class, "pagination-item") and contains(@class, "last")]/@href'
		).extract()[0]
		last_page_number = int(last_page_number_str.split('=')[-1])
		
		pages_item = PagesItem()
		pages_item['page_url_list'] = []
		pages_item['page_url_list'].append(self.start_urls[0])
		
		# for page_number in range(50, last_page_number, 50):
		# 	url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(topic, page_number)
		# 	pages_item['page_url_list'].append(url)
		
		return pages_item
