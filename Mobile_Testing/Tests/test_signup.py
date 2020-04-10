from appium import webdriver
from Mobile_Testing.helper import Helper
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.signup import SignupPage
from Mobile_Testing.Pages.home import HomePage
from faker import Faker
import time
from allure_commons.types import AttachmentType
import allure
import pytest


@allure.parent_suite("End to End testing - Android")
@allure.suite("Signup Testing")
@allure.feature("Signup Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthentication:
    driver = None
    my_factory = Faker()
    my_factory.random.seed(int(round(time.time() * 1000)))
    name = my_factory.name()
    email = my_factory.email()
    password = my_factory.password()


    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

    # Test #1 ->Signing up correctly
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up correctly")
    @allure.title("Sign up correctly")
    @allure.description("Signing up with correct format with " + name + ","
                        + email + "," + password+",22,M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Signs up correctly
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup(self.name, self.email, self.password, "22", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False

    # Test #2 ->Signing up with already registered email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with same email ")
    @allure.title("Signs up with same email ")
    @allure.description("Signs up with same email format with " + name + ","
                        + email + "," + password+",22, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Signs up with same email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup(self.name, self.email, self.password, "22", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True

    # Test #3 ->Signing up with no email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no email ")
    @allure.title("Signs up with no email ")
    @allure.description("Signs up with no email format with Kamel, "", Kimo2010, 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Signs up with no email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("Kamel", "", "Kimo2010", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True


    # Test #4 ->Signing up with no name
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no name ")
    @allure.title("Signs up with no name ")
    @allure.description("Signs up with no name format with "",kamelmohsenkamel@gmail.com , Kimo2010, 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Signs up with no name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("", "kamelmohsenkamel@gmail.com", "Kimo2010", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True


    # Test #5 ->Signing up with no name
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no password ")
    @allure.title("Signs up with no password ")
    @allure.description("Signs up with no password format with Kamel,kamelmohsenkamel@gmail.com , "", 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        Signs up with no password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("Kamel", "kamelmohsenkamel@gmail.com", "", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True


    # Test #6 ->Signing up with no age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no age ")
    @allure.title("Signs up with no age ")
    @allure.description("Signs up with no age format with Kamel,kamelmohsenkamel@gmail.com , Kimo2010, "", M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        Signs up with no age
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("Kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True


    # Test #7 ->Signing up with female gender
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with female gender ")
    @allure.title("Signs up with female gender ")
    @allure.description("Signs up with female gender format with Kamel,kamelmohsenkamel@gmail.com , Kimo2010, 21, F")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        Signs up with female gender
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("Kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "21", "F")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False


    # Test #8 ->Signing up with wrong name
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with wrong name format")
    @allure.title("Signs up with wrong name format")
    @allure.description("Signs up with wrong name format with @!@#!@,kamelmohsenkamel@gmail.com , Kimo2010, 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
        Signs up with wrong name format
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("@!@#!@", "kamelmohsenkamel@gmail.com", "Kimo2010", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True



    # Test #9 ->Signing up with wrong email format
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with wrong email format")
    @allure.title("Signs up with wrong email format")
    @allure.description("Signs up with wrong email format with kamel,kamelmohsenkamelgmail.com , Kimo2010, 21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test9
    def test_case_9(self, setup):
        """
        Signs up with wrong email format
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("kamel", "kamelmohsenkamelgmail.com", "Kimo2010", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True

# Test #10 ->Signing up with -ve age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with -ve age ")
    @allure.title("Signs up with -ve age ")
    @allure.description("Signs up with -ve age with kamel,kamelmohsenkamel@gmail.com , Kimo2010, -21, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test10
    def test_case_10(self, setup):
        """
        Signs up with -ve age
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "-21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True


# Test #11 ->Signing up with 0 age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with 0 age ")
    @allure.title("Signs up with 0 age ")
    @allure.description("Signs up with 0 age with kamel,kamelmohsenkamel@gmail.com , Kimo2010, 0, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test11
    def test_case_11(self, setup):
        """
        Signs up with 0 age
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "0", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True

# Test #12 ->Signing up with 999 age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with 999 age ")
    @allure.title("Signs up with 999 age ")
    @allure.description("Signs up with 999 age with kamel,kamelmohsenkamel@gmail.com , Kimo2010, 999, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test12
    def test_case_12(self, setup):
        """
        Signs up with 999 age
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup("kamel", "kamelmohsenkamel@gmail.com", "Kimo2010", "999", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            assert True