from appium import webdriver
from Mobile_Testing.helper import Helper, Constants
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
class TestSignup:
    """
       A class used to represent the Login page test
       ...
       Attributes
       ----------
       driver : webdriver
            A web driver element to control the android app
       my_factory : Faker
            An object that produces fake data
       name : string
            A randomly generated name
       email : string
            A randomly generated email
       password : string
            A randomly generated password
       Methods
       -------

       test_case_1()
            Signs up correctly
       test_case_2()
            Signs up with same email
       test_case_3()
            Signs up with no email
       test_case_4()
            Signs up with no name
       test_case_5()
            Signs up with no password
       test_case_6()
            Signs up with no age
       test_case_7()
            Signs up with female gender
       test_case_8()
            Signs up with wrong name format
       test_case_9()
            Signs up with wrong email format
       test_case_10()
            Signs up with -ve age
       test_case_11()
            Signs up with 0 age
       test_case_12()
            Signs up with 999 age
       """
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
        self.name = self.my_factory.name()
        self.email = self.my_factory.email()
        self.password = self.my_factory.password()
        yield
        self.driver.quit()

    # Test #1 ->Signing up correctly
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up correctly")
    @allure.title("Sign up correctly")
    @allure.description("Signing up with correct format with " + name + ","
                        + email + "," + password + ",22,M")
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
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False

    # Test #2 ->Signing up with already registered email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with existing email ")
    @allure.title("Signs up with existing email ")
    @allure.description("Signs up with same email format with " + name + ","
                        + Constants.correct_credentials["email"] + "," + Constants.correct_credentials["password"]+",22, M")
    @pytest.mark.Do
    @pytest.mark.Signup
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Signs up with existing email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signup_button()
        sp = SignupPage(self.driver)
        sp.do_the_signup(self.name, Constants.correct_credentials["email"], Constants.correct_credentials["password"], "22", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #3 ->Signing up with no email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no email ")
    @allure.title("Signs up with no email ")
    @allure.description("Signs up with no email format with " + name + ","
                        + " " + "," + password+",22, M")
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
        sp.do_the_signup(self.name, "", self.password, "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #4 ->Signing up with no name
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no name ")
    @allure.title("Signs up with no name ")
    @allure.description("Signs up with no name format with " + " " + ","
                        + email + "," + password+",22, M")
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
        sp.do_the_signup("", self.email, self.password, "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #5 ->Signing up with no password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no password ")
    @allure.title("Signs up with no password ")
    @allure.description("Signs up with no password format with " + name + ","
                        + email + "," + " "+",22, M")
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
        sp.do_the_signup(self.name, self.email, "", "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #6 ->Signing up with no age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with no age ")
    @allure.title("Signs up with no age ")
    @allure.description("Signs up with no age format with " + name + ","
                        + email + "," + password+"," ", M")
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
        sp.do_the_signup(self.name, self.email, self.password, "", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #7 ->Signing up with female gender
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with female gender ")
    @allure.title("Signs up with female gender ")
    @allure.description("Signs up with female gender format with " + name + ","
                        + email + "," + password+",21, F")
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
        sp.do_the_signup(self.name, self.email, self.password, "21", "F")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            Helper.report_allure(self.driver, "Sign up test Passed")
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
    @allure.description("Signs up with wrong name format with " + "@!@!#!@" + ","
                        + email + "," + password+",21, M")
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
        sp.do_the_signup("@!@#!@", self.email, self.password, "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

    # Test #9 ->Signing up with wrong email format
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with wrong email format")
    @allure.title("Signs up with wrong email format")
    @allure.description("Signs up with wrong email format with " + name + ","
                        + name + "," + password+",21, M")
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
        sp.do_the_signup(self.name, self.name, self.password, "21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

# Test #10 ->Signing up with -ve age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with -ve age ")
    @allure.title("Signs up with -ve age ")
    @allure.description("Signs up with -ve age with " + name + ","
                        + email + "," + password+",-21, M")
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
        sp.do_the_signup(self.name, self.email, self.password, "-21", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True


# Test #11 ->Signing up with 0 age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with 0 age ")
    @allure.title("Signs up with 0 age ")
    @allure.description("Signs up with 0 age with " + name + ","
                        + email + "," + password+",0, M")
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
        sp.do_the_signup(self.name, self.email, self.password, "0", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True

# Test #12 ->Signing up with 999 age
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Signup Tests")
    @allure.sub_suite("Sign up with 999 age ")
    @allure.title("Signs up with 999 age ")
    @allure.description("Signs up with 999 age with " + name + ","
                        + email + "," + password+",999, M")
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
        sp.do_the_signup(self.name, self.email, self.password, "999", "M")
        if Helper.element_exists_by_id(self.driver, HomePage.logout_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Sign up test Failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Sign up test Passed")
            assert True
