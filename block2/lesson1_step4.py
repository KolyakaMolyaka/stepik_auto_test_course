from selenium import webdriver
from math import log, sin
import time

def calc(x:str) -> str:
    return str(log(abs(12*sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(calc(x))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[value="robots"]')
    radiobutton.click()

    submit_btn = browser.find_element_by_css_selector('[type="submit"]')
    submit_btn.click()

except:
    print("something was wrong!")
finally:
    time.sleep(5)
    browser.quit()