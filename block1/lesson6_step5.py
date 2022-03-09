from selenium import webdriver
import time
from math import ceil, pow, pi, e

link = 'http://suninjuly.github.io/find_link_text'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	f_link = browser.find_element_by_link_text(str(ceil(pow(pi, e)*10000)))
	f_link.click()

	input1 = browser.find_element_by_tag_name('input')
	input1.send_keys('Nikolay')

	input2 = browser.find_element_by_name('last_name')
	input2.send_keys('Markeev')

	input3 = browser.find_element_by_class_name('city')
	input3.send_keys('Lipeck')

	input4 = browser.find_element_by_id('country')
	input4.send_keys('Russia')

	button = browser.find_element_by_css_selector('button.btn')
	button.click()
finally:
	time.sleep(30)
	browser.quit()