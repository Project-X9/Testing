from selenium.common.exceptions import NoSuchElementException
import time
from Web_Testing.helperClasses import helper, Gender
from selenium.common.exceptions import NoSuchElementException


class SignupPage:

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
        timeout = 5
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
            exit('Testing failed in signing up with credentials : ' + profile.email + " & " + profile.password)

