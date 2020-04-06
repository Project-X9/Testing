import allure
import pytest
from Mobile_Testing.Pages.SignupPage import SignupPage
from Mobile_Testing.helperClasses import MobileHelper, Profile, ConstantsClass, DOB, Gender
from Mobile_Testing.Pages.LoggedOutHome import LoggedOutHome
import time


@allure.parent_suite("End to End testing")
@allure.suite("Signup Tests")
@allure.feature("Signup Tests")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    # driver = helper().firefox_driver_init()
    # TODO: change Chrome executable path to your needs
    driver = MobileHelper().driver_init()
    correct_emails = ["test1@test.com", "test2@test.com", "test3@test.com"]
    correct_passwords = ["test123", "test234", "test345"]
    emails_different_confirmation = ["test4@test.com"]

    @pytest.yield_fixture
    def setup(self):
        self.driver = MobileHelper().driver_init()
        yield
        self.driver.quit()

# Test #1 -> Different Confirmation email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Sign up with different confirmation email")
    @allure.title("Sign up with different confirmation email")
    @allure.description("Signing up with different confirmation email from the original email field")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_1(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        if sp.signup_btn is None:
            MobileHelper().report_allure(self.driver, "TIMEOUT: Sign up page not loading")
            assert False

        constants = ConstantsClass()
        emails = constants.get_test_emails()
        profile = Profile(emails[0], "test_pass", "Mohammad Osama", DOB(31, 1, 2002), Gender.MALE, "another_email@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with different confirmation email")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up unsuccessful with different confirmation email")
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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("", "test_pass", "Mohammad Osama", DOB(31, 1, 1990), Gender.MALE,
                          "another_email@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with empty email")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with empty email")
            assert True

# # Test #3 -> Already Registered Email
#     @allure.severity(allure.severity_level.BLOCKER)
#     @allure.story("Failing signup")
#     @allure.sub_suite("Signup with already registered email")
#     @allure.title("Signup with already registered email")
#     @allure.description("Signing up with the following credentials email: test_projectX@hotmail.com")
#     @pytest.mark.Do
#     @pytest.mark.Signup
#     def test_case_3(self, setup):
#         logged_out_page = LoggedOutHome(self.driver)
#         logged_out_page.tb_signup_btn.click()
#         time.sleep(3)
#         sp = SignupPage(self.driver)
#         sp.check_signup_page()
#         constants = ConstantsClass()
#         # emails = constants.get_registered_emails()
#         profile = Profile(self.emails[0], "test_pass", "Testing Team", DOB(31, 1, 1995), Gender.MALE)
#
#         if sp.signup_to_spotify(profile):
#             MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with registered email")
#             assert False
#         else:
#             MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with already registered email")
#             assert True

    # Test #4 -> Success Sign up
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Succes Signup")
    @allure.sub_suite("Sign up with correct credentials and values")
    @allure.title("Sign up with correct credentials and values")
    @allure.description("Signing up with the following credentials and values -> Email: test1@test.com, Pass: test123")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_4(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_signup()
        time.sleep(3)
        sp = SignupPage(self.driver)
        constants = ConstantsClass()
        profile = constants.get_profile(self.correct_emails[0])
        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up with correct credentials and values proceeded")
            assert True
        else:
            MobileHelper().report_allure(self.driver, "ERROR: Sign up did not proceed with correct credentials and values")
            assert False

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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("mohdos_1999@hotmail.com", "", "Mohammad Osama", DOB(31, 1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with empty password")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with empty password")
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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(31, 1, 1990), Gender.UNSELECTED,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected gender")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected gender")
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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(-1, 1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected day")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected day")
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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(1, -1, 1990), Gender.MALE,
                          "mohdos_1999@hotmail.com")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected month")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected month")
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
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("mohdos_1999@hotmail.com", "test_pass", "Mohammad Osama", DOB(1, 1, -1990), Gender.MALE)

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with unselected year")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with unselected year")
            assert True

    # Test #10 -> Empty Confirmation Email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Failing Signup")
    @allure.sub_suite("Signup with empty confirmation email")
    @allure.title("Signup with empty confirmation email")
    @allure.description("Signing up with empty confirmation email")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_10(self, setup):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_signup()
        time.sleep(5)
        sp = SignupPage(self.driver)
        profile = Profile("test12@test.com", "test_pass", "Mohammad Osama", DOB(31, 1, 1990), Gender.MALE,
                          "")

        if sp.signup_to_spotify(profile):
            MobileHelper().report_allure(self.driver, "ERROR: Sign up proceeded with empty confirmation email")
            assert False
        else:
            MobileHelper().report_allure(self.driver, "SUCCESS: Sign up stopped with empty confirmation email")
            assert True
