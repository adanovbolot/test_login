from typing import List
from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from base.utils import Utils


class LoginPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.__USERNAME = '//input[@id="user-name"]'
        self.__PASSWORD = '//input[@id="password"]'
        self.__BUTTON = '//input[@id="login-button"]'
        self.__ERROR = '//h3[@data-test="error"]'
        self.__ELEMENT_SITE = '//span[@class="title"]'

        self.EXPECTED_ERROR_PASSWORD = \
            'Epic sadface: Password is required'
        self.EXPECTED_ERROR_USERNAME = \
            'Epic sadface: Username is required'
        self.EXPECTED_201_OK = \
            'PRODUCTS'
        self.EXPECTED_ERROR_USERNAME_PASSWORD = \
            'Epic sadface: Username and password do not match any user in this service'

    def username(self) -> WebElement:
        return self.is_present('xpath', self.__USERNAME)

    def password(self) -> WebElement:
        return self.is_present('xpath', self.__PASSWORD)

    def button(self) -> WebElement:
        return self.is_present('xpath', self.__BUTTON)

    def error(self):
        return self.is_present('xpath', self.__ERROR)

    def element_site(self):
        return self.is_present('xpath', self.__ELEMENT_SITE)
