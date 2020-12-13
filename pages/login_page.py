from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_correct("login"), f"substring 'login' is absent in {self.url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            f"{LoginPageLocators.LOGIN_FORM[1]} is not on the login page,login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            f"{LoginPageLocators.REGISTRATION_FORM} is not on tha page, reg form not found"
