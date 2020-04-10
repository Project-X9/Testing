
"""
Login Testing

This script tests the login functions and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""


import allure
import pytest

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from Web_Testing.Pages.LoginPage import LoginPage
import time
from Web_Testing.helperClasses import WebHelper

@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    driver = WebHelper().firefox_driver_init()
    link = WebHelper().get_login_url()
    correct_emails = ["test1@test.com", "test2@test.com", "test3@test.com"]
    correct_passwords = ["test123", "test234", "test345"]

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(self.link)
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(self.link)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Test #1 ->Correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Passing login")
    @allure.sub_suite("Login with correct credentials")
    @allure.title("Login with correct credentials")
    @allure.description("Signing in with the following credentials email : test1@test.com & password: test123")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_1(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[0], self.correct_passwords[0]):
            ap.click_logout()
            WebHelper().report_allure("SUCCESS: Login succeeded with correct credentials", self.driver)
            assert True
        else:
            WebHelper().report_allure("ERROR: Login failed with correct credentials", self.driver)
            assert False

    # Test #2 ->Correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Passing login")
    @allure.sub_suite("Login with correct credentials")
    @allure.title("Login with correct credentials")
    @allure.description("Signing in with the following credentials email : test1@test.com & password: test123")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_2(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[1], self.correct_passwords[1]):
            ap.click_logout()
            WebHelper().report_allure("SUCCESS: Login succeeded with correct credentials", self.driver)
            assert True
        else:
            WebHelper().report_allure("ERROR: Login failed with correct credentials", self.driver)
            assert False

    # Test #3 ->Correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Passing login")
    @allure.sub_suite("Login with correct credentials")
    @allure.title("Login with correct credentials")
    @allure.description("Signing in with the following credentials email : test1@test.com & password: test123")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_3(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[2], self.correct_passwords[2]):
            ap.click_logout()
            WebHelper().report_allure("SUCCESS: Login succeeded with correct credentials", self.driver)
            assert True
        else:
            WebHelper().report_allure("ERROR: Login failed with correct credentials", self.driver)
            assert False

    # Test #4 ->Wrong Password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with wrong password")
    @allure.title("Login with wrong password")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel@gmail.com & password: wrong password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_4(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "wrong_password"):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with incorrect credentials", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with incorrect credentials", self.driver)
            assert True

    # Test #5 ->Wrong Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with wrong email")
    @allure.title("Login with wrong email")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel & password: Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_5(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("kamelmohsenkamel", "Kimo2010"):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with incorrect credentials", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with incorrect credentials", self.driver)
            assert True

    # Test #6 ->Wrong Email and password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with wrong email")
    @allure.title("Login with wrong email")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel & password: Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_6(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("test_wrong@email.com", "UnknownPassowrd"):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with incorrect credentials", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with incorrect credentials", self.driver)
            assert True

    # Test #7 ->Empty Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty email")
    @allure.title("Login with empty email")
    @allure.description("Signing in with empty email")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_7(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("", "Kimo2010"):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with empty email", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with empty email", self.driver)
            assert True

    # Test #8 ->Empty Password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty password")
    @allure.title("Login with empty password")
    @allure.description("Signing in with empty password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_8(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("mohdos_1999@hotmail.com", ""):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with empty password", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with empty password", self.driver)
            assert True

    # Test #9 ->Empty Email and Password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty email and password")
    @allure.title("Login with empty email and password")
    @allure.description("Signing in with empty email and password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_9(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        ap = AccountOverviewPage(self.driver)
        if lp.login_to_spotify("", ""):
            ap.click_logout()
            WebHelper().report_allure("ERROR: Login succeeded with empty email and password", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with empty email and password", self.driver)
            assert True

    # Test #10 -> Testing Refresh
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Refresh Page test")
    @allure.sub_suite("Refresh Page test")
    @allure.title("Refresh Page test")
    @allure.description("Testing to refresh page that elements are still available")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_10(self, setup_final):
        time.sleep(2)
        self.driver.refresh()
        lp = LoginPage(self.driver)

        if (lp.email_txt is None) or (lp.pass_txt is None) or (lp.login_btn is None):
            WebHelper().report_allure("ERROR: Elements are not available after refresh", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Elements are available after refresh", self.driver)
            assert True


