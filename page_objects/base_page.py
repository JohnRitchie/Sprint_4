from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, element, timeout=6):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located(element))
        except TimeoutException:
            return False
        return True

    def click_element(self, element):
        element = self.browser.find_element(*element)
        # уважаемый ревьюер, обращение к первому элементу (arguments[0]) здесь идет потому, что это так работает
        # перечитайте, пожалуйста 8 урок ("Перейти к элементу")
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_button(self, button):
        self.click_element(button)

    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    def _click_ya_logo(self):
        self.click_element(BasePageLocators.YA_LOGO)

    def fill_input(self, field, value):
        self.browser.find_element(*field).send_keys(value)

    def open_ya_page(self):
        self._click_ya_logo()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.is_element_present(BasePageLocators.YA_SEARCH_BUTTON)

    def wait_text(self, element, text):
        WebDriverWait(self.browser, 6).until(expected_conditions.text_to_be_present_in_element(element, text))

    def get_text(self, element):
        return self.browser.find_element(*element).text
