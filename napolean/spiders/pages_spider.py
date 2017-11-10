# coding:utf-8


from scrapy import Selector
from scrapy.spiders import Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from napolean.Global import topic
from napolean.items import PagesItem

topic = '云南'


class PagesSpider(Spider):
	name = 'pages'
	allowed_domains = ['tieba.baidu.com']
	
	start_urls = [
		'https://tieba.baidu.com/f?ie=utf-8&kw={}&fr=search'.format(topic),
	]
	
	def parse(self, response):
		hxs = Selector(response)
		pages = hxs.xpath('//a[contains(@class, "pagination-item") and contains(@class, "last")]/@href').extract()
		
		import pdb
		pdb.set_trace()
		
		pages_item = PagesItem()
		pages_item['page_url_list'] = []
		pages_item['page_url_list'].append(self.start_urls[0])
		
		base_url = get_base_url(response)
		for one_page in pages:
			url = urljoin_rfc(base_url, one_page)
			url = url.decode("utf-8")
			pages_item['page_url_list'].append(url)
		
		return pages_item
