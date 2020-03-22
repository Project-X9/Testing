import time
from Web_Testing.helperClasses import helper
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
        self.email_txt = self.helper.find_element_by_id(self.driver, "login-username")
        self.pass_txt = self.helper.find_element_by_id(self.driver, "login-password")
        self.email_txt.clear()
        self.pass_txt.clear()

    def set_credentials(self, email, password):
        self.set_email(email)
        self.set_password(password)

    def click_remember_me(self):
        self.remember_me_check.click()

    def click_login(self):
        self.login_btn = self.helper.find_element_by_id(self.driver, "login-button")
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
            return True
        else:
            return False

    def is_correct_email(self, email):
        if self.get_account_overview_email() == email:
            return True
        else:
            return False

    def check_login_page(self):
        if self.driver.title == "Login - Spotify":
            return True
        else:
            return False

    def login_to_spotify(self, email, password):
        # timeout for login
        timeout = 5
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

