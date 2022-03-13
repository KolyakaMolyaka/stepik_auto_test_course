from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_product_btn = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET)
        add_product_btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_same_titles()
        self.should_be_same_prices()

    def should_be_same_titles(self):
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        got = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_TITLE).text
        assert expected == got, f'Book title and book in basket title are different: expected {expected}, got {got}'

    def should_be_same_prices(self):
        expected = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        got = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text
        assert expected == got, f'Book price and book price in basket are different: expected {expected}, got {got}'

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BASKET), 'Add product to basket is not presented'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            'Success message is presented'