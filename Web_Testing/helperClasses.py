import enum

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class helper:

    def __init__(self):
        self.month_dict = {"January": 1, "February": 2, "March": 3
            , "April": 4, "May": 5, "June": 6
            , "July": 7, "August": 8, "September": 9
            , "October": 10, "November": 11, "December": 12
                           }
        pass
    driver = None

    def chrome_driver_init(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # tb refers to Toolbar, tb_.. refers to Toolbar elements
        return driver

    def firefox_driver_init(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver

    def element_exists_by_xpath(self, driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def element_exists_by_class(self, driver, class_name):
        try:
            driver.find_element_by_class_name(class_name)
        except NoSuchElementException:
            return False
        return True

    def element_exists_by_id(self, driver, vid):
        try:
            driver.find_element_by_id(vid)
        except NoSuchElementException:
            return False
        return True

    # safe find elements

    def find_element_by_xpath(self, driver, xpath):
        try:
            element = driver.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_class_name(self, driver, class_name):
        try:
            element = driver.find_element_by_class_name(class_name)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_id(self, driver, vid):
        try:
            element = driver.find_element_by_id(vid)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_link_text(self, driver, link_txt):
        try:
            element = driver.find_element_by_link_text(link_txt)
            return element
        except NoSuchElementException:
            return None

    # v_by specifies element from 'by' enum, path is the value either Class Name, ID, or XPATH
    def find_element(self, driver, v_by, path):
        if v_by == by.ID:
            return self.find_element_by_id(driver, path)
        elif v_by == by.XPATH:
            return self.find_element_by_xpath(driver, path)
        else:
            return self.find_element_by_class_name(driver, path)

    def select_element_by_index(self, element, index):
        selector = Select(element)
        selector.select_by_index(index)

    def select_element_by_text(self, element, text):
        selector = Select(element)
        selector.select_by_visible_text(text)

    def get_month_dict(self):
        return self.month_dict

    def get_month_name_from(self, in_val):

        if in_val < 1 or in_val > 12:
            return ""

        for name, val in self.month_dict:
            if val == in_val:
                return name

        # default value, should not be reached logically if in_val is right
        return ""

    def get_month_val_from(self, name):
        return self.month_dict.get(name)

    def click_button(self, btn):
        btn.click()

    def fill(self, txt_element, text):
        txt_element.send_keys(text)

    def clear_txt(self, txt_element):
        txt_element.clear()

    def click_button_safe(self, btn):
        if btn is None:
            return
        btn.click()

    def fill_safe(self, txt_element, text):
        if txt_element is None:
            return
        txt_element.send_keys(text)

    def clear_txt_safe(self, txt_element):
        if txt_element is None:
            return
        txt_element.clear()

    def screenshot(self, driver):
        return driver.get_screenshot_as_png()

    def report_allure(self, driver, msg):
        allure.attach(self.screenshot(driver), msg,
                      attachment_type=AttachmentType.PNG)


class DOB():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_month_value(self):
        pass

    def get_month_name(self):
        pass


class Profile():
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


class ConstantsClass:

    def __init__(self):
        self.delay_time = 5
        self.test_accounts_dict = {"test_projectX@hotmail.com": "TestingTeamMKE2020"}
        self.test_accounts_to_profiles = {"test_projectX@hotmail.com":
                                              Profile("test_projectX@hotmail.com"
                                                      , "TestingTeamMKE"
                                                      , "Testing_TeamX", DOB(21, 2, 2020), Gender.MALE)}

    def get_home_link(self):
        return "https://www.spotify.com/eg-en/"

    def get_account_overview_link(self):
        return "https://www.spotify.com/eg-en/account/overview"

    def get_test_emails(self):
        emails = list(self.test_accounts_dict.keys())
        return emails

    def get_pass(self, email):
        return self.test_accounts_dict[email]

    def get_profile(self, email):
        return self.test_accounts_to_profiles.get(email)

    def get_registered_emails(self):
        return ["mohdos_1999@hotmail.com"]


class by(enum.Enum):
    ID = 1
    XPATH = 2
    CLASS_NAME = 3


class Gender(enum.Enum):
    MALE = "Male"
    FEMALE = "Female"
    UNSELECTED = "Un selected"
