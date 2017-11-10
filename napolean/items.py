# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NapoleanItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class PagesItem(scrapy.Item):
	page_url_list = scrapy.Field()


class OnePageItem(scrapy.Item):
	thread_url_list = scrapy.Field()


class OneThreadItem(scrapy.Item):
	thread_text = scrapy.Field()
