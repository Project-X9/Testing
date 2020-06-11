from appium import webdriver
import pytest
import time
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.profile import ProfilePage
from Mobile_Testing.Pages.premium import PremiumPage
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Profile Testing")
@allure.feature("Profile Testing")
@allure.severity(allure.severity_level.CRITICAL)
class TestProfile:
    """
         A class used to represent the Profile tests
         ...
         Attributes
         ----------
         driver: webdriver
              A web driver element to control the android app

         Methods
         -------


        test_case_1()
            checks the edit profile exists
        test_case_2()
            checks the first playlist exists
        test_case_3()
            checks the notifications checkbox is clickable
        test_case_4()
            checks change user name button
        test_case_5()
            checks change user password button
        test_case_6()
            checks change user email button
        test_case_7()
            changes the user name to correct name
        test_case_8()
            changes the user name to empty name
        test_case_9()
            changes the user name to !@!#@ name
        test_case_10()
            changes the user name to spaces name
        test_case_11()
            changes the user name to numbers name
        test_case_12()
            changes the user name to mixed name + characters name
        test_case_13()
            changes the user password to correct password
        test_case_14()
            changes the user password to empty password
        test_case_15()
            changes the user password to !@!#@ password
        test_case_16()
            changes the user password to spaces password
        test_case_17()
            changes the user email to correct email
        test_case_18()
            changes the user email to empty email
        test_case_19()
            changes the user email to !@!#@ email
        test_case_2()
            changes the user email to spaces email
        test_case_21()
            changes the user email to numbers email



         """

    driver = None

    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

        # Test #1 ->checks the edit profile exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks the edit profile exists")
    @allure.title("checks the edit profile exists")
    @allure.description("checks the edit profile exists")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        checks the edit profile exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed check edit profile")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.check_edit_profile_button():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed check edit profile")
            assert False

        # Test #2 ->checks the first playlist exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks the first playlist exists")
    @allure.title("checks the first playlist exists")
    @allure.description("checks the first playlist exists")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        checks the first playlist exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed check the first playlist exists")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()
        time.sleep(5)
        if pp.check_first_playlist():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed check the first playlist exists")
            assert False

        # Test #3 ->checks the first playlist exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks the notifications checkbox is clickable")
    @allure.title("checks the notifications checkbox is clickable")
    @allure.description("checks the notifications checkbox is clickable")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        checks the notifications checkbox is clickable
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check the notifications checkbox is clickable")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.check_notifications():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check the notifications checkbox is clickable")
            assert False

        # Test #4 ->checks change user name button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks change user name button")
    @allure.title("checks change user name button")
    @allure.description("checks change user name button")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        checks change user name button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change user name button")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.check_change_user_name_button():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change user name button")
            assert False

        # Test #5 ->checks change user password button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks change password button")
    @allure.title("checks change password button")
    @allure.description("checks change password button")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        checks change password button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change password button")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.check_change_user_password_button():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change password button")
            assert False

        # Test #6 ->checks change user email button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("checks change email button")
    @allure.title("checks change email button")
    @allure.description("checks change email button")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        checks change email button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change email button")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.check_change_user_email_button():
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to check change email button")
            assert False

        # Test #7 ->changes the user name to correct name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to correct name")
    @allure.title("changes the user name to correct name")
    @allure.description("changes the user name to correct name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        changes the user name to correct name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to correct name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.change_name("Abdallah George", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to correct name")
            assert False

        # Test #8 ->changes the user name to empty name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to empty name")
    @allure.title("changes the user name to empty name")
    @allure.description("changes the user name to empty name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
        changes the user name to empty name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to empty name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_name("", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_name("Abdallah George", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to empty name")
            assert False

        # Test #9 ->changes the user name to !@!#@ name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to !@!#@ name")
    @allure.title("changes the user name to !@!#@ name")
    @allure.description("changes the user name to !@!#@ name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test9
    def test_case_9(self, setup):
        """
        changes the user name to !@!#@ name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to !@!#@ name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_name("!@!#@", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_name("Abdallah George", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to !@!#@ name")
            assert False

        # Test #10 ->changes the user name to spaces name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to spaces name")
    @allure.title("changes the user name to spaces name")
    @allure.description("changes the user name to spaces name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test10
    def test_case_10(self, setup):
        """
        changes the user name to spaces name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to spaces name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_name("      ", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_name("Abdallah George", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to spaces name")
            assert False

        # Test #11 ->changes the user name to numbers name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to numbers name")
    @allure.title("changes the user name to numbers name")
    @allure.description("changes the user name to numbers name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test11
    def test_case_11(self, setup):
        """
        changes the user name to numbers name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to numbers name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_name("12345", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_name("Abdallah George", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to numbers name")
            assert False

        # Test #12 ->changes the user name to name + characters name
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user name to name + characters name")
    @allure.title("changes the user name to name + characters name")
    @allure.description("changes the user name to name + characters name")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test12
    def test_case_12(self, setup):
        """
        changes the user name to name + characters name
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user name to name + characters name")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_name("kamel12345_!@#!@$", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_name("Abdallah George", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test changes the user name to name + characters name")
            assert False

        # Test #13 ->changes the user password to correct password
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user password to correct password")
    @allure.title("changes the user password to correct password")
    @allure.description("changes the user password to correct password")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test13
    def test_case_13(self, setup):
        """
        changes the user password to correct password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to correct password")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.change_the_password("1234567", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to correct password")
            assert False

        # Test #14 ->changes the user password to empty password
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user password to empty password")
    @allure.title("changes the user password to empty password")
    @allure.description("changes the user password to empty password")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test14
    def test_case_14(self, setup):
        """
        changes the user password to empty password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to empty password")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_password("","or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_password("1234567", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to empty password")
            assert False

        # Test #15 ->changes the user password to !@!#@ password
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user password to !@!#@ password")
    @allure.title("changes the user password to !@!#@ password")
    @allure.description("changes the user password to !@!#@ password")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test15
    def test_case_15(self, setup):
        """
        changes the user password to !@!#@ password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to !@!#@ password")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_password("!@!#@", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_password("1234567", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to !@!#@ password")
            assert False

        # Test #16 ->changes the user password to spaces password
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user password to spaces password")
    @allure.title("changes the user password to spaces password")
    @allure.description("changes the user password to spaces password")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test16
    def test_case_16(self, setup):
        """
        changes the user password to spaces password
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to spaces password")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_password("    ", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_password("1234567", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user password to spaces password")
            assert False

        # Test #17 ->changes the user email to correct email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user email to correct email")
    @allure.title("changes the user email to correct email")
    @allure.description("changes the user email to correct email")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test17
    def test_case_17(self, setup):
        """
        changes the user email to correct email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to correct email")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if pp.change_the_email("abdallah@gmail.com", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to correct email")
            assert False

        # Test #18 ->changes the user email to empty email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user email to empty email")
    @allure.title("changes the user email to empty email")
    @allure.description("changes the user email to empty email")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test18
    def test_case_18(self, setup):
        """
        changes the user email to empty email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to empty email")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_email("", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_email("abdallah@gmail.com", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to empty email")
            assert False

        # Test #19 ->changes the user email to !@!#@  email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user email to !@!#@  email")
    @allure.title("changes the user email to !@!#@  email")
    @allure.description("changes the user email to !@!#@  email")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test19
    def test_case_19(self, setup):
        """
        changes the user email to !@!#@  email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to !@!#@  email")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_email("!@!#@ ","or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_email("abdallah@gmail.com", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to !@!#@  email")
            assert False

        # Test #20 ->changes the user email to spaces email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user email to spaces email")
    @allure.title("changes the user email to spaces email")
    @allure.description("changes the user email to spaces email")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test20
    def test_case_20(self, setup):
        """
        changes the user email to spaces email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to spaces email")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_email("      ", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_email("abdallah@gmail.com", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to spaces email")
            assert False

        # Test #21 ->changes the user email to numbers email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Profile Tests")
    @allure.sub_suite("changes the user email to numbers email")
    @allure.title("changes the user email to numbers email")
    @allure.description("changes the user email to numbers email")
    @pytest.mark.Do
    @pytest.mark.Profile
    @pytest.mark.Test21
    def test_case_21(self, setup):
        """
        changes the user email to numbers email
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()

        pp = PremiumPage(self.driver)
        if not pp.enter_profile():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to numbers email")
            assert False
        pp = ProfilePage(self.driver)
        pp.check_edit_profile_button()

        if not pp.change_the_email("1234567", "or"):
            Helper.report_allure(self.driver, "Passed")
            assert True
        else:
            pp.change_the_email("abdallah@gmail.com", "re")
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "failed to test change the user email to numbers email")
            assert False