from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time


link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link2)

    # Get operands
    lhv = int(browser.find_element_by_id('num1').text)
    rhv = int(browser.find_element_by_id('num2').text)

    # Select answer
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(lhv + rhv))
    # alternative: select_by_visible_text(str(sum(lhv, rhv)))

    # Submit exercise
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

except AssertionError as e:
    print('Error message:', e)
finally:
    time.sleep(5)
    browser.quit()