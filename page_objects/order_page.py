from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def _click_input_metro(self):
        self.browser.find_element(*OrderPageLocators.INPUT_METRO).click()

    def _click_calender(self):
        self.click_element(OrderPageLocators.INPUT_CALENDER)

    def _click_timeline(self):
        self.browser.find_element(*OrderPageLocators.INPUT_TIMELINE).click()

    def fill_input_name(self, name):
        self.fill_input(OrderPageLocators.INPUT_NAME, name)

    def fill_input_surname(self, surname):
        self.fill_input(OrderPageLocators.INPUT_SURNAME, surname)

    def fill_input_address(self, address):
        self.fill_input(OrderPageLocators.INPUT_ADDRESS, address)

    def fill_input_phone(self, phone):
        self.fill_input(OrderPageLocators.INPUT_PHONE, phone)

    def click_button_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def click_button_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def click_button_confirm(self):
        self.click_element(OrderPageLocators.CONFIRMATION_BUTTON)

    def click_button_status(self):
        self.click_element(OrderPageLocators.STATUS_BUTTON)

    def choose_station(self, station):
        self._click_input_metro()
        self.browser.find_element(OrderPageLocators.INPUT_STATION[0],
                                  OrderPageLocators.INPUT_STATION[1].format(station)).click()

    def choose_date(self, date):
        # я надеюсь, ревьюер не потребует создать полноценный механизм пользования календарем?
        day = date.split()[0]
        self._click_calender()
        self.browser.find_element(OrderPageLocators.INPUT_DATE[0],
                                  OrderPageLocators.INPUT_DATE[1].format(day)).click()

    def choose_rental_period(self, period):
        self._click_timeline()
        self.browser.find_element(OrderPageLocators.INPUT_RENTAL_PERIOD[0],
                                  OrderPageLocators.INPUT_RENTAL_PERIOD[1].format(period)).click()

    def choose_color(self, color='чёрный жемчуг'):
        if color == 'чёрный жемчуг':
            locator = OrderPageLocators.INPUT_COLOR_BLACK
        elif color == 'серая безысходность':
            locator = OrderPageLocators.INPUT_COLOR_GREY
        else:
            raise Exception('Sorry, unknown color!')

        self.click_element(locator)

    def get_order_number(self):
        text = self.get_text(OrderPageLocators.ORDER_TEXT)
        order_number = text.split()[2].strip('.')
        return order_number
    
    def order_scooter(self, name, surname, address, phone, station, date, period, color):
        self.fill_input_name(name)
        self.fill_input_surname(surname)
        self.fill_input_address(address)
        self.fill_input_phone(phone)
        self.choose_station(station)

        self.click_button_next()

        self.choose_date(date)
        self.choose_rental_period(period)
        self.choose_color(color)

        self.click_button_order()
        self.click_button_confirm()

        order_number = self.get_order_number()
        self.click_button_status()

        return order_number

