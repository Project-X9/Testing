
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

    """
    A class used to represent the Login Page

    ...

    Attributes
    ----------
    signup_with_facebook : WebDriverElement
        a Web Driver element representing the Signup with Facebook button
    email_txt : WebDriverElement
        a Web Driver element representing the Email Text Field
    confirm_email_txt : WebDriverElement
        a Web Driver element representing the Confirm Email Text Field
    password_txt : WebDriverElement
        a Web Driver element representing the Password Text Field
    display_name_txt : WebDriverElement
        a Web Driver element representing the username Text Field
    dob_day_txt : WebDriverElement
        a Web Driver element representing birth date day Text Field
    dob_month_txt : WebDriverElement
        a Web Driver element representing birth month day Text Field
    dob_year_txt : WebDriverElement
        a Web Driver element representing birth year day Text Field
    radio_btns : WebDriverElement
        a Web Driver element representing the gender radio buttons
    gender_male : WebDriverElement
        a Web Driver element representing the male radio button
    gender_female : WebDriverElement
        a Web Driver element representing the female radio button
    signup : WebDriverElement
        a Web Driver element representing the Signup button
    login : WebDriverElement
        a Web Driver element representing the Login button

    Methods
    -------
    check_signup_page()
        Checks if currently in signup page
    select_month_by_text(month)
        selects the given month from the birth date month drop down
    select_month_by_index(m_index)
        selects the given index from the birth date month drop down
    set_email(email)
        Fills the email text field with the given email
    set_confirm_email(email)
        Fills the confirm email text field with the given email
    set_password(password)
        Fills the password text field with the given password
    clear_credentials()
        Clears the email, confirm email and password text fields
    clear_all()
        Clears all text fields in th page
    set_dob(dob)
        Fills the birth date day, month and year text fields
    set_credentials(email, conf_email, password)
        Set the email, confirm email and password text fields with the given email, conf_email and password
    select_gender(gender)
        Selects a gender radio button based on the given gender
    click_signup()
        Clicks on the signup button
    is_text_dangers_visible()
        Checks if any warning texts appeared/visible
    is_in_login_page()
        Checks if currently in login page
    is_in_account_overview()
        Checks if currently in Account Overview page
    click_login()
        Clicks on the login button
    signup_to_spotify(profile)
        sign up with the given user profile
    """

    def __init__(self, driver):
        """
        Initializes the page elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
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
        self.signup = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/form/div[7]/div/button")
        self.login = self.find_element_by_id("register-link-login")

    def check_signup_page(self):
        """
        Checks if currently in signup page

        :returns: a boolean if currently in signup page
        :rtype: bool
        """
        return self.url_has('signup')

    def select_month_by_text(self, month):
        """
        selects the given month from the birth date month drop down

        :param month: the month name
        :type month: str

        """
        self.select_element_by_text(self.dob_month_txt, month)

    def select_month_by_index(self, m_index):
        """
        selects the given index from the birth date month drop down

        :param m_index: the month number
        :type m_index: int

        """
        self.select_element_by_index(self.dob_month_txt, m_index)

    def set_email(self, email):
        """
        Fills the email text field with the given email

        :param email: the user's email
        :type email: str
        """
        self.email_txt.send_keys(email)

    def set_confirm_email(self, email):
        """
        Fills the confirm email text field with the given email

        :param email: the user's confirmation email
        :type email: str
        """
        self.confirm_email_txt.send_keys(email)

    def set_password(self, password):
        """
        Fills the password text field with the given password

        :param password: the user's password
        :type password: str
        """
        self.password_txt.send_keys(password)

    def clear_credentials(self):
        """
        Clears the email, confirm email and password text fields
        """
        self.email_txt.clear()
        self.confirm_email_txt.clear()
        self.password_txt.clear()

    def clear_all(self):
        """
        Clears all text fields in th page
        """
        self.clear_credentials()
        self.dob_day_txt.clear()
        self.dob_year_txt.clear()
        self.display_name_txt.clear()

    def set_dob(self, dob):
        """
        Fills the birth date day, month and year text fields

        :param dob: the dob object holding the birth date day, month and year
        :type dob: DOB
        """
        if 1 <= dob.day <= 31:
            self.dob_day_txt.send_keys(dob.day)
        if 1 <= dob.month <= 12:
            self.select_month_by_index(dob.month)
        if 1900 < dob.year <= 3048:
            self.dob_year_txt.send_keys(dob.year)

    def set_credentials(self, email, conf_email, password):
        """
        Set the email, confirm email and password text fields with the given email, conf_email and password

        :param email: the user's email
        :type email: str

        :param conf_email: the user's confirmation email
        :type conf_email: str

        :param password: the user's password
        :type password: str

        """
        self.set_email(email)
        self.set_confirm_email(conf_email)
        self.set_password(password)

    def select_gender(self, gender):
        """
        Selects a gender radio button based on the given gender

        :param gender: the user's gender
        :type gender: Gender

        """
        if gender == Gender.MALE:
            self.click_button_safe(self.gender_male)
        elif gender == Gender.FEMALE:
            self.click_button_safe(self.gender_female)

    def click_signup(self):
        """
        Clicks on the signup button
        """
        self.signup.click()

    def is_text_dangers_visible(self):
        """
        Checks if any warning texts appeared/visible

        :returns: a boolean True if the warnings appeared, False otherwise
        :rtype: bool

        """
        try:
            text_dangers = self.find_elements_by_class_name('text-danger')
            text_invalid = self.find_element_by_id("invalid")
            return ((text_dangers is not None) and (len(text_dangers) > 0)) or (text_invalid is not None)
        except:
            return False

    def is_in_login_page(self):
        """
        Checks if currently in login page

        :returns: a boolean if currently in login page
        :rtype: bool
        """
        url = self.driver.current_url
        return ((len(url) >= 6 and url[-6:] == 'signin') or (len(url) >= 7 and url[-7:] == 'signin/'))

    def is_in_account_overview(self):
        """
        Checks if currently in Account Overview page

        :returns: a boolean if currently in Account Overview page
        :rtype: bool
        """
        url = self.driver.current_url
        return ((len(url) >= 8 and url[-8:] == 'overview') or (len(url) >= 9 and url[-9:] == 'overview/'))

    def click_login(self):
        """
        Clicks on the login button
        """
        self.click_button_safe(self.login)

    def signup_to_spotify(self, profile):
        """
        sign up with the given user profile

        :param profile: the user's profile
        :type profile: Profile

        :returns: a boolean True if succeeded to signup, False otherwise
        :rtype: bool
        """
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
            account_overview.initialize_account_overview_elements()
            account_overview_email = account_overview.get_account_overview_email()
            time.sleep(timeout)

            account_overview.click_logout()

            print("Signed up successfully")

            # if signed up successfully
            if self.is_in_account_overview():
                # failed to find account overview elements but logged in successfully
                if account_overview_email is None:
                    print("Could not find Account overview elements")
                # Account overview email is not the same as the provided login email but logged in successfully
                elif account_overview_email != profile.email:
                    print("INTERNAL ERROR: Account overview email is not matching the signup/login email: Login email = "
                          + profile.email + ", Overview email = " + account_overview_email)
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
