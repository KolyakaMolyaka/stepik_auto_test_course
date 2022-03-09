from selenium import webdriver
from math import log,sin

def calc(x: str) -> str:
    return str(log(abs(12 * sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # click button to open modal window
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()


    # switch to the new tab, which was opened after click on button
    second_window = browser.switch_to.window(browser.window_handles[1])

    # Get x and calculate f(x)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    # Paste answer in input
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # submit task
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()


except AssertionError as e:
    print('Error message:', e)
finally:
    print(browser.switch_to.alert.text)
    browser.quit()

