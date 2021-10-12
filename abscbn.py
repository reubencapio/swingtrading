from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spiders import BaseSpider
import scrapy
from bs4 import BeautifulSoup
import urllib
import re
import sys 
sys.path.append('D:\downloads\depot_tools\depot_tools\python276_bin\Lib\site-packages')
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import html2text


class someSpider(CrawlSpider):
	name = 'abs'
	allowed_domains = ['news.abs-cbn.com']
	start_urls = ['http://news.abs-cbn.com/business']
	
	rules = (Rule (LinkExtractor(allow=r'business/'), callback="parse_obj", follow=True),)

	def parse_obj(self, response):
		print "respone.url == " + response.url
		filename = response.url	
		filename = re.sub(r'[\W_]+', '', filename)
		filename = filename.translate(None, ':/') + '.txt'
		filename = 'C:/Users/FPT Software/scraper/tutorial/tutorial/spiders/abscbn_output/' + filename;
		#print "filename == " + filename	
		soup = BeautifulSoup(response.body, "html5lib")
		text = [p.get_text() for p in soup.find_all('p')]
		output = ''.join(text)
		output = output.strip()
		if re.match(r'^\s*$', output):
			print "blankpage"
		else:
			with open(filename, 'wb') as f:
				f.write(output.encode('utf-8'))