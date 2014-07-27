# -*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup
   

htmltext = urllib.urlopen("http://blog.naver.com/CommentList.nhn?blogId=aileen1031&logNo=130107595002&currentPage=&isMemolog=false&focusingCommentNo=&showLastPage=true&shortestContentAreaWidth=false").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for item in soup.select(".comm"):
   authors.append(item.get_text().strip()+"\n")

for author in authors:
   print author.encode('utf-8')