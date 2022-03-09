from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # paste name
    name_input = browser.find_element_by_name('firstname')
    name_input.send_keys("Nikolay")

    # paste last name
    lastname_input = browser.find_element_by_name('lastname')
    lastname_input.send_keys("Markeev")

    # paste email
    email_input = browser.find_element_by_name('email')
    email_input.send_keys("pro100email@mail.ru")

    # paste file
    file_input = browser.find_element_by_name('file')

    filedir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(filedir, 'log.txt')
    file_input = file_input.send_keys(filepath)

    # submit actions
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

except AssertionError as e:
    print('Error message:', e)
finally:
    time.sleep(5)
    browser.quit()

