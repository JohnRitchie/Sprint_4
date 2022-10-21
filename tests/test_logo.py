import time

from helpers import open_main_page, open_order_page
from links import MAIN_PAGE_LINK, YA_PAGE_LINK


def test_logo_click_scooter_logo_from_main_page_open_main_page(browser):
    main_page = open_main_page(browser)

    main_page.click_scooter_logo()
    assert browser.current_url == MAIN_PAGE_LINK, 'Main page is not open!'


def test_logo_click_scooter_logo_from_order_page_open_main_page(browser):
    order_page = open_order_page(browser)

    order_page.click_scooter_logo()
    assert browser.current_url == MAIN_PAGE_LINK, 'Main page is not open!'


def test_logo_click_ya_logo_from_main_page_open_ya_page(browser):
    main_page = open_main_page(browser)

    main_page.click_ya_logo()
    browser.switch_to.window(browser.window_handles[1])

    # неявное ожидание уже используется в conftest, а для явного не хочется вводить новые локаторы нового сайта
    time.sleep(10)

    assert browser.current_url == YA_PAGE_LINK, 'Ya page is not open!'


def test_logo_click_ya_logo_from_order_page_open_ya_page(browser):
    order_page = open_order_page(browser)

    order_page.click_ya_logo()
    browser.switch_to.window(browser.window_handles[1])

    # неявное ожидание уже используется в conftest, а для явного не хочется вводить новые локаторы нового сайта
    time.sleep(10)

    assert browser.current_url == YA_PAGE_LINK, 'Ya page is not open!'
