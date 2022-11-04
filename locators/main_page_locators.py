from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    ORDER_BUTTON_UP = (By.XPATH, './/button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_DOWN = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')

    NOT_HIDDEN_FAQ_ITEM_PANEL = (By.XPATH, './/div[@class="accordion__panel" and not(@hidden)]')

    FIRST_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-0')
    FIRST_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-0"]/p')

    SECOND_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-1')
    SECOND_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-1"]/p')

    THIRD_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-2')
    THIRD_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-2"]/p')

    FOURTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-3')
    FOURTH_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-3"]/p')

    FIFTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-4')
    FIFTH_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-4"]/p')

    SIXTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-5')
    SIXTH_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-5"]/p')

    SEVENTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-6')
    SEVENTH_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-6"]/p')

    EIGHTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-7')
    EIGHTH_FAQ_ITEM_PANEL = (By.XPATH, './/div[@id="accordion__panel-7"]/p')
