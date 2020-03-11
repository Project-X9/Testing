import sys
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from Pages.login import LoginPage
from helper import MY_PATH
sys.path.append(MY_PATH)


# These decorators help readability in allure reports
@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class Test:

    driver = webdriver.Chrome(ChromeDriverManager().install())

    @pytest.yield_fixture
    def setup(self):
        self.driver.get("https://accounts.spotify.com/en/login")
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("https://accounts.spotify.com/en/login")
        self.driver.maximize_window()
        yield
        self.driver.close()

# Test #1 ->Correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Passing login")
    @allure.sub_suite("Login with correct credentials")
    @allure.title("Login with correct credentials")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel@gmail.com & password: Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_1(self, setup):
        lp = LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "Kimo2010"):
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_screen_status_page", attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_screen_status_page", attachment_type=AttachmentType.PNG)
            assert False
# Test #2 ->Wrong Password

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with wrong password")
    @allure.title("Login with wrong password")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel@gmail.com & password: wrong password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_2(self, setup):
        lp = LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "wrong password"):
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_failed_login", attachment_type=AttachmentType.PNG)
            assert False
        else:
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_failed_login", attachment_type=AttachmentType.PNG)
            assert True

# Test #3 ->Wrong Email

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with wrong email")
    @allure.title("Login with wrong email")
    @allure.description("Signing in with the following credentials email : kamelmohsenkamel & password: Kimo2010")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_3(self, setup_final):
        lp = LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("kamelmohsenkamel", "Kimo2010"):
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_failed_login", attachment_type=AttachmentType.PNG)
            assert False
        else:
            allure.attach(self.driver.get_screenshot_as_png(), "test_login_failed_login", attachment_type=AttachmentType.PNG)
            assert True
