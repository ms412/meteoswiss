

import os
import time
import re
import json
import requests
from lxml import html, etree
import logging
from bs4 import BeautifulSoup

_url = 'https://www.meteoswiss.admin.ch'

_page = requests.get('https://www.meteoswiss.admin.ch/home/messwerte.html')
#soup = BeautifulSoup(_page.content, 'html.parser')
soup = BeautifulSoup(_page.content, 'lxml')
#print(soup)
#mydivs = soup.find_all("div", {"class": "measurementv3-dataview"})
#x = soup.select('.measurementv3-dataview-tmpl')
#print('x',x)
tag = soup.find('script',id="measurementv3-dataview-tmpl")
#q=mydivs.findAll("div", class_="measurementv3-dataview")
#mydivs = soup.find_all("div")
print('y',type(tag))
print('xx', tag.string)
print(tag.get_attribute_list)
ddd = BeautifulSoup(tag.string,'lxml')
#tt = ddd.'measurementv3-detailview'
x = ddd.find(re.compile("measurementv3-detailview"))
print(type(x))
print(x['data-details-json'])
#print('xxxx',x)
#data_soup.find_all(attrs={"data-foo": "value"})
#p#rint(ddd.contents,len(ddd.contents))
#for child in ddd.descendants:
 #   print('child',type(child),child)
  #  print('Child',child['data-details-json'])


