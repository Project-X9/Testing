from appium import webdriver
from Mobile_Testing.helper import Helper
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.signup import SignupPage
from Mobile_Testing.Pages.home import HomePage
from allure_commons.types import AttachmentType
import allure
import pytest


@allure.parent_suite("End to End testing - Android")
@allure.suite("Signup Testing")
@allure.feature("Signup Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthentication:
    driver = None

    @pytest.yield_fixture
    def setup(self):
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

    # Test #1 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up correctly")
    @allure.title("Sign up correctly")
    @allure.description("Signing up with correct format with Kamel, kamelmohsenkamel@gmail.com, Kimo2010, 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_1(self, setup):
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("Kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up Failed")
            assert False



