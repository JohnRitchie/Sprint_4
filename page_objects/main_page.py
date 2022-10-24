from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def is_faq_item_panel_not_hidden(self, item_panel):
        not_hidden_item_panel = self.browser.find_element(*MainPageLocators.NOT_HIDDEN_FAQ_ITEM_PANEL)
        clicked_item_panel = self.browser.find_element(*item_panel)
        return clicked_item_panel == not_hidden_item_panel

    def click_faq_item_heading(self, item_heading):
        self.click_button(item_heading)

    def click_order_button_up(self):
        self.click_button(MainPageLocators.ORDER_BUTTON_UP)

    def click_order_button_down(self):
        self.click_button(MainPageLocators.ORDER_BUTTON_DOWN)
