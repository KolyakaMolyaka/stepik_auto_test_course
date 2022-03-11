from selenium.webdriver.common.by import  By

def test_add_to_button_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button is not None

