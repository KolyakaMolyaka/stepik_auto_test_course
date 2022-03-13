from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTATION_FROM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_TITLE = (By.TAG_NAME, 'h1')
    PRODUCT_IN_BASKET_TITLE = (By.CSS_SELECTOR, '.alertinner strong')  # product should be first with alertinner
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
