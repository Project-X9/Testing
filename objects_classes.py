
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helperClasses import helper, by, Gender
import time

# Testing email: test_projectX@hotmail.com
# Testing pass: TestingTeamMKE

class LoggedOutHome:

    def __init__(self, driver):
        # tb refers to Toolbar, tb_.. refers to Toolbar elements
        self.tb_login_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[6]/a")
        self.tb_signup_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[5]/a")
        self.tb_download_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[3]/a")
        self.tb_help_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[2]/a")
        self.tb_premium_btn = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/nav/ul/li[1]/a")
        # self.tb_logo = driver.find_element_by_xpath("/html/body/div[2]/div/header/div/div[1]/a/span/svg/g/path")
        self.getspotify_btn = driver.find_element_by_id("generic-btn-premium")
        self.fb_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[3]/a/span")
        self.twitter_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[2]/a/span")
        self.instagram_btn = driver.find_element_by_xpath("/html/body/div[3]/footer/nav/div[3]/ul/li[1]/a/span")
        self.subheading = driver.find_element_by_xpath("//h4[text()='Millions of songs. No credit card needed.']")
        self.heading = driver.find_element_by_xpath("//h1[text()='Music for everyone.']")
        self.for_artists_btn = driver.find_element_by_xpath("//a[text()='For Artists']")

    def getButtons(self):

        btns_arr = [self.tb_download_btn, self.tb_help_btn,
                    self.tb_login_btn,
                    self.tb_signup_btn, self.tb_premium_btn,
                    self.getspotify_btn]
        return btns_arr


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.helper = helper()
        # self.logo = driver.find_element_by_xpath("//*[@id='app']/body/div[1]/div[1]/div/a")
        self.fb_btn = self.helper.find_element_by_xpath(self.driver, "//*[@id='app']/body/div[1]/div[2]/div/div[2]/div/a")
        self.email_txt = self.helper.find_element_by_id(self.driver, "login-username")
        self.pass_txt = self.helper.find_element_by_id(self.driver, "login-password")
        self.remember_me_check = self.helper.find_element_by_xpath(self.driver, "//*[@id='app']/body/div[1]/div[2]/div/form/div[3]/div[1]/div/label/span")
        self.login_btn = self.helper.find_element_by_id(self.driver, "login-button")
        self.forgot_pass_btn = self.helper.find_element_by_xpath(self.driver, "//*[@id='reset-password-link']")
        self.signup_btn = self.helper.find_element_by_id(self.driver, "sign-up-link")
        self.disclaimer_txt = self.helper.find_element_by_xpath(self.driver, "//*[@id='app']/body/div[1]/div[2]/div/div[7]/div/p")
        self.terms_cond_btn = self.helper.find_element_by_xpath(self.driver, "//*[@id='app']/body/div[1]/div[2]/div/div[7]/div/p/a[1]")
        self.privacy_policy_btn = self.helper.find_element_by_xpath(self.driver, "//*[@id='app']/body/div[1]/div[2]/div/div[7]/div/p/a[2]")
        self.subheading = self.helper.find_element_by_xpath(self.driver, "//span[text()='To continue, log in to Spotify.']")
        self.no_account_text = self.helper.find_element_by_xpath(self.driver, "//*[@id='sign-up-section']/div/div/signup/div/div/div[2]/div")
        # self.incorrect_credentials_txt = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/p")
        self.account_overview_elements = None

    def initialize_account_overview(self):
        # el_exists = helper().element_exists_by_xpath(self.driver, "ProfileSection__valueCell--1fz0K")
        # if not el_exists:
        #     return False
        try:
            self.account_overview_elements = self.driver.find_elements_by_class_name("ProfileSection__valueCell--1fz0K")
            return True
        except:
            return False
        # self.account_overview_email = self.driver.find_element_by_link_text("/eg-en/account/overview/")

    def get_account_overview_email(self):
        account_overview_email = self.account_overview_elements[1].text
        return account_overview_email

    def set_email(self, email):
        self.email_txt.send_keys(email)

    def set_password(self, password):
        self.pass_txt.send_keys(password)

    def clear_credentials(self):
        self.email_txt.clear()
        self.pass_txt.clear()

    def set_credentials(self, email, password):
        self.set_email(email)
        self.set_password(password)

    def click_remember_me(self):
        self.remember_me_check.click()

    def click_login(self):
        self.login_btn.click()

    def click_forget_password(self):
        self.forgot_pass_btn.click()

    def click_sign_up(self):
        self.signup_btn.click()

    def click_terms_conditions(self):
        self.terms_cond_btn.click()

    def click_privacy_policy(self):
        self.privacy_policy_btn.click()

    def check_login_failure(self):
        if self.driver.title == "Login - Spotify":
            assert True
        else:
            assert False

    def is_correct_email(self, email):
        if self.get_account_overview_email() == email:
            return True
        else:
            return False

    def check_login_page(self):
        if self.driver.title == "Login - Spotify":
            assert True
        else:
            assert False

    def login_to_spotify(self, email, password):
        # timeout for login
        timeout = 10
        try:
            self.clear_credentials() # clear email and password fields
            self.set_credentials(email, password) # set email and password fields
            self.click_login()

            time.sleep(timeout)

            # if incorrect_credentials exists
            my_helper = helper()
            incorrect_credentials_exist = my_helper.element_exists_by_xpath(self.driver, "/html/body/div[1]/div[2]/div/div[2]/div/p")
            # if logged in successfully
            if self.driver.title == "Account overview - Spotify":
                initialize_success = self.initialize_account_overview() # try to find overview elements such as email, password, etc
                print("Successfully logged in")

                # failed to find account overview elements but logged in successfully
                if not initialize_success:
                    print("Could not find Account overview elements")
                    return True

                # Account overview email is not the same as the provided login email but logged in successfully
                if self.get_account_overview_email() != email:
                    print("INTERNAL ERROR: Account overview email is not matching the login email: Login email = "
                          + email + ", Overview email = " + self.get_account_overview_email())

                else:
                    print("SUCCESS: Account overview email is the same as the provided login email")

                return True

            # if incorrect_credentials text exists
            elif incorrect_credentials_exist:
                return False

            # if timeout without any page loaded
            else:
                print("Login timed out")
                return False

        # any other error that cause test to fail
        except:
            exit('Testing failed in login with credentials : ' + email + " & " + password)




class SignupPage():

    def __init__(self, driver):
        self.driver = driver
        self.helper = helper()
        self.signup_with_facebook = self.helper.find_element_by_id(self.driver, "select-button-signup-fb")
        self.email_txt = self.helper.find_element_by_id(self.driver, "register-email")
        self.confirm_email_txt = self.helper.find_element_by_id(self.driver, "register-confirm-email")
        self.password_txt = self.helper.find_element_by_id(self.driver, "register-password")
        self.display_name_txt = self.helper.find_element_by_id(self.driver, "register-displayname")
        self.dob_day_txt = self.helper.find_element_by_id(self.driver, "register-dob-day")
        self.dob_month_txt = self.helper.find_element_by_id(self.driver, "register-dob-month")
        self.dob_year_txt = self.helper.find_element_by_id(self.driver, "register-dob-year")
        self.gender_male = self.helper.find_element_by_id(self.driver, "register-male")
        self.gender_female = self.helper.find_element_by_id(self.driver, "register-female")
        self.terms_and_conditions = self.helper.find_element_by_link_text(self.driver, "Terms and Conditions of Use")
        self.privacy_policy = self.helper.find_element_by_link_text(self.driver, "Privacy Policy")
        self.signup = self.helper.find_element_by_id(self.driver, "register-button-email-submit")
        self.login = self.helper.find_element_by_id(self.driver, "register-link-login")

    def check_signup_page(self):
        return self.driver.title == "Sign up - Spotify"

    def select_month_by_text(self, month):
        self.helper.select_element_by_text(self.dob_month_txt, month)

    def select_month_by_index(self, m_index):
        self.helper.select_element_by_index(self.dob_month_txt, m_index)

    def set_email(self, email):
        self.email_txt.send_keys(email)

    def set_confirm_email(self, email):
        self.confirm_email_txt.send_keys(email)

    def set_password(self, password):
        self.password_txt.send_keys(password)

    def clear_credentials(self):
        self.email_txt.clear()
        self.confirm_email_txt.clear()
        self.password_txt.clear()

    def set_dob(self, dob):
        if 1 <= dob.day <= 31:
            self.dob_day_txt.send_keys(dob.day)
        if 1 <= dob.month <= 12:
            self.select_month_by_index(dob.month)
        if 1900 < dob.year <= 2020:
            self.dob_year_txt.send_keys(dob.year)

    def set_credentials(self, email, conf_email, password):
        self.set_email(email)
        self.set_confirm_email(conf_email)
        self.set_password(password)

    def select_gender(self, gender):
        if gender == Gender.MALE:
            self.gender_male.click()
        elif gender == Gender.FEMALE:
            self.gender_female.click()

    def click_signup(self):
        self.signup.click()

    def initialize_account_overview(self):
        try:
            self.account_overview_elements = self.driver.find_elements_by_class_name("ProfileSection__valueCell--1fz0K")
            return True
        except NoSuchElementException:
            return False

    def get_account_overview_email(self):
        account_overview_email = self.account_overview_elements[1].text
        return account_overview_email

    def signup_to_spotify(self, profile):
        timeout = 10
        try:
            self.set_credentials(profile.email, profile.c_email, profile.password)
            self.set_dob(profile.dob)
            self.select_gender(profile.gender)
            self.helper.fill(self.display_name_txt, profile.name)
            self.click_signup()
            time.sleep(timeout)

            # if signed up successfully
            if self.driver.title == "Account overview - Spotify":
                initialize_success = self.initialize_account_overview()  # try to find overview elements such as email, password, etc
                print("Successfully signed up")

                # failed to find account overview elements but logged in successfully
                if not initialize_success:
                    print("Could not find Account overview elements")
                    return True

                # Account overview email is not the same as the provided login email but logged in successfully
                if self.get_account_overview_email() != profile.email:
                    print("INTERNAL ERROR: Account overview email is not matching the login email: Login email = "
                          + profile.email + ", Overview email = " + self.get_account_overview_email())

                else:
                    print("SUCCESS: Account overview email is the same as the provided login email")

                return True

            # if incorrect_credentials text exists
            elif self.driver.title == "Sign up - Spotify":
                return False

            # if timeout without any page loaded
            else:
                print("Sign up timed out")
                return False

        # any other error that cause test to fail
        except:
            exit('Testing failed in login with credentials : ' + profile.email + " & " + profile.password)


