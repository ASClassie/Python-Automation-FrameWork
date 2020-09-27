from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _login_link = "a[href*='/sign_in']"
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType='css')

    def enterEmail(self, email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType='name')

    def login(self, username, password):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessfull(self):
        result = self.isElementPresent("img[class ='gravatar']",locatorType='xpath')

        return result

    def verifyLoginFailed(self):
        pass
