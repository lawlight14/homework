#-*- coding: utf-8 -*-
# JTBC 뉴스 속보 xml문서 파싱하기

import urllib
import webbrowser
from xml.etree.ElementTree import parse

class NewsRSS(object):
	def __init__(self, no, name, URL):
		self.no = no
		self.name = name
		self.URL = URL

	def getNo(self):
		return self.no

	def getName(self):
		return self.name

	def getURL(self):
		return self.URL


while(True):
	kindList = [
		NewsRSS(1, "Jtbc", "http://fs.jtbc.joins.com/RSS/newsflash.xml"),
		NewsRSS(2, "중앙", "http://rss.joins.com/joins_homenews_list.xml"),
		NewsRSS(3, "조선", "http://www.chosun.com/site/data/rss/rss.xml"),
		NewsRSS(4, "동아", "http://rss.donga.com/total.xml"),
		NewsRSS(5, "헤럴드경제", "http://biz.heraldm.com/rss/010000000000.xml")
	]

	for item in kindList:
		print item.getNo(), ":", item.getName()
	print

	selectedKind = int(raw_input("원하시는 신문사를 선택하세요(종료는 6번) : "))
	if(selectedKind == 6):
		break
	elif(1 > selectedKind or selectedKind > 5):
		print "잘못 입력했습니다."
		continue

	selectedKind -= 1

	print
	xml = urllib.urlopen(kindList[selectedKind].getURL())

	tree = parse(xml)	
	root = tree.getroot()

	newsdict = {}

	line = 1
	for parent in root.getiterator():
		for child in parent.findall("item"):
			newsdict[line] = child
			print line, child.find("title").text
			line += 1

	print

	select = int(raw_input("보고 싶은 뉴스 번호를 입력하세요: "))
	sel_title = newsdict[select].find("title").text
	sel_link = newsdict[select].find("link").text

	print sel_title
	print sel_link
	print
	
	webbrowser.open(sel_link)