
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.util =Util()

    def VerifyPageTitle(self,titleToVerify):

        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle,titleToVerify)
        except:
            self.log.error('Failed to get Page title')
            print_stack()
            return False