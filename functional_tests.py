# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:15:54 2015

@author: RMB
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title