import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from time import sleep
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LogIn(unittest.TestCase):
    def setUp(self):
        self.simpledriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpledriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        sleep(20) #to avoid check message

    def test_01_positive_login(self):
        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Korea2022")
        sleep(6)  # to avoid CAPTCHA check
        loginPageObj.click_signin_button()

        self.assertEqual(self.driver.title, "Amazon.com. Spend less. Smile more.")

    def test_01_negative_login(self):
        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nellikoko91@gmail.com")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("12345678")
        loginPageObj.click_signin_button()

        # self.assertEqual(self.driver.title, "Amazon Sign-In")
        invalidPasswordMessage = loginPageObj.get_text_of_invalid_password_message()
        self.assertEqual(invalidPasswordMessage, "Your password is incorrect")

    def test_02_negative_login(self):
        loginPageObj = LoginPage(self.simpledriver)
        loginPageObj.fill_username_field("Nelli91lllllllll@gmail.com")
        loginPageObj.click_to_continue_button()

        invalidUsernameMessage = loginPageObj.get_text_of_invalid_username_message()
        self.assertEqual(invalidUsernameMessage, "We cannot find an account with that email address")
        print("There was a problem. We cannot find an account with that email address/mobile number")

    def tearDown(self):
        self.driver.close()
