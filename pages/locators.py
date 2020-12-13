from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MSG_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_NAME_IN_SUCCESS_MSG = (By.CSS_SELECTOR, '.alertinner>strong')
    CART_AMOUNT = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
