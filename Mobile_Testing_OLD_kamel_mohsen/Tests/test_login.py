from appium import webdriver
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.home import HomePage
from allure_commons.types import AttachmentType
import allure
import pytest


@allure.parent_suite("End to End testing - Android")
@allure.suite("Login Testing")
@allure.feature("Login Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:
    """
       A class used to represent the Login page test
       ...
       Attributes
       ----------
       driver: webdriver
            A web driver element to control the android app

       Methods
       -------

       test_case_1()
            Login correctly
       test_case_2()
            Login with wrong email
       test_case_3()
            Login  with wrong email format
       test_case_4()
            Login  with no email
       test_case_5()
            Login  with wrong password
       test_case_6()
            Login  with no password
       test_case_7()
            Login  with no  password & email
       """
    driver = None

    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

    # Test #1 ->Logging in correctly
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login correctly")
    @allure.title("Login correctly")
    @allure.description("Logging in with correct format with " + Constants.correct_credentials["email"] + ", "
                        + Constants.correct_credentials["password"])
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Login correctly
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            Helper.report_allure(self.driver, "Login test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False

    # Test #2 ->Logging in with wrong email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with wrong email")
    @allure.title("Login with wrong email")
    @allure.description("Logging in with wrong email with kamelmohsenkamel99@gmail.com, Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Login with wrong email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("kamelmohsenkamel99@gmail.com", "Kimo2010")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True

    # Test #3 ->Logging in with wrong email format
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with wrong email format")
    @allure.title("Login with wrong email format")
    @allure.description("Logging in with wrong email format with kamelmohsenkamelgmail.com, Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Login  with wrong email format
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("kamelmohsenkamelgmail.com", "Kimo2010")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True

    # Test #4 ->Logging in with no email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with no email")
    @allure.title("Login with no email")
    @allure.description("Logging in with no email with "", Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Login  with no email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("", "Kimo2010")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True

    # Test #5 ->Logging in with wrong password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with wrong password")
    @allure.title("Login with wrong password")
    @allure.description("Logging in with wrong password with kamelmohsenkamel@gmail.com, !@#!@#1")
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        Login  with wrong password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("kamelmohsenkamel@gmail.com", "!@#!@#1")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True

    # Test #6 ->Logging in with no password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with no password")
    @allure.title("Login with no password")
    @allure.description("Logging in with no password with kamelmohsenkamel@gmail.com, ")
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        Login  with no password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("kamelmohsenkamel@gmail.com", "")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True

    # Test #7 ->Logging in with no  password & email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Tests")
    @allure.sub_suite("Login with no  password & email")
    @allure.title("Login with no  password & email")
    @allure.description("Logging in with no  password & email with "", """)
    @pytest.mark.Do
    @pytest.mark.Login
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        Login  with no  password & email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login("", "")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Login test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Login test passed")
            assert True
