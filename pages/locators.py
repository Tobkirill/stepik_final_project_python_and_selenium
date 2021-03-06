from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FOR_REG = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FOR_REG = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_REG = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MSG_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_NAME_IN_SUCCESS_MSG = (By.CSS_SELECTOR, '.alertinner>strong')
    CART_AMOUNT = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_CART_BUTTON = (By.CSS_SELECTOR, '.btn-group>.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ShoppingCart:
    SHOPPING_CART_SUMMARY = (By.CSS_SELECTOR, '#basket_formset')
    SHOPPING_CART_IS_EMPTY_MSG = (By.CSS_SELECTOR, '#content_inner>p')
