from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from links import MAIN_PAGE_LINK, ORDER_PAGE_LINK, YA_PAGE_LINK


def test_logo_click_scooter_logo_from_main_page_open_main_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_scooter_logo()
    assert browser.current_url == MAIN_PAGE_LINK, 'Main page is not open!'


def test_logo_click_scooter_logo_from_order_page_open_main_page(browser):
    order_page = OrderPage(browser, ORDER_PAGE_LINK)
    order_page.open()

    order_page.click_scooter_logo()
    assert browser.current_url == MAIN_PAGE_LINK, 'Main page is not open!'


def test_logo_click_ya_logo_from_main_page_open_ya_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.open_ya_page()
    assert browser.current_url == YA_PAGE_LINK, 'Ya page is not open!'


def test_logo_click_ya_logo_from_order_page_open_ya_page(browser):
    order_page = OrderPage(browser, ORDER_PAGE_LINK)
    order_page.open()

    order_page.open_ya_page()
    assert browser.current_url == YA_PAGE_LINK, 'Ya page is not open!'
