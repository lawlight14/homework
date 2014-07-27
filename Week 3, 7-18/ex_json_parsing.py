#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)

elem = data['data']
print "MEM_NUM   Age          Job        MEM_CODE     etc"
for item in elem:
	etc = ""
	if(item['job'] == "Programmer"):
		etc += "Master "
	if(item['age'] >= 50):
		etc += "Old"

	print "%5d %7d %15s %13d    %s" %(item['MEM_NUM'], item['age'], item['job'], item['MEM_CODE'], etc)
	