from selenium import webdriver
import time
from pages.home.login_page import LoginPage
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_Valid_Login(self):
        self.lp.login('abhaysharmagzb@gmail.com','password')
        result = self.lp.verifyLoginSuccessfull()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(username='meow@gmail.com',password='pass')
        result = self.lp.verifyLoginFailed()
        assert result == True
