from appium import webdriver
from Mobile_Testing.helperClasses import MobileHelper
from Mobile_Testing.Pages.LoggedOutHome import LoggedOutHome
from Mobile_Testing.Pages.SignupPage import SignupPage
from allure_commons.types import AttachmentType
import allure
import pytest


@allure.parent_suite("End to End testing - Android")
@allure.suite("Authentication Testing")
@allure.feature("Authentication Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthentication:
    driver = None

    @pytest.yield_fixture
    def setup(self):
        self.driver = MobileHelper.driver_init()
        yield
        self.driver.quit()

    # Test #1 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Authentication Tests")
    @allure.sub_suite("Sign up clicking")
    @allure.title("Sign up clicking")
    @allure.description("Clicking the sign up button")
    @pytest.mark.Do
    @pytest.mark.Authentication
    def test_case_1(self, setup):
        ap = LoggedOutHome(self.driver)
        ap.click_signup()
        sp = SignupPage(self.driver)
        if sp.name_txt is not None:
            assert True
        else:
            print(self.driver.current_activity)
            MobileHelper.report_allure(self.driver, "Sign up Page not entered")
            assert False
