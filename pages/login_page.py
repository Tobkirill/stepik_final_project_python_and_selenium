from .base_page import BasePage
from .locators import LoginPageLocators
import faker


class LoginPage(BasePage):
    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        email_for_reg = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REG)
        email_for_reg.send_keys(email)
        password_for_reg = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REG)
        password_for_reg.send_keys("Tduyrhdfk123")
        repeat_password_reg = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_REG)
        repeat_password_reg.send_keys("Tduyrhdfk123")
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


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
