from Mobile_Testing.helperClasses import MobileHelper
from Mobile_Testing.Pages.LoggedInHome import LoggedInHome


class LoginPage(MobileHelper):

    def __init__(self, driver):
        self.set_driver(driver)
        self.email_txt = self.find_element_by_id(self.driver, "email_et")
        self.pass_txt = self.find_element_by_id(self.driver, "password_et")
        self.login_btn = self.find_element_by_id(self.driver, "login_bt")
        self.forgot_pass_btn = None

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

    def click_login(self):
        self.login_btn.click()
        # self.login_btn.click()

    def click_forget_password(self):
        self.forgot_pass_btn.click()
        # self.forgot_pass_btn.click()

    def is_open(self):
        if (self.email_txt is None) or (self.login_btn is None):
            return False
        else:
            return True

    def is_logged_in(self):
        logged_in_page = LoggedInHome(self.driver)
        if logged_in_page.logout_btn is None:
            return False
        else:
            return True

    def login_to_spotify(self, email, password):
        # timeout for login
        timeout = 1
        try:
            self.clear_credentials() # clear email and password fields
            self.set_credentials(email, password) # set email and password fields
            self.click_login()

            self.driver.implicitly_wait(timeout)

            # if logged in successfully

            if self.is_logged_in():
                print("Successfully logged in")
                return True

            # if timeout without any page loaded
            else:
                return False

        # any other error that cause test to fail
        except:
            exit('Testing failed in login with credentials : ' + email + " & " + password)

