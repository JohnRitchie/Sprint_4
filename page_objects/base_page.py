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
        self.browser.execute_script("arguments[0].click();", self.browser.find_element(*element))

    def click_button(self, button):
        self.click_element(button)

    def click_scooter_logo(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    def click_ya_logo(self):
        self.click_element(BasePageLocators.YA_LOGO)

    def fill_input(self, field, value):
        self.browser.find_element(*field).send_keys(value)
