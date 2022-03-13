from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest

@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_should_see_add_to_basket_btn(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page() # открываем страницу авторизации

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.should_be_empty_basket()