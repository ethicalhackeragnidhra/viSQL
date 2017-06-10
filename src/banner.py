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


import os

banner_nix = """
                          
"""

banner_win = """
        _ _____ ____    __       ______            __
 _   __(_) ___// __ \  / /      /_  __/___  ____  / /
| | / / /\__ \/ / / / / /        / / / __ \/ __ \/ / 
| |/ / /___/ / /_/ / / /___     / / / /_/ / /_/ / /  
|___/_//____/\___\_\/_____/    /_/  \____/\____/_/                                                  

					Version: %s
					http://github.com/blackvkng
					Black Viking - Cyber-Warrior.org

"""%(__version__)

if os.name == "nt":
	banner = banner_win
else:
	banner = banner_nix

