from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import pytest
import objects_classes
import time

from helperClasses import helper, ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver = objects_classes.helper().chrome_driver_init()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get("https://www.spotify.com/eg-en/")
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("https://www.spotify.com/eg-en/")
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
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(5)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("test_projectX@hotmail.com", ConstantsClass().get_pass("test_projectX@hotmail.com")):
            helper().report_allure(self.driver, "SUCCESS: Login succeeded with correct credentials")
            assert True
        else:
            helper().report_allure(self.driver, "ERROR: Login failed with correct credentials")
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
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(5)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "wrong_password"):
            helper().report_allure(self.driver, "ERROR: Login succeeded with incorrect credentials")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Login failed with incorrect credentials")
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
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(3)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("kamelmohsenkamel", "Kimo2010"):
            helper().report_allure(self.driver, "ERROR: Login succeeded with incorrect credentials")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Login failed with incorrect credentials")
            assert True


# Test #4 ->Empty Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty email")
    @allure.title("Login with empty email")
    @allure.description("Signing in with empty email")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_4(self, setup_final):
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(3)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("", "Kimo2010"):
            helper().report_allure(self.driver, "ERROR: Login succeeded with empty email")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Login failed with empty email")
            assert True

    # Test #5 ->Empty Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty password")
    @allure.title("Login with empty password")
    @allure.description("Signing in with empty password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_5(self, setup_final):
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(3)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("mohdos_1999@hotmail.com", ""):
            helper().report_allure(self.driver, "ERROR: Login succeeded with empty password")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Login failed with empty password")
            assert True

    # Test #6 ->Empty Email and Password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing login")
    @allure.sub_suite("Login with empty email and password")
    @allure.title("Login with empty email and password")
    @allure.description("Signing in with empty email and password")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_6(self, setup_final):
        logged_out_page = objects_classes.LoggedOutHome(self.driver)
        logged_out_page.tb_login_btn.click()
        time.sleep(3)
        lp = objects_classes.LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("", ""):
            helper().report_allure(self.driver, "ERROR: Login succeeded with empty email and password")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Login failed with empty email and password")
            assert True


