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
__date__    = "07.06.2017"
__mail__    = "blackvkng@yandex.com"

try:
	__version__ = open("version", "r").read().strip()
except:
	__version__ = "0.0.1"

import os
import sys
import time

from src import crawler
from src import sqliScan
from src import reverseIp

from colorama import init, Fore, Style

colors = {
	"":        "",
	"red":     Fore.RED,
	"cyan":    Fore.CYAN,
	"blue":    Fore.BLUE,
	"green":   Fore.GREEN,
	"white":   Fore.WHITE,
	"yellow":  Fore.YELLOW,
	"magenta": Fore.MAGENTA,
	"bright":  Style.BRIGHT
}

textTypes = {"info": "[INFO] ", "err": "[ERROR] ", "": ""}

sitesFromReverse  = []
sitesFromCrawler  = []
sitesFromSqliScan = []

def logo():
	print colors["bright"] + colors["blue"] + """                                                  
             ,,                                   
             db   .M\"""bgd   .g8""8q. `7MMF'      
                 ,MI    "Y .dP'    `YM. MM        
`7M'   `MF'`7MM  `MMb.     dM'      `MM MM        
  VA   ,V    MM    `YMMNq. MM        MM MM        
   VA ,V     MM  .     `MM MM.      ,MP MM      , 
    VVV      MM  Mb     dM `Mb.    ,dP' MM     ,M 
     W     .JMML.P"Ybmmd"    `"bmmd"' .JMMmmmmMMM 
                                 MMb              
                                  `bood'                                                        

\t\t\tVersion: %s
\t\t\thttp://github.com/blackvkng
\t\t\tBlack Viking - Cyber-Warrior.org 
"""%(__version__)

def vprint(text, color="", type=""):
	''' A function to use print more impressive '''

	text =  colors['yellow'] + textTypes[type] + colors['magenta'] + "["  + time.strftime("%H:%M:%S") + "] " + colors[color] + text
	print text

def usage():
	print colors['bright'] + colors['blue'] + """
Usage: viSQL
-----------------
	$ python2 viSQL.py -t http://www.bible-history.com
	$ python2 viSQL.py --target 54.201.8.54

	$ python2 viSQL.py -h/--help
"""

def rIp(url):
	''' A function to use src/reverseIp.py '''
	
	vprint("Reverse IP lookup started", "green", "info")

	for site in reverseIp.run(url):
		vprint("  " + site, "cyan", "info") 
		sitesFromReverse.append('http://' + site)

def crawl():
	''' A function to use src/crawler.py '''

	vprint("Crawler started", "green", "info")

	for site in sitesFromReverse:
		vprint("Crawling -> " + site, "yellow", "info")

		sites = crawler.run(site)

		if type(sites) != list:
			vprint(sites, "red", "err")
			continue
		else:
			pass

		vprint("  Found %s URL to SQL scan"%(len(sites)), "cyan", "info")
		sitesFromCrawler.append((site, sites))

def sC():
	''' A function to user src/sqliScan.py '''

	vprint("SQLi scan started", "green", "info")

	for tup in sitesFromCrawler:

		if len(tup[1]) == 0:
			continue
		else:
			pass

		vprint("Site: " + tup[0], "yellow", "info")

		for url in tup[1]:
			test = sqliScan.run(url)

			if test == True:
				vprint("SQLi vuln! --> " + url, "cyan", "info")
			elif test == "exit":
				break
			else:
				pass

		print "-" * 20

def main():
	''' Main function '''

	if len(sys.argv) == 3 and sys.argv[1] in ['-t', '--target']:
		url = sys.argv[-1]

		vprint("Target Web site: " +  url, "yellow", "info")
		
		rIp(url)
		crawl()
		sC()

	else:
		usage()

if __name__ == "__main__":
	init(autoreset=True)
	logo()
	vprint("Program started", "green", "info")
	main()
	vprint("Program shutting down", "yellow", "info")
