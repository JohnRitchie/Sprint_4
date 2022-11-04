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

    def is_element_present(self, element, timeout=25):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located(element))
        except TimeoutException:
            return False
        return True

    def click_element(self, element):
        element = self.browser.find_element(*element)
        # уважаемый ревьюер, клик сделан так, чтобы избежать ошибки ElementClickInterceptedError
        # с такой реализацией я эту ошибку не получаю, с любой другой, что я нашел - получаю
        # если вы знаете, как эту ошибку обойти иначе, напишите, пожалуйста об этом в реью
        self.browser.execute_script("arguments[0].click();", element)

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

    def get_text(self, element):
        # ответ в faq открывается не сразу
        self.browser.implicitly_wait(50)
        return self.browser.find_element(*element).text
