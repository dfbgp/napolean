# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from napolean.Global import page_url_list_file_name
from napolean.Global import thread_text_file_name
from napolean.Global import thread_url_list_file_name
from napolean.items import OnePageItem
from napolean.items import OneThreadItem
from napolean.items import PagesItem


class NapoleanPipeline(object):
	def process_item(self, item, spider):
		
		if isinstance(item, PagesItem):
			with open(page_url_list_file_name, 'a+', encoding='utf-8') as f:
				buffer = ''
				page_url_list = item['page_url_list']
				for one_url in page_url_list:
					buffer += one_url
					buffer += '\n'
				
				f.write(buffer)
				pass
		
		elif isinstance(item, OnePageItem):
			with open(thread_url_list_file_name, 'a+', encoding='utf-8') as f:
				thread_url_list = item['thread_url_list']
				buffer = ''
				for one_url in thread_url_list:
					if one_url.strip():
						buffer += '{}\n'.format(one_url)
				
				f.write(buffer)
				pass
		
		elif isinstance(item, OneThreadItem):
			with open(thread_text_file_name, 'a+', encoding='utf-8') as f:
				text = item['thread_text']
				text = '{}\n'.format(text)
				f.write(text)
				print(text)
				pass
		else:
			pass
		
		return item
