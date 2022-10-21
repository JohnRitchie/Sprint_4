from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    ORDER_BUTTON_UP = (By.XPATH, './/button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_DOWN = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')

    FAQ_SECTION = (By.CLASS_NAME, 'accordion')
    NOT_HIDDEN_FAQ_ITEM_PANEL = (By.XPATH, './/div[@class="accordion__panel" and not(@hidden)]')

    FIRST_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-0')
    FIRST_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-0')

    SECOND_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-1')
    SECOND_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-1')

    THIRD_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-2')
    THIRD_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-2')

    FOURTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-3')
    FOURTH_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-3')

    FIFTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-4')
    FIFTH_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-4')

    SIXTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-5')
    SIXTH_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-5')

    SEVENTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-6')
    SEVENTH_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-6')

    EIGHTH_FAQ_ITEM_HEADING = (By.ID, 'accordion__heading-7')
    EIGHTH_FAQ_ITEM_PANEL = (By.ID, 'accordion__panel-7')
