from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
from traceback import print_stack
import utilities.custom_logger as cl
import logging


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info('Locator Type', locatorType, ' not correct/supported')

        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element Found with locator: {locator} and locatorType: {locatorType}')

        except:
            self.log.info(f'Element Not Found with locator: {locator} and locatorType: {locatorType}')

        return element

    def elementClick(self,locator,locatorType='id'):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info(f'Clicked on element with locator:{locator} locatorType: {locatorType}')
        except:
            self.log.info(f'Cannot click on element with locator:{locator} locatorType: {locatorType}')
            print_stack()

    def sendKeys(self,data,locator,locatorType='id'):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info(f'Sent Data on element with locator:{locator} locatorType: {locatorType}')
        except:
            self.log.info(f'Cannot sent data on element with locator:{locator} locatorType: {locatorType}')
            print_stack()

    def isElementPresent(self, locator, locatorType ='id'):
        element = self.getElement(locator, locatorType)
        try:
            if element is not None:
                self.log.info('Element Found')
                return True
            else:
                return False
        except:
            self.log.info('Element Not Found')
            return False

    def elementPresenceCheck(self, locator, byType):
        elementList = self.driver.find_elements(byType, locator)
        try:
            if len(elementList) > 0:
                self.log.info('Element Found')
                return True
            else:
                return False
        except:
            self.log.info('Element Not Found')
            return False


    def waitForElement(self,locator,locatorType='id',timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info(f'Waiting for Maximium {timeout} :: seconds  for element to be clickable')

            wait =WebDriverWait(self.driver,10,poll_frequency=1,ignored_exceptions=
                                [NoSuchElementException,ElementNotVisibleException,
                                 ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,locator)))

            self.log.info('Element appeared on the Webpage')

        except:
            self.log.info('Element not appeared on the webpage')
            print_stack()

        return element