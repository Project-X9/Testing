
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.helperClasses import WebHelper, by, Gender
import time


class LoginPage(WebHelper):
    """
    A class used to represent the Login Page

    ...

    Attributes
    ----------
    fb_btn : WebDriverElement
        a Web Driver element representing the Login with Facebook button
    email_txt : WebDriverElement
        a Web Driver element representing the Email Text Field
    pass_txt : WebDriverElement
        a Web Driver element representing the Password Text Field
    login_btn : WebDriverElement
        a Web Driver element representing the Login button
    forgot_pass_btn : WebDriverElement
        a Web Driver element representing the Forgot Password button
    signup_btn : WebDriverElement
        a Web Driver element representing the Signup button
    text_danger : WebDriverElement
        a Web Driver element representing the Text Field warnings

    Methods
    -------
    set_email(email)
        Fills the email text field with the given email
    set_password(password)
        Fills the password text field with the given password
    clear_credentials()
        Clears the email and password text fields
    set_credentials(email, password)
        Set the email and password text fields with the given email and password
    click_signup()
        Clicks on the signup button
    click_login()
        Clicks on the login button
    invalid_user_text_appeared()
        Checks if the "Invalid username/password" text appeared
    check_login_page()
        Checks if currently on login page
    is_in_account_overview()
        Checks if currently on Account Overview page
    login_to_spotify(email, password)
        Login with the given email and password
    """

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.fb_btn = self.find_elements_by_class_name("facebookButton metro")
        self.email_txt = self.find_element_by_id("email")
        self.pass_txt = self.find_element_by_id("password")
        self.login_btn = self.find_element_by_id("signinbutton")
        self.forgot_pass_btn = self.find_element_by_id("forgot-password-link")
        self.signup_btn = self.find_element_by_id("signuplink")
        self.incorrect_user_text = self.find_element_by_id("invalid")
        self.text_danger = self.find_elements_by_class_name("text-danger")
        self.account_overview_email = ""
        self.account_overview_username = ""

    def set_email(self, email):
        """
        Fills the email text field with the given email

        :param email : The email to fill the text field with
        :type email: str

        """
        self.email_txt.send_keys(email)

    def set_password(self, password):
        """
        Fills the password text field with the given password

        :param password : The password to fill the text field with
        :type password: str
        """
        self.pass_txt.send_keys(password)

    def clear_credentials(self):
        """Clears the email and password text fields"""
        self.email_txt.clear()
        self.pass_txt.clear()

    def set_credentials(self, email, password):
        """
        Set the email and password text fields with the given email and password

        :param email : The email to fill the text field with
        :type email: str

        :param password : The password to fill the text field with
        :type password: str

        """
        self.set_email(email)
        self.set_password(password)

    def click_signup(self):
        """Clicks on the signup button"""
        self.click_button_safe(self.signup_btn)

    def click_login(self):
        """Clicks on the login button"""
        self.click_button_safe(self.login_btn)

    def invalid_user_text_appeared(self):
        """
        Checks if the "Invalid username/password" text appeared

        :returns: a boolean if the invalid user text has appeared
        :rtype: bool
        """
        self.incorrect_user_text = self.find_element_by_id("invalid")
        if self.incorrect_user_text is None:
            return False
        else:
            return True

    def check_login_page(self):
        """
        Checks if currently in login page

        :returns: a boolean if currently in login page
        :rtype: bool
        """
        return self.url_has('signin')

    def is_in_account_overview(self):
        """
        Checks if currently in Account Overview page

        :returns: a boolean if currently in account overview
        :rtype: bool
        """
        try:
            assertion = self.url_has("account/overview", self.driver)
            return assertion
        except:
            return False

    def login_to_spotify(self, email, password):
        """
        Login with the given email and password

        :param email : The email used for login
        :type email: str

        :param password : The password used for login
        :type password: str

        :returns: a boolean True if succeeded to login
        :rtype: bool

        :raises NoSuchElementException : If a Web Driver element cannot be found in the page
        """
        # timeout for login
        timeout = 4
        try:
            self.clear_credentials() # clear email and password fields
            self.set_credentials(email, password) # set email and password fields
            self.click_login()

            time.sleep(timeout)
            # if logged in successfully
            if self.is_in_account_overview():
                ap = AccountOverviewPage(self.driver)
                ap.initialize_account_overview_elements()
                initialize_success = ap.is_page_initialized()
                print("Successfully logged in")
                ap_email = ap.get_account_overview_email()

                # failed to find account overview elements but logged in successfully
                if not initialize_success:
                    print("Could not find Account overview elements")
                    return True
                # Account overview email is not the same as the provided login email but logged in successfully
                if ap_email != email:
                    print("INTERNAL ERROR: Account overview email is not matching the login email: Login email = "
                          + email + ", Overview email = " + ap_email)

                else:
                    print("SUCCESS: Account overview email is the same as the provided login email")

                return True

            # if timeout without any page loaded
            else:
                # if incorrect credentials did not appear, then there is a problem
                if self.invalid_user_text_appeared():
                    print("Incorrect credentials.")
                else:
                    print(
                        "ERROR: 'Incorrect credentials' Warning did not appear. Probable cause: Signin button failure")

                return False

        # any other error that cause test to fail
        except:
            return False

