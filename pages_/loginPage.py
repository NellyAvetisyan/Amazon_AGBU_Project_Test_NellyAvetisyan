from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signinButtonLocator = (By.ID, "signInSubmit")
        self.__invalidUsernameMassageLocator = (By.CLASS_NAME, "a-list-item")
        self.__invalidPasswordMassageLocator = (By.CLASS_NAME, "a-list-item")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_signin_button(self):
        signinButtonElement = self._find_element(self.__signinButtonLocator)
        self._click(signinButtonElement)

    def get_text_of_invalid_password_message(self):
        invalidPasswordMessageElement = self._find_element(self.__invalidPasswordMassageLocator)
        self._get_element_text(invalidPasswordMessageElement)
        return invalidPasswordMessageElement

    def get_text_of_invalid_username_message(self):
        invalidUsernameMassageElement = self._find_element(self.__invalidUsernameMassageLocator)
        self._get_element_text(invalidUsernameMassageElement)
        return invalidUsernameMassageElement
