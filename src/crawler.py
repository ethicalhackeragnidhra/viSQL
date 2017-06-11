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


def parameterControl(url):
	
    for site in sites:
        if url.split("=")[0] in site:
            return False

    return True

def run(startUrl):

    global sites

    sites = []
    
    try:
        html = requests.get(startUrl, timeout=3)
    except:
        return "Connection error!"

    test = html.url.split("/")
    if len(test) >= 4:
    	baseUrl = 'http://' + '/'.join(test[2:-1]) + '/'
    else:
    	baseUrl = html.url.rstrip("/") + "/"
    
    for url in re.findall('<a href="(.*?)"', html.text):
        if ".php?" in url:
            if url != "/":
                if url not in sites:
                    if parameterControl(url):
                        if baseUrl not in url:
                            url = baseUrl + url.lstrip("/")
                            sites.append(url)
                    	
                        else:
                    	    sites.append(url)

    return sites
