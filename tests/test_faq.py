import pytest

from page_objects.main_page import MainPage
from links import MAIN_PAGE_LINK
from locators.main_page_locators import MainPageLocators


@pytest.mark.parametrize('item_heading, expected_text, panel',
                         [(MainPageLocators.FIRST_FAQ_ITEM_HEADING,
                           'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                           MainPageLocators.FIRST_FAQ_ITEM_PANEL),
                          (MainPageLocators.SECOND_FAQ_ITEM_HEADING,
                           'Пока что у нас так: один заказ — один самокат. '
                           'Если хотите покататься с друзьями, '
                           'можете просто сделать несколько заказов — один за другим.',
                           MainPageLocators.SECOND_FAQ_ITEM_PANEL),
                          (MainPageLocators.THIRD_FAQ_ITEM_HEADING,
                           'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                           'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                           'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                           MainPageLocators.THIRD_FAQ_ITEM_PANEL),
                          (MainPageLocators.FOURTH_FAQ_ITEM_HEADING,
                           'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                           MainPageLocators.FOURTH_FAQ_ITEM_PANEL),
                          (MainPageLocators.FIFTH_FAQ_ITEM_HEADING,
                           'Пока что нет! '
                           'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                           MainPageLocators.FIFTH_FAQ_ITEM_PANEL),
                          (MainPageLocators.SIXTH_FAQ_ITEM_HEADING,
                           'Самокат приезжает к вам с полной зарядкой. '
                           'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                           'Зарядка не понадобится.',
                           MainPageLocators.SIXTH_FAQ_ITEM_PANEL),
                          (MainPageLocators.SEVENTH_FAQ_ITEM_HEADING,
                           'Да, пока самокат не привезли. '
                           'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                           MainPageLocators.SEVENTH_FAQ_ITEM_PANEL),
                          (MainPageLocators.EIGHTH_FAQ_ITEM_HEADING,
                           'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
                           MainPageLocators.EIGHTH_FAQ_ITEM_PANEL),
                          ])
def test_faq_click_item_open_panel_text(browser, item_heading, expected_text, panel):
    main_page = MainPage(browser, MAIN_PAGE_LINK)
    main_page.open()

    main_page.click_faq_item_heading(item_heading)

    expected_text = expected_text
    actual_text = main_page.get_text(panel)

    assert actual_text == expected_text, 'FAQ item panel is hidden!'
