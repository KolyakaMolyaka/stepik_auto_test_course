from selenium import webdriver
from math import log, sin
import time

def calc(x:str) -> str:
    return str(log(abs(12*sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    radio_btn = browser.find_element_by_id('peopleRule')

    people_checked = radio_btn.get_attribute('checked')
    print('value of people radio: ', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'

    robots_radio = browser.find_element_by_id('robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots radio: ', robots_checked)
    assert robots_checked is not None, 'Robots radio is not selected by default'
except AssertionError as e:
    print('Error message:', e)
finally:
    time.sleep(5)
    browser.quit()