from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import allure
from allure_commons.types import AttachmentType

class Helper:

    @staticmethod
    def driver_init():
        driver = webdriver.Remote("http://localhost:4723/wd/hub", Constants.desired_cap)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def element_exists_by_id(driver, _id):
        try:
            driver.find_element_by_id(_id)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def element_exists_by_accessibility_id(driver, accessibility_id):
        try:
            driver.find_element_by_accessibility_id(accessibility_id)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def element_exists_by_xpath(driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def find_element_by_xpath(driver, xpath):
        try:
            element = driver.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def find_element_by_id(driver, _id):
        try:
            element = driver.find_element_by_id(_id)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def find_element_by_accessibility_id(driver, accessibility_id):
        try:
            element = driver.find_element_by_xpath(accessibility_id)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def screenshot(driver):
        return driver.get_screenshot_as_png()

    @staticmethod
    def report_allure(driver, msg):
        allure.attach(Helper.screenshot(driver), msg,
                      attachment_type=AttachmentType.PNG)


class Constants:
    desired_cap = {
        "deviceName": "AndroidEmulator",
        "platformName": "Android",
        "app": "/Users/KIMO/AndroidStudioProjects/ProjectX/app/build/outputs/apk/debug/app-debug.apk",
        "appWaitActivity": ".authentication.AuthenticationPage",
        "appWaitPackage": "com.example.projectx"
    }
