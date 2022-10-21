from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from links import MAIN_PAGE_LINK, ORDER_PAGE_LINK


def open_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    assert page.is_faq_section_present(), 'FAQ section is not presented!'

    return page


def open_order_page(browser):
    page = OrderPage(browser, ORDER_PAGE_LINK)
    page.open()
    assert page.is_next_button_present(), 'Next button is not presented!'

    return page
