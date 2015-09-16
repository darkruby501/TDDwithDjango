# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:15:54 2015

@author: RMB
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists.
assert 'To-do' in browser.title, "Browser title was " + browser.title

#She types "Buy peacock feathers" into a text box 

#When she hits enter, the page updates, and now the page lists
#"1: Buy peacock featuers" as an item.

#However this is a to-do list, not a to do item. She enters "Use peacock feathers
#for magic spell as another item.

#The page updates again.

#Edith wonders whether the site will remember her list. Then she sees that the site
#has generated a unique URL fo her - - there is some text to that effect.

#She visits the URL, her to-do list is still there.

#Satisfied, she returns to her homeworld.

#Coding is for whats, not whys.