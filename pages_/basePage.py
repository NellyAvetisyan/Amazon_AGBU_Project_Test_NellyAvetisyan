from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print("ERROR:Element not found or wrong")
            exit(1)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _elementy_should_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("ERROR: Element should be visible but not")
            logger("ERROR", "Element should be visible but not")
            exit(3)

    def _click(self, webElement):
        webElement.click()

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)
        logger("INFO", "text successfully added to element")

    def _get_title(self):
        return self.driver.title

    def _get_element_text(self, webElement):
        return webElement.text

    def _press_and_hold(self):
        pass

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

    def _double_click(self):
        pass
