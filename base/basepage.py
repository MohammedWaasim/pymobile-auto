import pdb

import allure
from allure_commons.types import AttachmentType
from appium.webdriver import WebElement
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.custom_logger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locator, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locator))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locator))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locator)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locator)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locator))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locator)))
            return element
        else:
            self.log.info("Locator value " + locator + "not found")

        return element

    def getElement(self, locator, locatorType="id")->WebElement:
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locator, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locator :" + locator)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locator :" + locator)

        return element

    def clickElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locator, locatorType)
            element.click()
            cl.allureLogs("Clicked on Element with LocatorType: " + locatorType + " and with the locator :" + locator)
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locator :" + locator)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locator :" + locator)

    def isDisplayed(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locator, locatorType)
            element.is_displayed()
            cl.allureLogs(" Element with LocatorType: " + locatorType + " and with the locator :" + locator + "is displayed ")
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locator :" + locator + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locator :" + locator + " is not displayed")
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            allure.attach.file(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)
            cl.allureLogs("Screenshot save to Path : " + screenshotPath)
        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def enterText(self,text,locator,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            element=self.getElement(locator,locatorType)
            element.send_keys(text)
            cl.allureLogs("entered give text "+text+ " in LocatorType: " + locatorType + " and with the locator :" + locator )
        except:
            self.log.info(
                " could not enter give text in LocatorType: " + locatorType + " and with the locator :" + locator )
