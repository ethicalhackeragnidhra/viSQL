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

import urllib2

sql_errors = {
			 "error in your SQL syntax": 'SQL syntax error',
			 "Query failed": 'Query failed',
			 "supplied argument is not a valid MySQL result resource in": 'Bad argument',
			 "Microsoft JET Database Engine error '80040e14'": 'JET DBE error',
			 "Error:unknown": 'Unknown error',
			 "Fatal error": 'Fatal error',
			 "mysql_fetch": 'MySQL fetch',
			 "Syntax error": 'Syntax error'
			}

def run(url):
	global source
	
	source = ""

	try:
		source = urllib2.urlopen(url+"'", timeout=5).read()
	except KeyboardInterrupt:
		return "exit"

	except:
		pass

	for error in sql_errors:
		if error in source:
			return True
		else: 
			pass

	return False
