from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import allure
from allure_commons.types import AttachmentType
import uiautomator2

class MobileHelper:
    @staticmethod
    def driver_init():
        driver = webdriver.Remote("http://localhost:4723/wd/hub", Constants().desired_cap)
        driver.implicitly_wait(10)
        return driver

    def set_driver(self, driver):
        self.driver = driver

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
    def find_element_by_id(driver, id):
        try:
            full_id = "com.example.projectx:id/" + id
            element = driver.find_element_by_id(full_id)
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
        allure.attach(MobileHelper.screenshot(driver), msg,
                      attachment_type=AttachmentType.PNG)


class Constants:
    def __init__(self):
        self.apk_locations = \
            [r"C:\Users\Mohammad\Desktop\University\Software_Engineering\Other Teams\Android-master\ProjectX\app\build\outputs\apk\debug\app-debug.apk",
             "/Users/KIMO/AndroidStudioProjects/ProjectX/app/build/outputs/apk/debug/app-debug.apk",
             "EMAN_LOCATION HERE..."
             ]
        self.mo_os = 0
        self.kimo = 1
        self.eman = 2
        self.desired_cap = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "platformVersion": "9",
            "app": self.apk_locations[self.mo_os],
            "appWaitActivity": ".authentication.AuthenticationPage",
            "appWaitPackage": "com.example.projectx",
            "automationName": "uiautomator2"
        }
