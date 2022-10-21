from helpers import open_main_page
from locators.main_page_locators import MainPageLocators


def test_faq_click_first_item_open_first_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.FIRST_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.FIRST_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_second_item_open_second_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.SECOND_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.SECOND_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_third_item_open_third_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.THIRD_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.THIRD_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_fourth_item_open_fourth_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.FOURTH_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.FOURTH_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_fifth_item_open_fifth_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.FIFTH_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.FIFTH_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_sixth_item_open_sixth_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.SIXTH_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.SIXTH_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_seventh_item_open_seventh_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.SEVENTH_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.SEVENTH_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'


def test_faq_click_eighth_item_open_eighth_panel_text(browser):
    main_page = open_main_page(browser)

    main_page.click_faq_item_heading(MainPageLocators.EIGHTH_FAQ_ITEM_HEADING)
    assert main_page.is_faq_item_panel_not_hidden(MainPageLocators.EIGHTH_FAQ_ITEM_PANEL), 'FAQ item panel is hidden!'
