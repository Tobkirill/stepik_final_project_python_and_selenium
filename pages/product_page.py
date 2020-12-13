from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            f"'Add to cart' button is not present on the page"

    def add_product_to_cart(self):
        self.should_be_add_to_cart_button()
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_success_msg_of_added_product(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG_OF_ADDED_PRODUCT)

    def should_be_the_same_name_in_success_msg(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MSG)
        assert product_name.text == product_name_in_msg.text, f"Product name is incorrect in success msg"

    def should_be_correct_text_of_success_msg(self):
        self.should_be_the_same_name_in_success_msg()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_OF_ADDED_PRODUCT)
        assert product_name.text in success_msg.text, f"{product_name.text} is not in success msg string"

    def should_be_the_same_product_price_and_cart_amount(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_amount = self.browser.find_element(*ProductPageLocators.CART_AMOUNT)
        assert product_price.text == cart_amount.text, "Product price and cart amount is not the same"
