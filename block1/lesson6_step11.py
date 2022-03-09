# -*- coding: utf-8 -*-
from selenium import webdriver
import time

try: 
	link = "http://suninjuly.github.io/registration1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_xpath('//input[text()="First name*",required]')
	input2 = browser.find_element_by_xpath('//input[text()="Last name*",required]')
	input3 = browser.find_element_by_xpath('//input[text()="Email*",required]')

	input1.send_keys('SECRET')
	input2.send_keys('SECRET')
	input3.send_keys('SECRET')

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	time.sleep(1)

	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text

	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	time.sleep(5)
	browser.quit()