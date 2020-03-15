from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import pytest
from objects_classes import helper, LoginPage, SignupPage, LoggedOutHome
from helperClasses import Profile, DOB, Gender, ConstantsClass
import time


@allure.parent_suite("End to End testing")
@allure.suite("Login Tests")
@allure.feature("Log in Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver = helper().chrome_driver_init()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(ConstantsClass().get_home_link())
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(ConstantsClass().get_home_link())
        self.driver.maximize_window()
        yield
        self.driver.close()

# Test #1 -> Different Confirmation email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Login")
    @allure.sub_suite("Sign up with different confirmation email")
    @allure.title("Sign up with different confirmation email")
    @allure.description("Signing up with different confirmation email from the original email field")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_1(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        if not sp.check_signup_page():
            helper().report_allure(self.driver, "TIMEOUT: Sign up page not loading")
            assert False

        constants = ConstantsClass()
        emails = constants.get_test_emails()
        profile = Profile(emails[0], "test_pass", "Mohammad Osama", DOB(31, 1, 2002), Gender.MALE, "another_email@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with different confirmation email")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up unsuccessful with different confirmation email")
            assert True

# Test #2 -> Empty Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with empty email")
    @allure.title("Signup with empty email")
    @allure.description("Signing up with empty email")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_2(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("", "test_pass", "Mohammad Osama", DOB(31, 1, 1990), Gender.MALE,
                          "another_email@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with empty email")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with empty email")
            assert True

# Test #3 -> Already Registered Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing signup")
    @allure.sub_suite("Signup with already registered email")
    @allure.title("Signup with already registered email")
    @allure.description("Signing up with the following credentials email: test_projectX@hotmail.com")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_3(self, setup_final):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(3)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        constants = ConstantsClass()
        emails = constants.get_registered_emails()
        profile = Profile(emails[0], "test_pass", "Testing Team", DOB(31, 1, 1995), Gender.MALE)

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with registered email")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with already registered email")
            assert True

    # # Test #4 -> Success Sign up
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.story("Succes Signup")
    # @allure.sub_suite("Sign up with correct credentials and values")
    # @allure.title("Sign up with correct credentials and values")
    # @allure.description("Signing up with the following credentials and values:"
    #                     + ConstantsClass().get_profile("test_projectX@hotmail.com"))
    # @pytest.mark.Do
    # @pytest.mark.Signup
    # def test_case_4(self, setup_final):
    #     logged_out_page = LoggedOutHome(self.driver)
    #     logged_out_page.tb_signup_btn.click()
    #     time.sleep(3)
    #     sp = SignupPage(self.driver)
    #     sp.check_signup_page()
    #     constants = ConstantsClass()
    #     emails = constants.get_test_emails()
    #     profile = constants.get_profile(emails[0])
    #     if sp.signup_to_spotify(profile):
    #         helper().report_allure(self.driver, "SUCCESS: Sign up with correct credentials and values proceeded")
    #         assert True
    #     else:
    #         helper().report_allure(self.driver, "ERROR: Sign up did not proceed with correct credentials and values")
    #         assert False

# Test #5 -> Empty Password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with empty password")
    @allure.title("Signup with empty password")
    @allure.description("Signing up with empty password")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_5(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("mohdos_1999@hotmail.com", "", "Mohammad Osama", DOB(31, 1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with empty password")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with empty password")
            assert True

    # Test #6 -> Unselected gender
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with unselected gender")
    @allure.title("Signup with unselected gender")
    @allure.description("Signing up with unselected gender")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_6(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(31, 1, 1990), Gender.UNSELECTED,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected gender")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected gender")
            assert True

    # Test #7 -> unselected day
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with unselected day")
    @allure.title("Signup with unselected day")
    @allure.description("Signing up with unselected day")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_7(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(-1, 1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected day")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected day")
            assert True

    # Test #8 -> unselected month
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with unselected month")
    @allure.title("Signup with unselected month")
    @allure.description("Signing up with unselected month")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_8(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(1, -1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected month")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected month")
            assert True

    # Test #9 -> unselected year
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with unselected year")
    @allure.title("Signup with unselected year")
    @allure.description("Signing up with unselected year")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_9(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.tb_signup_btn.click()
        time.sleep(5)
        sp = SignupPage(self.driver)
        sp.check_signup_page()
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(1, 1, -1990), Gender.MALE)

        if sp.signup_to_spotify(profile):
            helper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected year")
            assert False
        else:
            helper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected year")
            assert True


