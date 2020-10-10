from selenium import webdriver
import time
from pages.home.login_page import LoginPage
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_Valid_Login(self):
        self.lp.login('abhaysharmagzb@gmail.com','password')
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1,"Title is Incorrect")
        result2 = self.lp.verifyLoginSuccessfull()
        self.ts.markFinal('test_Valid_Login',result2,"Login was not successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(username='meow@gmail.com',password='pass')
        result = self.lp.verifyLoginFailed()
        assert result == True
