
"""
Home Page Testing

This script tests the home page that appears when logged out functions and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import time

import allure
import pytest
from Web_Testing.helperClasses import WebHelper
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from Web_Testing.helperClasses import ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Home")
@allure.feature("Home Page")
@allure.severity(allure.severity_level.BLOCKER)
class TestLoggedOutHome:

    driver = WebHelper().firefox_driver_init()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(WebHelper().get_home_url())
        self.driver.maximize_window()
        yield

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(WebHelper().get_home_url())
        self.driver.maximize_window()
        yield
        self.driver.close()

# Test #1 -> Signup button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Clicking Signup")
    @allure.title("Testing Sign up Button")
    @allure.description("Testing Sign up button")
    @pytest.mark.Do
    @pytest.mark.LoggedOutHome
    def test_case_1(self, setup):
        logged_out_home = LoggedOutHome(self.driver)
        logged_out_home.click_signup()
        time.sleep(2)
        sp = SignupPage(self.driver)
        if sp.check_signup_page():
            WebHelper().report_allure("Signup button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Signup button failed", self.driver)
            assert False

# Test #2 -> Testing Login Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Button")
    @allure.title("Testing Login Button")
    @allure.description("Testing Login Button")
    @pytest.mark.Do
    @pytest.mark.LoggedOutHome
    def test_case_2(self, setup):
        logged_out_home = LoggedOutHome(self.driver)
        logged_out_home.click_login()
        time.sleep(2)
        sp = LoginPage(self.driver)
        if sp.check_login_page():
            WebHelper().report_allure("Login button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Login button failed", self.driver)
            assert False

# Test #3 -> Testing Premium Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium Button")
    @allure.title("Testing Premium Button")
    @allure.description("Testing Premium Button")
    @pytest.mark.Do
    @pytest.mark.LoggedOutHome
    def test_case_3(self, setup_final):
        logged_out_home = LoggedOutHome(self.driver)
        logged_out_home.click_premium()
        time.sleep(2)
        if str(self.driver.current_url).find('premium') != -1:
            WebHelper().report_allure("Premium button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Premium button failed", self.driver)
            assert False
