from base.selenium_driver import SeleniumDriver
import pytest
import utilities.custom_logger as cl
import logging
from traceback import print_stack

class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.resultList = []

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenshot(resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("EXCEPTION Occurred !!!")
            self.screenshot(resultMessage)
            print_stack()

    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self,testName,result,resultMessage):
        self.setResult(result,resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName, " ### TEST FAILED ###")
            self.resultList.clear()
            assert True == False

        else:
            self.log.info(testName, " ### TEST SUCCESSFUL ###")
            self.resultList.clear()
            assert True == False









