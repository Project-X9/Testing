
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Web_Testing.helperClasses import WebHelper, by, Gender
import time


class LoginPage(WebHelper):

    def __init__(self, driver):
        self.set_driver(driver)
        self.fb_btn = self.find_elements_by_class_name("facebookButton metro")
        self.email_txt = self.find_element_by_id("email")
        self.pass_txt = self.find_element_by_id("password")
        # self.remember_me_check = self.driver.find_element_by_xpath("//*[@id='app']/body/div[1]/div[2]/div/form/div[3]/div[1]/div/label/span")
        self.login_btn = self.find_element_by_id("signinbutton")
        self.forgot_pass_btn = self.find_element_by_id("forgot-password-link")
        self.signup_btn = self.find_element_by_id("signuplink")
        self.incorrect_user_text = self.find_element_by_id("invalid")
        self.text_danger = self.find_elements_by_class_name("text-danger")
        self.account_overview_email = ""
        self.account_overview_username = ""
        # self.logo = driver.find_element_by_xpath("//*[@id='app']/body/div[1]/div[1]/div/a")

    def initialize_account_overview(self):
        # el_exists = helper().element_exists_by_xpath(self.driver, "ProfileSection__valueCell--1fz0K")
        # if not el_exists:
        #     return False
        try:
            usernames = self.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]")
            emails = self.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[2]")
            if (usernames is not None) and (len(usernames) > 0):
                self.account_overview_username = usernames[0].text
            if (emails is not None) and (len(emails) > 0):
                self.account_overview_email = emails[0].text
            return True
        except NoSuchElementException:
            return False
        # self.account_overview_email = self.driver.find_element_by_link_text("/eg-en/account/overview/")

    def get_account_overview_email(self):
        return self.account_overview_email

    def get_account_overview_username(self):
        return self.account_overview_username

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
        pass
        # self.helper.click_button_safe(self.remember_me_check)
        # self.remember_me_check.click()

    def click_login(self):
        self.click_button_safe(self.login_btn)
        # self.login_btn.click()

    def click_forget_password(self):
        self.click_button_safe(self.forgot_pass_btn)
        # self.forgot_pass_btn.click()

    def click_sign_up(self):
        self.click_button_safe(self.signup_btn)
        # self.signup_btn.click()

    def click_terms_conditions(self):
        pass
        # self.helper.click_button_safe(self.terms_cond_btn)
        # self.terms_cond_btn.click()

    def click_privacy_policy(self):
        pass
        # self.helper.click_button_safe(self.privacy_policy_btn)
        # self.privacy_policy_btn.click()

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

    def invalid_user_text_appeared(self):
        self.incorrect_user_text = self.find_element_by_id("invalid")
        if self.incorrect_user_text is None:
            return False
        else:
            return True

    def check_login_page(self):
        return self.url_has('signin')
        # url = str(self.driver.current_url)
        # result = url.find('signin')
        # if result == -1:
        #     return False
        # else:
        #     return True

    def is_in_account_overview(self):
        try:
            assertion = self.url_has("account/overview", self.driver)
            return assertion
        except:
            return False

    def login_to_spotify(self, email, password):
        # timeout for login
        timeout = 4
        try:
            self.clear_credentials() # clear email and password fields
            self.set_credentials(email, password) # set email and password fields
            self.click_login()

            time.sleep(timeout)
            # if logged in successfully
            if self.is_in_account_overview():
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

            # if timeout without any page loaded
            else:
                # if incorrect credentials did not appear, then there is a problem
                print("line 14")
                if self.invalid_user_text_appeared():
                    print("line 15")
                    print("Incorrect credentials.")
                else:
                    print(
                        "ERROR: 'Incorrect credentials' Warning did not appear. Probable cause: Signin button failure")

                return False

        # any other error that cause test to fail
        except:
            print("line 18")
            exit('Testing failed in login with credentials : ' + email + " & " + password)