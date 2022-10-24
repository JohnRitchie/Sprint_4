from page_objects.order_page import OrderPage
from links import ORDER_PAGE_LINK, STATUS_PAGE_LINK


def test_order_order_with_first_right_dataset_success(browser):
    order_page = OrderPage(browser, ORDER_PAGE_LINK)
    order_page.open()

    order_number = order_page.order_scooter('Петр', 'Петров', 'Москва, Кирова 2, кв. 2', '+79876543210',
                                            'Охотный Ряд', '30 число этого месяца', 'трое суток', 'серая безысходность')

    assert browser.current_url == STATUS_PAGE_LINK.format(order_number), 'Status page is not open!'


def test_order_order_with_second_right_dataset_success(browser):
    order_page = OrderPage(browser, ORDER_PAGE_LINK)
    order_page.open()

    order_number = order_page.order_scooter('Иван', 'Иванов', 'Москва, Ленина 1, кв. 1', '+70123456789',
                                            'Сокольники', '10 число этого месяца', 'пятеро суток', 'чёрный жемчуг')

    assert browser.current_url == STATUS_PAGE_LINK.format(order_number), 'Status page is not open!'
