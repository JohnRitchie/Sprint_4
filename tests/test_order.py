from helpers import open_order_page
from links import STATUS_PAGE_LINK


def test_order_order_with_one_method_success(browser):
    order_page = open_order_page(browser)
    order_number = order_page.order_scooter('Петр', 'Петров', 'Москва, Кирова 2, кв. 2', '+79876543210',
                                            'Охотный Ряд', '30 число этого месяца', 'трое суток', 'серая безысходность')

    assert browser.current_url == STATUS_PAGE_LINK.format(order_number), 'Status page is not open!'


def test_order_order_with_all_methods_success(browser):
    order_page = open_order_page(browser)
    order_page.fill_input_name('Иван')
    order_page.fill_input_surname('Иванов')
    order_page.fill_input_address('Москва, Ленина 1, кв. 1')
    order_page.fill_input_phone('+70123456789')
    order_page.choose_station('Сокольники')

    order_page.click_button_next()

    order_page.choose_date('10 число этого месяца')
    order_page.choose_rental_period('пятеро суток')
    order_page.choose_color('чёрный жемчуг')

    order_page.click_button_order()
    order_page.click_button_confirm()

    order_number = order_page.get_order_number()
    order_page.click_button_status()

    assert browser.current_url == STATUS_PAGE_LINK.format(order_number), 'Status page is not open!'

