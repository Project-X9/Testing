from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import allure
from allure_commons.types import AttachmentType


class Helper:
    """
       A class used to represent the Login page test
       ...
       Attributes
       ----------
    None

       Methods
       -------

       driver_init()
            Initiates the web driver
       element_exists_by_id()
            Safely checks that element exist by id
       element_exists_by_accessibility_id()
            Safely checks that element exist by accessibility id
       element_exists_by_xpath()
            Safely checks that element exist by xpath
       find_element_by_xpath()
            Safely find element by xpath
       find_element_by_id()
            Safely find element by id
       find_element_by_accessibility_id()
            Safely find element by accessibility id
       screenshot()
            takes a screen shot of the app
       report_allure()
            attach the screen shot to allure report

       """
    @staticmethod
    def driver_init():
        """
        initiates the driver
        """
        driver = webdriver.Remote("http://localhost:4723/wd/hub", Constants.desired_cap, keep_alive=False)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def element_exists_by_id(driver, _id):
        """
        Safely checks that element exist by id
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param _id: id of the element
        :type _id string
        :return: Boolean
        """
        try:
            driver.find_element_by_id(_id)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def element_exists_by_accessibility_id(driver, accessibility_id):
        """
        Safely checks that element exist by accessibility id
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param accessibility_id: accessibility id of the element
        :type accessibility_id string
        :return: Boolean
        """
        try:
            driver.find_element_by_accessibility_id(accessibility_id)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def element_exists_by_xpath(driver, xpath):
        """
        Safely checks that element exist by id
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param xpath: xpath of the element
        :type xpath string
        :return: Boolean
        """
        try:
            driver.find_element_by_xpath(xpath)
            driver.implicitly_wait(5)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def find_element_by_xpath(driver, xpath):
        """
        Safely find that element by xpath
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param xpath: id of the element
        :type xpath string
        :return: Boolean
        """
        try:
            element = driver.find_element_by_xpath(xpath)
            driver.implicitly_wait(5)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def find_element_by_id(driver, _id):
        """
        Safely find that element by id
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param _id: id of the element
        :type _id string
        :return: Boolean
        """
        try:
            element = driver.find_element_by_id(_id)
            driver.implicitly_wait(5)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def find_element_by_accessibility_id(driver, accessibility_id):
        """
        Safely find that element by accessibility id
        :param driver: driver that will find the element
        :type driver: WebDriver
        :param accessibility_id: id of the element
        :type accessibility_id string
        :return: Boolean
        """
        try:
            element = driver.find_element_by_xpath(accessibility_id)
            driver.implicitly_wait(5)
            return element
        except NoSuchElementException:
            return None

    @staticmethod
    def screenshot(driver):
        """
            takes a screen shot of the app
        """
        return driver.get_screenshot_as_png()

    @staticmethod
    def report_allure(driver, msg):
        """
                    attach the screen shot to allure report
        """
        allure.attach(Helper.screenshot(driver), msg,
                      attachment_type=AttachmentType.PNG)


class Constants:
    """
         A class used to represent the Login page test
         ...
         Attributes
         ----------
        desired_cap : dictionary
                The details of your device
        correct_credentials : dictionary
                The correct credentials for login
        first_song_playlist : string
                the xpath fo the first element in playlist

         Methods
         -------
            None

         """

    # desired_cap = {
    #     "deviceName": "AndroidEmulator",
    #     "platformName": "Android",
    #     "app": "/Users/KIMO/AndroidStudioProjects/ProjectX/app/build/outputs/apk/debug/app-debug.apk",
    #     "appWaitActivity": ".authentication.AuthenticationPage",
    #     "appWaitPackage": "com.example.projectx"
    # }
    # desired_cap = {
    #     "deviceName": "samsung-sm_g955f-ce11171b62faecd00c",
    #     "platformName": "Android",
    #     "app": "/Users/KIMO/AndroidStudioProjects/ProjectX/app/build/outputs/apk/debug/app-debug.apk",
    #     "appWaitActivity": ".authentication.AuthenticationPage",
    #     "appWaitPackage": "com.example.projectx"
    # }
    desired_cap = {
        "deviceName": "samsung-sm_a207f-R9WM91DQY1J",
        "platformName": "Android",
        "app": "/Users/KIMO/AndroidStudioProjects/ProjectX/app/build/outputs/apk/debug/app-debug.apk",
        "appWaitActivity": ".authentication.AuthenticationPage",
        "appWaitPackage": "com.example.projectx"
    }
    correct_credentials = {
        "email": "abdallah@gmail.com",
        "password": "123456"
    }
    first_song_playlist = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout"
