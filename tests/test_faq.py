from page_objects.main_page import MainPage
from links import MAIN_PAGE_LINK
from locators.main_page_locators import MainPageLocators


def test_faq_click_first_item_open_first_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.FIRST_FAQ_ITEM_HEADING)

    expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    actual_text = main_page.get_text(MainPageLocators.FIRST_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_second_item_open_second_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.SECOND_FAQ_ITEM_HEADING)

    expected_text = 'Пока что у нас так: один заказ — один самокат. ' \
                    'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    actual_text = main_page.get_text(MainPageLocators.SECOND_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_third_item_open_third_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.THIRD_FAQ_ITEM_HEADING)

    expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                    'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                    'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    actual_text = main_page.get_text(MainPageLocators.THIRD_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_fourth_item_open_fourth_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.FOURTH_FAQ_ITEM_HEADING)

    expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    actual_text = main_page.get_text(MainPageLocators.FOURTH_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_fifth_item_open_fifth_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.FIFTH_FAQ_ITEM_HEADING)

    expected_text = 'Пока что нет! ' \
                    'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    actual_text = main_page.get_text(MainPageLocators.FIFTH_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_sixth_item_open_sixth_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.SIXTH_FAQ_ITEM_HEADING)

    expected_text = 'Самокат приезжает к вам с полной зарядкой. ' \
                    'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. ' \
                    'Зарядка не понадобится.'

    actual_text = main_page.get_text(MainPageLocators.SIXTH_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_seventh_item_open_seventh_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.SEVENTH_FAQ_ITEM_HEADING)

    expected_text = 'Да, пока самокат не привезли. ' \
                    'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    actual_text = main_page.get_text(MainPageLocators.SEVENTH_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'


def test_faq_click_eighth_item_open_eighth_panel_text(browser):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(MainPageLocators.EIGHTH_FAQ_ITEM_HEADING)

    expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    actual_text = main_page.get_text(MainPageLocators.EIGHTH_FAQ_ITEM_PANEL)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'
