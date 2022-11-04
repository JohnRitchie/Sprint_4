from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')
    ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRMATION_BUTTON = (By.XPATH, './/button[text()="Да"]')
    STATUS_BUTTON = (By.XPATH, './/button[text()="Посмотреть статус"]')

    INPUT_NAME = (By.XPATH, './/input[@placeholder="* Имя"]')
    INPUT_SURNAME = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_METRO = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    INPUT_STATION = (By.XPATH, './/div[text()="{}"]')
    INPUT_PHONE = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    INPUT_CALENDER = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    INPUT_DATE = (By.CLASS_NAME, 'react-datepicker__day--0{}')
    INPUT_TIMELINE = (By.CLASS_NAME, 'Dropdown-placeholder')
    INPUT_RENTAL_PERIOD = (By.XPATH, './/div[text()="{}"]')
    INPUT_COLOR_BLACK = (By.ID, 'black')
    INPUT_COLOR_GREY = (By.ID, 'grey')

    ORDER_TEXT = (By.CLASS_NAME, 'Order_Text__2broi')
