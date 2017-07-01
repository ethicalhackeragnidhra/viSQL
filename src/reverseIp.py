#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#


""" 
Cyber Warrior Ar-Ge Training adına geliştirmiş hedef 
site ve sunucudaki sitelerde SQL Injection açığı
arama aracı.
"""

__author__  = "Black Viking"
__version__ = "0.0.1"

__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

import re
import requests
import urlparse

def run(url):
	if urlparse.urlparse(url).netloc == '':
		url = urlparse.urlparse(url).path
	else:
		url = urlparse.urlparse(url).netloc

	return re.findall("<td>(.*?)</td>", requests.get("http://viewdns.info/reverseip/?host=%s&t=1"%(url)).text)[3:]
