from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
        self.__cartPageProductNumber = (By.CLASS_NAME, "a-spacing-mini a-spacing-top-base")

    def delete_first_product(self):
        firstProductDeleteButton = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButton)

    def get_text_of_empty_cart_page(self):
        cartPageProductNumber = self._find_element(self.__cartPageProductNumber)
        # if cartPageProductNumber.text == "Your Amazon Cart is empty."
        return self._get_element_text(cartPageProductNumber)

    # def delete_all_products(self):
    #     firstProductDeleteButton = self._find_element(self.__firstProductDeleteButtonLocator)
    #     cartPageProductCount = self._find_element(self.__cartPageProductNumber))
    #     while cartPageProductCount != 0:
    #         self._click(firstProductDeleteButton)
    #         cartPageProductNumber -= 1
    #     else:
    #         print("Your cart is empty")

    def get_text_of_cart_count_number(self):
        cartCountNumberElement = self._find_element(self.__cartPageProductNumber)
        return int(self._get_element_text(cartCountNumberElement))
