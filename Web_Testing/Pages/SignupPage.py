
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
import time


class SignupPage(WebHelper):

    def __init__(self, driver):
        self.driver = driver
        self.signup_with_facebook = self.find_element_by_class_name("facebookButton metro")
        self.email_txt = self.find_element_by_id("email")
        self.confirm_email_txt = self.find_element_by_id("confirmemail")
        self.password_txt = self.find_element_by_id("password")
        self.display_name_txt = self.find_element_by_id("name")
        self.dob_day_txt = self.find_element_by_id("day")
        self.dob_month_txt = self.find_element_by_name("month")
        self.dob_year_txt = self.find_element_by_id("year")
        self.radio_btns = self.find_elements_by_id("sex")
        self.gender_male = self.radio_btns[0]
        self.gender_female = self.radio_btns[1]
        # self.terms_and_conditions = self.helper.find_element_by_link_text(self.driver, "Terms and Conditions of Use")
        # self.privacy_policy = self.helper.find_element_by_link_text(self.driver, "Privacy Policy")
        self.signup = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[7]/div/button")
        # self.login = self.helper.find_element_by_id(self.driver, "register-link-login")

    def check_signup_page(self):
        return self.url_has('signup')

    def select_month_by_text(self, month):
        self.select_element_by_text(self.dob_month_txt, month)

    def select_month_by_index(self, m_index):
        self.select_element_by_index(self.dob_month_txt, m_index)

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

    def clear_all(self):
        self.clear_credentials()
        self.dob_day_txt.clear()
        self.dob_year_txt.clear()
        self.display_name_txt.clear()

    def set_dob(self, dob):
        if 1 <= dob.day <= 31:
            self.dob_day_txt.send_keys(dob.day)
        if 1 <= dob.month <= 12:
            self.select_month_by_index(dob.month)
        if 1900 < dob.year <= 3048:
            self.dob_year_txt.send_keys(dob.year)

    def set_credentials(self, email, conf_email, password):
        self.set_email(email)
        self.set_confirm_email(conf_email)
        self.set_password(password)

    def select_gender(self, gender):
        if gender == Gender.MALE:
            self.click_button_safe(self.gender_male)
            # self.gender_male.click()
        elif gender == Gender.FEMALE:
            self.click_button_safe(self.gender_female)
            # self.gender_female.click()

    def click_signup(self):
        self.signup.click()

    def is_text_dangers_visible(self):
        try:
            text_dangers = self.find_elements_by_class_name('text-danger')
            return len(text_dangers) > 0
        except:
            return False

    def is_in_login_page(self):
        url = self.driver.current_url
        return ((len(url) >= 6 and url[-6:] == 'signin') or (len(url) >= 7 and url[-7:] == 'signin/'))

    def is_in_account_overview(self):
        url = self.driver.current_url
        return ((len(url) >= 8 and url[-8:] == 'overview') or (len(url) >= 9 and url[-9:] == 'overview/'))

    def signup_to_spotify(self, profile):
        timeout = 3
        try:
            self.clear_all()
            self.set_credentials(profile.email, profile.c_email, profile.password)
            self.set_dob(profile.dob)
            self.select_gender(profile.gender)
            self.fill(self.display_name_txt, profile.name)
            self.click_signup()
            time.sleep(3)
            if not self.is_in_login_page():
                print("Failed to signup")
                if not self.is_text_dangers_visible():
                    print("INTERNAL ERROR: Warnings did not appear")
                return False

            # TODO: remove driver refresh after correct implementation
            self.driver.refresh()
            time.sleep(2)

            lp = LoginPage(self.driver)
            lp.set_credentials(profile.email, profile.password)
            lp.click_login()
            time.sleep(3)
            account_overview = AccountOverviewPage(self.driver)
            time.sleep(timeout)

            print("Signed up successfully")

            # if signed up successfully
            if self.is_in_account_overview():
                # failed to find account overview elements but logged in successfully
                if account_overview.email is None:
                    print("Could not find Account overview elements")
                # Account overview email is not the same as the provided login email but logged in successfully
                elif account_overview.email != profile.email:
                    print("INTERNAL ERROR: Account overview email is not matching the signup/login email: Login email = "
                          + profile.email + ", Overview email = " + account_overview.email)
                else:
                    print("SUCCESS: Account overview email is the same as the provided login email")

                return True

            # if timeout without any page loaded
            else:
                print("INTERNAL ERROR: Unable to login after successful signup")
                return True

        # any other error that cause test to fail
        except:
            exit('Testing failed in signup with credentials : ' + profile.email + " & " + profile.password)
