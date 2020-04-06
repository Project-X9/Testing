import allure
import pytest
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from Web_Testing.Pages.LoginPage import LoginPage
import time
from Web_Testing.helperClasses import WebHelper


@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestSignin:

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver = WebHelper().firefox_driver_init()
    link = "http://localhost:3000/signin"
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
        if lp.login_to_spotify(self.correct_emails[0], self.correct_passwords[0]):
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
        if lp.login_to_spotify(self.correct_emails[1], self.correct_passwords[1]):
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
        if lp.login_to_spotify(self.correct_emails[2], self.correct_passwords[2]):
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
        if lp.login_to_spotify("kamelmohsenkamel@gmail.com", "wrong_password"):
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
        if lp.login_to_spotify("kamelmohsenkamel", "Kimo2010"):
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
        if lp.login_to_spotify("test_wrong@email.com", "UnknownPassowrd"):
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
        if lp.login_to_spotify("", "Kimo2010"):
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
        if lp.login_to_spotify("mohdos_1999@hotmail.com", ""):
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
    def test_case_9(self, setup_final):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.check_login_page()
        if lp.login_to_spotify("", ""):
            WebHelper().report_allure("ERROR: Login succeeded with empty email and password", self.driver)
            assert False
        else:
            WebHelper().report_allure("SUCCESS: Login failed with empty email and password", self.driver)
            assert True

