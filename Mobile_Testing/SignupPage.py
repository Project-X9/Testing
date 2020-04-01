
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import Gender, Profile
import time
from Mobile_Testing.helperClasses import MobileHelper
from Mobile_Testing.LoggedOutHome import LoggedOutHome
from Mobile_Testing.LoginPage import LoginPage

class SignupPage(MobileHelper):

    def __init__(self, driver):
        self.driver = driver
        self.name_txt = self.find_element_by_id(self.driver, "signUpName_et")
        self.email_txt = self.find_element_by_id(self.driver, "signUpEmail_et")
        self.password_txt = self.find_element_by_id(self.driver, "signUpPassword_et")
        self.male_gender_checkbox = self.find_element_by_id(self.driver, "signUpMale_rb")
        self.female_gender_checkbox = self.find_element_by_id(self.driver, "signUpFemale_rb")
        self.age_txt = self.find_element_by_id(self.driver, "signUpAge_et")
        self.signup_btn = self.find_element_by_id(self.driver, "createUser_bt")

    def fill_name(self, name):
        self.name_txt.send_keys(name)

    def fill_email(self, email):
        self.email_txt.send_keys(email)

    def fill_password(self, password):
        self.password_txt.send_keys(password)

    def fill_age(self, age):
        self.age_txt.send_keys(age)

    def choose_male(self):
        self.male_gender_checkbox.click()

    def choose_female(self):
        self.female_gender_checkbox.click()

    def click_signup(self):
        self.signup_btn.click()

    def is_open(self):
        if (self.email_txt is None) or (self.signup_btn is None):
            return False
        else:
            return True

    def signup_to_spotify(self, profile):
        self.fill_name(profile.name)
        self.fill_email(profile.email)
        self.fill_password(profile.password)
        self.fill_age(profile.dob)
        if profile.gender == Gender.MALE:
            self.choose_male()
        else:
            self.choose_female()

        self.click_signup()
        time.sleep(5)
        logged_out_home = LoggedOutHome(self.driver)

        # check if any element is None which means that the page is not open
        if logged_out_home.login_btn is None:
            return False
        logged_out_home.click_login()

        time.sleep(5)
        login_page = LoginPage(self.driver)

        # check if any element is None which means that the page is not open
        if login_page.login_btn is None:
            return False

        did_login = login_page.login_to_spotify(profile.email, profile.password)
        time.sleep(5)
        # did login successfully
        if did_login:
            return True
        else:
            return False



