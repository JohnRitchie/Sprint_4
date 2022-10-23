from selenium.webdriver.common.by import By


class BasePageLocators:
    YA_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    YA_SEARCH_BUTTON = (By.XPATH, './/button[text()="Найти"]')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
