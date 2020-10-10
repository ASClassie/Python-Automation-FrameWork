from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_link = "a[href*='/login']"
    _email_field = 'email'
    _password_field = 'password'
    _login_button = 'input[value="Login"]'

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='css')

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='css')

    def login(self, username='', password=''):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()
    def verifyLoginSuccessfull(self):
        self.waitForElement("//img[contains(@class,'zl-navbar-rhs-img')]",locatorType='xpath',timeout=5,pollFrequency=1)
        result = self.isElementPresent("//img[contains(@class,'zl-navbar-rhs-img')]", locatorType='xpath')

        return result

    def verifyLoginFailed(self):
        self.waitForElement('//span[@class="dynamic-text help-block"]',locatorType='xpath',timeout=5,pollFrequency=1)
        result = self.isElementPresent('//span[@class="dynamic-text help-block"]',locatorType='xpath')

        return result

    def verifyLoginTitle(self):
        return self.VerifyPageTitle("Google")



