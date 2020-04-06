from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import allure
from allure_commons.types import AttachmentType
import enum

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
            "appWaitPackage": "com.example.projectx"
        }



class by(enum.Enum):
    ID = 1
    XPATH = 2
    CLASS_NAME = 3
    LINK_TEXT = 4


class Gender(enum.Enum):
    MALE = "Male"
    UNSELECTED = "Un selected"
    FEMALE = "Female"


class Profile:
    # TODO: add any required fields here
    # dob = Date of Birth
    # c_email = Confirmed Email, if not provided -> set with the original email (Used for signup mismatched emails test)
    def __init__(self, email, password, name, dob, gender, c_email=''):
        self.email = email
        self.c_email = email
        if c_email != '':
            self.c_email = c_email
        self.password = password
        self.name = name
        self.dob = dob
        self.gender = gender


class DOB:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_month_value(self):
        pass

    def get_month_name(self):
        pass

    def is_equal(self, dob):
        if int(dob[1])==self.day and int(dob[0])==self.month and int(dob[2])==self.year:
            return True
        return False


class ConstantsClass:

    def __init__(self):
        self.delay_time = 5

        self.test_accounts_dict = { "test_projectX@hotmail.com" : "TestingTeamMKE" }
        self.test_accounts_to_profiles = { "test_projectX@hotmail.com" :
                                               Profile("test_projectX@hotmail.com"
                                                       , "TestingTeamMKE"
                                                       , "Testing TeamX", DOB(21, 2, 2020), Gender.MALE)
                                           , "test1@test.com" :
                                               Profile("test1@test.com"
                                                       , "test123"
                                                       , "Testing TeamX", DOB(21, 2, 1990), Gender.MALE)
                                           , "test2@test.com" :
                                               Profile("test2@test.com"
                                                       , "test234"
                                                       , "Testing TeamX", DOB(21, 2, 1992), Gender.MALE)
                                           , "test3@test.com" :
                                               Profile("test3@test.com"
                                                       , "test345"
                                                       , "Testing TeamX", DOB(21, 2, 2000), Gender.FEMALE)
                                           , "test4@test.com" :
                                               Profile("test4@test.com"
                                                       , "test456"
                                                       , "Testing TeamX", DOB(21, 2, 1950), Gender.MALE, "email_different@test.com")
                                           , "test50@test.com" :
                                               Profile("test50@test.com"
                                                       , "test505152"
                                                       , "Testing TeamX", DOB(21, 2, 1950), Gender.MALE, "test50@test.com")
                                           , "test51@test.com" :
                                               Profile("test51@test.com"
                                                       , "test505152"
                                                       , "Testing TeamX", DOB(21, 2, 1950), Gender.MALE, "test51@test.com")
                                           }

    def get_home_link(self):
        return "http://localhost:3000/home"

    def get_account_overview_link(self):
        return "http://localhost:3000/accountoverview"

    def get_test_emails(self):
        emails = list(self.test_accounts_dict.keys())
        return emails

    def get_pass(self, email):
        return self.test_accounts_dict[email]

    def get_dob(self, email):
        return self.test_accounts_to_profiles.get(email).dob

    def get_name(self, email):
        return self.test_accounts_to_profiles.get(email).name

    def get_profile(self, email):
        return self.test_accounts_to_profiles.get(email)

    def get_registered_emails(self):
        return ["mohdos_1999@hotmail.com"]

