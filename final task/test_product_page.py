from pages.product_page import ProductPage
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

