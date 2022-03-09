from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from math import log, sin

link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # в течении 12 секунд ждём пока цена дома не станет равна 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    # кликаем по кнопке, когда цена = 100$
    browser.find_element(By.ID, 'book').click()

    # Get x and calculate f(x)
    x = browser.find_element_by_id('input_value').text
    y = str(log(abs(12 * sin(int(x)))))

    # Paste answer in input
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(y)

    # submit task
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()