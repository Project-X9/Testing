
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender, Profile
import time
from Mobile_Testing.helperClasses import MobileHelper

class LoggedOutHome(MobileHelper):

    def __init__(self, driver):
        self.driver = driver
        self.signup_btn = self.find_element_by_id(self.driver, "signUp_bt")
        self.login_btn = self.find_element_by_id(self.driver, "signIn_bt")
        self.login_with_facebook_btn = self.find_element_by_id(self.driver, "login_button")

    def click_signup(self):
        self.signup_btn.click()

    def is_open(self):
        if (self.signup_btn is None) or (self.login_btn is None):
            return False
        else:
            return True

    def click_login_with_facebook(self):
        self.login_with_facebook_btn.click()

    def click_login(self):
        self.login_btn.click()