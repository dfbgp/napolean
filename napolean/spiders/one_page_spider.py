# coding:utf-8

from scrapy import Selector
from scrapy.spiders import Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from napolean.Global import page_url_list_file_name
from napolean.items import OnePageItem


class OnePageSpider(Spider):
	name = 'threads'
	allowed_domans = ['tieba.baidu.com']
	
	start_urls = []
	
	def __init__(self):
		with open(page_url_list_file_name, 'r', encoding='utf-8') as f:
			for line in f.readlines():
				self.start_urls.append(line)
	
	def parse(self, response):
		hxs = Selector(response)
		
		base_url = get_base_url(response)
		one_page_item = OnePageItem()
		one_page_item['thread_url_list'] = []
		
		threads = hxs.xpath('//a[contains(@class, "j_th_tit")]/@href').extract()
		for one_thread in threads:
			url = urljoin_rfc(base_url, one_thread)
			url = url.decode("utf-8")
			one_page_item['thread_url_list'].append(url)
		
		return one_page_item
