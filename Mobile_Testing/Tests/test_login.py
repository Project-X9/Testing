import allure
import pytest
from Mobile_Testing.Pages.LoggedOutHome import LoggedOutHome
from Mobile_Testing.helperClasses import MobileHelper
from Mobile_Testing.Pages.LoginPage import LoginPage


@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    driver = MobileHelper().driver_init()
    correct_emails = ["test1@test.com", "test2@test.com", "test3@test.com"]
    correct_passwords = ["test123", "test234", "test345"]

    @pytest.yield_fixture
    def setup(self):
        self.driver = MobileHelper().driver_init()
        yield
        self.driver.quit()

    # Test #1 ->Correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Passing login")
    @allure.sub_suite("Login with correct credentials")
    @allure.title("Login with correct credentials")
    @allure.description("Signing in with the following credentials email : test1@test.com & password: test123")
    @pytest.mark.Do
    @pytest.mark.Login
    def test_case_1(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[0], self.correct_passwords[0]):
            MobileHelper().report_allure(self.driver, "SUCCESS: Login succeeded with correct credentials")
            assert True
        else:
            MobileHelper().report_allure(self.driver, "ERROR: Login failed with correct credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[1], self.correct_passwords[1]):
            MobileHelper().report_allure(self.driver, "SUCCESS: Login succeeded with correct credentials")
            assert True
        else:
            MobileHelper().report_allure(self.driver, "ERROR: Login failed with correct credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify(self.correct_emails[2], self.correct_passwords[2]):
            MobileHelper().report_allure(self.driver, "SUCCESS: Login succeeded with correct credentials")
            assert True
        else:
            MobileHelper().report_allure(self.driver, "ERROR: Login failed with correct credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "wrong_password"):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with incorrect credentials")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with incorrect credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("kamelmohsenkamel", "Kimo2010"):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with incorrect credentials")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with incorrect credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("test_wrong@email.com", "UnknownPassowrd"):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with incorrect credentials")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with incorrect credentials")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("", "Kimo2010"):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with empty email")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with empty email")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("mohdos_1999@hotmail.com", ""):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with empty password")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with empty password")
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
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(1)
        lp = LoginPage(self.driver)
        if lp.login_to_spotify("", ""):
            MobileHelper().report_allure(self.driver, "ERROR: Login succeeded with empty email and password")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Login failed with empty email and password")
            assert True


