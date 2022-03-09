from selenium import webdriver
import time
from math import log, sin

import time


def calc(x: str) -> str:
    return str(log(abs(12 * sin(int(x)))))


link = 'https://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Get x and calculate f(x)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    # Paste answer in input
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # I'm the robot click
    checkbox_element = browser.find_element_by_id('robotCheckbox')
    checkbox_element.click()

    # Robots rule click
    robotsrules_radio = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsrules_radio)
    robotsrules_radio.click()

    # Submit
    button = browser.find_element_by_css_selector('[type="submit"]')
    # Scroll to submit btn
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

except AssertionError as e:
    print('Error message:', e)
finally:
    time.sleep(5)
    browser.quit()

