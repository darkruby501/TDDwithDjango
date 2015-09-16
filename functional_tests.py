# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:15:54 2015

@author: RMB
"""

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self): #
        self.browser = webdriver.Firefox()
        
    def tearDown(self): #
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        
        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title) #
        self.fail('Finish the test!')
        
        # She is invited to enter a to-do item straigtht away
        
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
    
if __name__ == '__main__': #
    unittest.main(warnings='ignore') #    
    
    
    
    
    
    