from .base_page import BasePage
from .locators import ShoppingCart


class BasketPage(BasePage):
    def is_shopping_cart_empty(self):
        assert self.is_not_element_present(*ShoppingCart.SHOPPING_CART_SUMMARY), "Shopping cart is not empty"
        assert self.is_element_present(*ShoppingCart.SHOPPING_CART_IS_EMPTY_MSG), "Empty shopping cart msg is not present"
