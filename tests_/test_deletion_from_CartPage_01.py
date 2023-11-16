import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener

class DeletionFromCartPage(unittest.TestCase):
    def setUp(self):
        self.simpledriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpledriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        sleep(20) #to avoid check message
        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Korea2022")
        sleep(6)  # to avoid CAPTCHA check
        loginPageObj.click_signin_button()
        navigationBarObj = NavigationBar(self.simpledriver)
        navigationBarObj.click_to_cart_button()

    def test_emptiness_of_cart_page(self):
        cartPageObj = CartPage(self.simpledriver)
        emptyCartMessage = cartPageObj.get_text_of_empty_cart_page()
        self.assertEqual(emptyCartMessage, "Your Amazon Cart is empty.")

    def test_delete_first_product_from_cart(self):
        cartPageObj = CartPage(self.simpledriver)
        cartPageObj.delete_first_product()

    def test_delete_all_products_from_cart(self):
        cartPageObj = CartPage(self.simpledriver)
        cartCountNumberElement = cartPageObj.get_text_of_cart_count_number()
        while cartCountNumberElement != 0:
            cartPageObj.delete_first_product()
            cartCountNumberElement -= 1
        else:
            print("Your Amazon cart is empty")

        self.assertEqual(cartCountNumberElement, 0)

    def tearDown(self):
        self.driver.close()
