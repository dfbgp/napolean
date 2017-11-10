# -*- coding: utf-8 -*-
# encoding=utf-8

from scrapy import Selector
from scrapy.spiders import Spider

from napolean.Global import thread_url_list_file_name
from napolean.items import OneThreadItem


class OneThreadSpider(Spider):
	name = 'posts'
	allowed_domans = ['tieba.baidu.com']
	
	start_urls = []
	
	def __init__(self):
		with open(thread_url_list_file_name, 'r', encoding='utf-8') as f:
			for line in f.readlines():
				self.start_urls.append(line)
	
	def parse(self, response):
		hxs = Selector(response)
		
		buffer = ''

		title_tokens = hxs.xpath('//div[contains(@class, "core_title")]//text()').extract()
		
		for token in title_tokens:
			token = token.strip()
			if token:
				buffer += '{};'.format(token)
		
		text_data_list = hxs.xpath('//div[contains(@class, "d_post_content_main")]//text()').extract()
		for text in text_data_list:
			text = text.strip()
			if text:
				buffer += '{};'.format(text)
		
		one_thread_item = OneThreadItem()
		one_thread_item['thread_text'] = buffer
		
		return one_thread_item
