from appium import webdriver
import pytest
from Mobile_Testing.helper import Helper
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.signup import SignupPage
from Mobile_Testing.Pages.login import LoginPage
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Authentication Testing")
@allure.feature("Authentication Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthentication:
    driver = None
    """
       A class used to represent the Authentication test
       ...
       Attributes
       ----------
       driver: webdriver
            A web driver element to control the android app

       Methods
       -------

       test_case_1()
             Clicks on the Sign up button and checks that it works
       test_case_2()
            Clicks on the Login button and checks that it works
       test_case_3()
            Checks that Facebook sign in button is available

       """


    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

        # Test #1 ->Clicks on the Sign up button and checks that it works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Authentication Tests")
    @allure.sub_suite("Sign up clicking")
    @allure.title("Sign up clicking")
    @allure.description("Clicking the sign up button")
    @pytest.mark.Do
    @pytest.mark.Authentication
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Clicks on the Sign up button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()

        if Helper.element_exists_by_id(self.driver, SignupPage.name_text_field_id):
            Helper.report_allure(self.driver, "Sign up Page entered")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up Page not entered")
            assert False

        # Test #2 ->Clicking the Login button

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Authentication Tests")
    @allure.sub_suite("Login clicking")
    @allure.title("Login clicking")
    @allure.description("Clicking the Login button")
    @pytest.mark.Do
    @pytest.mark.Authentication
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Clicks on the Login button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()

        if Helper.element_exists_by_id(self.driver, LoginPage.email_text_field_id):
            Helper.report_allure(self.driver, "Login Page  entered")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login Page not entered")
            assert False

    # Test #3 ->Checking the Facebook button is available

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Authentication Tests")
    @allure.sub_suite("Facebook Button Checking")
    @allure.title("Facebook Button Checking")
    @allure.description("Checking the Facebook button is available")
    @pytest.mark.Do
    @pytest.mark.Authentication
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Checks that Facebook sign in button is available
        """
        ap = AuthenticationPage(self.driver)
        if Helper.element_exists_by_id(self.driver, ap.login_with_facebook_button_id):
            Helper.report_allure(self.driver, "Facebook Page available")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Facebook Page not available")
            assert False
