from page_objects.main_page import MainPage
from links import MAIN_PAGE_LINK, ORDER_PAGE_LINK


def test_order_button_click_order_button_up_open_order_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_order_button_up()
    assert browser.current_url == ORDER_PAGE_LINK, 'Order page is not open!'


def test_order_button_click_order_button_down_open_order_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_order_button_down()
    assert browser.current_url == ORDER_PAGE_LINK, 'Order page is not open!'
