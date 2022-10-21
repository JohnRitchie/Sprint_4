from helpers import open_main_page
from links import ORDER_PAGE_LINK


def test_order_button_click_order_button_up_open_order_page(browser):
    main_page = open_main_page(browser)

    main_page.click_order_button_up()
    assert browser.current_url == ORDER_PAGE_LINK, 'Order page is not open!'


def test_order_button_click_order_button_down_open_order_page(browser):
    main_page = open_main_page(browser)

    main_page.click_order_button_down()
    assert browser.current_url == ORDER_PAGE_LINK, 'Order page is not open!'
