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


class Browser(enum.Enum):
    CHROME = 0
    FIREFOX = 1


class WebHelper:
    """
    A class used to provide helper function to ease testing

    ...

    Attributes
    ----------
    base_url : str
        holds the base url for the website
    month_dict : dict
        a dictionary that maps the month name to month number
    driver : WebDriver
        holds the web driver of the class

    Methods
    -------
    get_login_url(email)
        gets the login url of the website
    get_signup_url(email)
        gets the signup url of the website
    get_premium_url(email)
        gets the premium url of the website
    get_home_url(email)
        gets the home url of the website
    get_account_overview_url(email)
        gets the account overview url of the website
    get_account_edit_url(email)
        gets the account edit url of the website
    get_account_changepassword_url()
        gets the change password url of the website
    set_driver(driver)
        sets the class' driver with the input driver
    chrome_driver_init()
        initializes the chrome driver
    firefox_driver_init()
        initializes the firefox driver
    get_driver()
        gets the class' driver
    url_has(text, driver=None)
        checks if the current driver url contains the input text
    element_exists_by_xpath(xpath)
        Checks if an element exists with the input xpath
    element_exists_by_class(class_name)
        Checks if an element exists with the input class name
    element_exists_by_id(vid)
        Checks if an element exists with the input id
    find_element_by_xpath(xpath)
        finds the element with the given xpath
    find_elements_by_xpath(xpath)
        finds the elements with the given xpath
    find_element_by_class_name(class_name)
        finds the element with the given class name
    find_elements_by_class_name(class_name, driver=None)
        finds the elements with the given class name
    find_element_by_id(vid)
        finds the element with the given id
    find_elements_by_id(vid)
        finds the elements with the given id
    find_element_by_name(vname)
        finds the element with the given name
    find_elements_by_name(vname)
        finds the elements with the given name
    find_element_by_link_text(link_txt)
        finds the element with the given link text
    find_elements_by_link_text(link_txt)
        finds the elements with the given link text
    select_element_by_index(element, index)
        selects an option from the provided element using a given index
    select_element_by_text(element, text)
        selects an option from the provided element using a given text
    get_month_dict()
        gets the month name to month number dictionary
    get_month_name_from(in_val)
        gets the month name from the input month number
    get_month_val_from(name)
        gets the month number from the input month name
    click_button(btn)
        clicks on the given button
    fill(txt_element, text)
        fills the provided text field with the given text
    clear_txt(txt_element)
        clears the given text field
    click_button_safe(btn)
        safely clicks on the given button without causing a crash
    fill_safe(txt_element, text)
        safely fills the provided text field with the given text without causing a crash
    clear_txt_safe(txt_element)
        safely clears the given text field without causing a crash
    screenshot(driver)
        takes a screenshot of the website using the given driver
    report_allure(msg, driver=None)
        attaches a screenshot to allure's report with a given message

    """

    base_url = "http://localhost:3000/"
    month_dict = {"January": 1, "February": 2, "March": 3
        , "April": 4, "May": 5, "June": 6
        , "July": 7, "August": 8, "September": 9
        , "October": 10, "November": 11, "December": 12
                       }

    def get_login_url(self):
        """
        gets the login url of the website

        :returns: the login url of the website
        :rtype: str
        """
        return self.base_url + "signin"

    def get_signup_url(self):
        """
        gets the signup url of the website

        :returns: the signup url of the website
        :rtype: str
        """
        return self.base_url + "signup"

    def get_premium_url(self):
        """
        gets the premium url of the website

        :returns: the premium url of the website
        :rtype: str
        """
        return self.base_url + "premium"

    def get_home_url(self):
        """
        gets the home url of the website

        :returns: the home url of the website
        :rtype: str
        """
        return self.base_url + "home"

    def get_account_overview_url(self):
        """
        gets the account overview url of the website

        :returns: the account overview url of the website
        :rtype: str
        """
        return self.base_url + "account/overview"

    def get_account_edit_url(self):
        """
        gets the edit account url of the website

        :returns: the edit account url of the website
        :rtype: str
        """
        return self.base_url + "account/edit"

    def get_account_changepassword_url(self):
        """
        gets the change password url of the website

        :returns: the change password url of the website
        :rtype: str
        """
        return self.base_url + "account/changepassword"

    def set_driver(self, driver):
        """
        sets the class' driver with the input driver

        :param driver: the driver to which the class' driver is to be set
        :type driver: WebDriver

        """
        self.driver = driver

    def chrome_driver_init(self):
        """
        initializes the chrome driver

        :returns: the class' driver
        :rtype: WebDriver
        """
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        return self.driver

    def firefox_driver_init(self):
        """
        initializes the firefox driver

        :returns: the class' driver
        :rtype: WebDriver
        """
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return self.driver

    def get_driver(self):
        """
        gets the class' driver

        :returns: the class' driver
        :rtype: WebDriver
        """
        return self.driver

    def url_has(self, text, driver=None):
        """
        checks if the current driver url contains the input text

        If the argument `driver` is not passed in, the class' driver is used

        :param text: the text to be compared with the driver's current url
        :type text: str

        :param driver: the driver from which to retrieve the url (default is None)
        :type driver: WebDriver

        :returns: a boolean to check if the current driver's url contains the input text or not
        :rtype: bool
        """
        if driver is None:
            driver = self.driver
        url = str(driver.current_url)
        result = url.find(text)
        if result == -1:
            return False
        else:
            return True

    def element_exists_by_xpath(self, xpath):
        """
        Checks if an element exists with the input xpath

        :param xpath: element xpath
        :type xpath: str

        :returns: a boolean to check if the element exists or not
        :rtype: bool
        """
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def element_exists_by_class(self, class_name):
        """
        Checks if an element exists with the input class name

        :param class_name: element class name
        :type class_name: str

        :returns: a boolean to check if the element exists or not
        :rtype: bool
        """
        try:
            self.driver.find_element_by_class_name(class_name)
        except NoSuchElementException:
            return False
        return True

    def element_exists_by_id(self, vid):
        """
        Checks if an element exists with the input id

        :param vid: element id
        :type vid: str

        :returns: a boolean to check if the element exists or not
        :rtype: bool
        """
        try:
            self.driver.find_element_by_id(vid)
        except NoSuchElementException:
            return False
        return True

    # safe find elements

    def find_element_by_xpath(self, xpath):
        """
        finds the element with the given xpath

        :param xpath: element xpath
        :type xpath: str

        :returns: a WebDriver element associated with the given xpath
        :rtype: WebDriver element
        """
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    def find_elements_by_xpath(self, xpath):
        """
        finds the elements with the given xpath

        :param xpath: elements xpath
        :type xpath: str

        :returns: a list containing the WebDriver elements associated with the given xpath
        :rtype: list
        """
        try:
            element = self.driver.find_elements_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_class_name(self, class_name):
        """
        finds the element with the given class name

        :param class_name: element class name
        :type class_name: str

        :returns: a WebDriver element associated with the given class name
        :rtype: WebDriver element
        """
        try:
            element = self.driver.find_element_by_class_name(class_name)
            return element
        except NoSuchElementException:
            return None

    def find_elements_by_class_name(self, class_name, driver=None):
        """"
        finds the elements with the given class name

        If the argument `driver` is not passed in, the class' driver is used

        :param class_name: elements class name
        :type class_name: str

        :param driver: the driver from which to retrieve the element (default is None)
        :type driver: WebDriver

        :returns: a list containing the WebDriver elements associated with the given class name
        :rtype: list
        """
        if driver is None:
            driver = self.driver
        try:
            element = driver.find_elements_by_class_name(class_name)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_id(self, vid):
        """"
        finds the element with the given id

        :param vid: element id
        :type vid: str

        :returns: a WebDriver element associated with the given id
        :rtype: WebDriver element
        """
        try:
            element = self.driver.find_element_by_id(vid)
            return element
        except NoSuchElementException:
            return None

    def find_elements_by_id(self, vid):
        """"
        finds the elements with the given id

        :param vid: elements id
        :type vid: str

        :returns: a list containing the WebDriver elements associated with the given id
        :rtype: list
        """
        try:
            element = self.driver.find_elements_by_id(vid)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_name(self, vname):
        """
        finds the element with the given name

        :param vname: element name
        :type vname: str

        :returns: a WebDriver element associated with the given name
        :rtype: WebDriver element
        """
        try:
            element = self.driver.find_element_by_name(vname)
            return element
        except NoSuchElementException:
            return None

    def find_elements_by_name(self, vname):
        """
        finds the elements with the given name

        :param vname: elements name
        :type vname: str

        :returns: a list containing the WebDriver elements associated with the given name
        :rtype: list
        """
        try:
            element = self.driver.find_elements_by_name(vname)
            return element
        except NoSuchElementException:
            return None

    def find_element_by_link_text(self, link_txt):
        """
        finds the element with the given link text

        :param link_txt: element link text
        :type link_txt: str

        :returns: a WebDriver element associated with the given link text
        :rtype: WebDriver element
        """
        try:
            element = self.driver.find_element_by_link_text(link_txt)
            return element
        except NoSuchElementException:
            return None

    def find_elements_by_link_text(self, link_txt):
        """
        finds the elements with the given link text

        :param link_txt: elements link text
        :type link_txt: str

        :returns: a list containing the WebDriver elements associated with the given link text
        :rtype: list
        """
        try:
            element = self.driver.find_elements_by_link_text(link_txt)
            return element
        except NoSuchElementException:
            return None

    def select_element_by_index(self, element, index):
        """
        selects an option from the provided element using a given index

        :param element: the element from which the item is to be selected
        :type element: WebDriver element

        :param index: the index of the item to be selected
        :type index: int

        """
        selector = Select(element)
        selector.select_by_index(index)

    def select_element_by_text(self, element, text):
        """
        selects an option from the provided element using a given text

        :param element: the element from which the item is to be selected
        :type element: WebDriver element

        :param text: the text to be selected
        :type text: str

        """
        selector = Select(element)
        selector.select_by_visible_text(text)

    def get_month_dict(self):
        """
        gets the month name to month number dictionary

        :returns: a dictionary mapping the month names to month numbers
        :rtype: dict
        """
        return self.month_dict

    def get_month_name_from(self, in_val):
        """

        :param in_val: month number
        :type in_val: int

        :returns: the month name
        :rtype: str

        """
        if in_val < 1 or in_val > 12:
            return ""

        for name, val in self.month_dict:
            if val == in_val:
                return name

        # default value, should not be reached logically if in_val is right
        return ""

    def get_month_val_from(self, name):
        """
        gets the month number from the input month name

        :param name: the name of the month
        :type name: str

        :returns: the month number
        :rtype: int
        """
        return self.month_dict.get(name)

    def click_button(self, btn):
        """
        clicks on the given button

        :param btn: The button to be clicked
        :type btn: WebDriver element

        """
        btn.click()

    def fill(self, txt_element, text):
        """
        the element to which the text is to be filled

        :param txt_element:
        :type txt_element: WebDriver element

        :param text: The text used to fill the text field
        :type text: str

        """
        txt_element.send_keys(text)

    def clear_txt(self, txt_element):
        """
        clears the given text field

        :param txt_element: The text field from which the text is to be cleared
        :type txt_element: WebDriver element

        """
        txt_element.clear()

    def click_button_safe(self, btn):
        """
        safely clicks on the given button without causing a crash

        :param btn: The button to be clicked
        :type btn: WebDriver element

        """
        if btn is None:
            return
        btn.click()

    def fill_safe(self, txt_element, text):
        """
        safely fills the provided text field with the given text without causing a crash

        :param txt_element: the element to which the text is to be filled
        :type txt_element: WebDriver element

        :param text: the text used to fill the text field
        :type text: str

        """
        if txt_element is None:
            return
        txt_element.send_keys(text)

    def clear_txt_safe(self, txt_element):
        """
        safely clears the given text field without causing a crash

        :param txt_element: the element from which the text is to be cleared
        :type txt_element: WebDriver element

        """
        if txt_element is None:
            return
        txt_element.clear()

    def screenshot(self, driver):
        """
        takes a screenshot of the website using the given driver

        :param driver: the driver used to take the screenshot from
        :type driver: WebDriver

        :returns: image screenshot
        :rtype: png image

        """
        return driver.get_screenshot_as_png()

    def report_allure(self, msg, driver=None):
        """"
        attaches a screenshot to allure's report

        If the argument `driver` is not passed in, the class' driver is used

        :param msg: the message used to be attached with the screenshot
        :type msg: str

        :param driver: the driver used to take a screenshot from (default is None)
        :type driver: WebDriver

        """
        if driver is None:
            driver = self.driver
        allure.attach(self.screenshot(driver), msg,
                      attachment_type=AttachmentType.PNG)


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
        if int(dob[1]) == self.day and int(dob[0]) == self.month and int(dob[2]) == self.year:
            return True
        return False


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
        return self.test_accounts_to_profiles.get(email).password

    def get_dob(self, email):
        return self.test_accounts_to_profiles.get(email).dob

    def get_name(self, email):
        return self.test_accounts_to_profiles.get(email).name

    def get_profile(self, email):
        return self.test_accounts_to_profiles.get(email)

    def get_registered_emails(self):
        return ["mohdos_1999@hotmail.com"]


class by(enum.Enum):
    ID = 1
    XPATH = 2
    CLASS_NAME = 3
    LINK_TEXT = 4


class Gender(enum.Enum):
    MALE = "Male"
    UNSELECTED = "Un selected"
    FEMALE = "Female"
