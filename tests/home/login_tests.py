from selenium import webdriver
import time
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_Valid_Login(self):
        base_url = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\\chromedriver.exe')
        driver.implicitly_wait(7)
        driver.get(base_url)
        lp = LoginPage(driver)
        lp.login('abhaysharmagzb@gmail.com', 'abhay@1#')
        result = lp.verifyLoginSuccessfull()

        assert result == True
        driver.quit()


test = LoginTests()
test.test_Valid_Login()
