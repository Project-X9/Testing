"""
Account Overview Testing

This script tests the account overview page information and buttons and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import pytest
from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from Web_Testing.Pages.LoginPage import LoginPage
import time
from Web_Testing.helperClasses import WebHelper, ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Account Overview Tests")
@allure.feature("Account Overview Tests")
@allure.severity(allure.severity_level.CRITICAL)
class TestAccountOverview:
    exit_code = 0
    # TODO: change Firefox executable path to your needs
    helper = WebHelper()
    driver = helper.firefox_driver_init()
    account_overview_page = AccountOverviewPage(driver)

    def login_first(self):
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        self.driver.implicitly_wait(3)
        lp = LoginPage(self.driver)
        lp.login_to_spotify("test9@test.com", ConstantsClass().get_pass("test9@test.com"))

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(WebHelper().get_account_overview_url())
        self.driver.maximize_window()
        self.account_overview_page.click_account()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_check_information(self):
        self.driver.get(WebHelper().get_home_url())
        self.driver.maximize_window()
        self.login_first()
        time.sleep(2)
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(WebHelper().get_home_url())
        self.driver.maximize_window()
        logged_out_page = LoggedOutHome(self.driver)
        logged_out_page.click_login()
        yield
        self.driver.close()
        self.helper.stop_display()
        if self.self.exit_code == -1:
            exit(-1)

    # Test #1 ->Check all information in account overview page
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Check right information")
    @allure.title("Check right information")
    @allure.description("Check user information and signing in with the following credentials email : "
                        "test_projectX@hotmail.com & password: ")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_1(self, setup_check_information):
        self.account_overview_page.click_account()
        self.driver.implicitly_wait(3)
        if self.account_overview_page.account_overview_check("test9@test.com",
                                                             ConstantsClass().calculate_age("test9@test.com"),
                                                             ConstantsClass().get_name("test9@test.com"),
                                                             ConstantsClass().get_premium("test9@test.com")):
            WebHelper().report_allure("SUCCESS: All information is correct", self.driver)
            assert True
        else:
            WebHelper().report_allure("ERROR: Incorrect information", self.driver)
            self.exit_code = -1
            assert False

    # Test #2 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking account link")
    @allure.title("Clicking account link")
    @allure.description("Clicking account link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_2(self, setup):
        self.account_overview_page.click_account()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_overview_url():
            WebHelper().report_allure("Account link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Account link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #3 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking Download link")
    @allure.title("Clicking Download link")
    @allure.description("Clicking Download link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_3(self, setup):
        self.account_overview_page.click_download_link()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_home_url():
            WebHelper().report_allure("Download functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Download not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #4 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking help link")
    @allure.title("Clicking help link")
    @allure.description("Clicking help link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_4(self, setup):
        self.account_overview_page.click_help_link()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_home_url():
            WebHelper().report_allure("Help link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Help link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #5 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking premium link")
    @allure.title("Clicking premium link")
    @allure.description("Clicking premium link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_5(self, setup):
        self.account_overview_page.click_premium_link()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_premium_url():
            WebHelper().report_allure("Premium link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Premium link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #6 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking account overview link")
    @allure.title("Clicking account overview link")
    @allure.description("Clicking account overview link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_6(self, setup):
        self.account_overview_page.click_account_overview()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_overview_url():
            WebHelper().report_allure("Account Overview link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Account Overview link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #7 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking edit profile link")
    @allure.title("Clicking edit profile link")
    @allure.description("Clicking edit profile link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_7(self, setup):
        self.account_overview_page.click_edit_profile()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_edit_url():
            WebHelper().report_allure("Edit Profile link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Edit Profile link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #8 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking change password link")
    @allure.title("Clicking change password link")
    @allure.description("Clicking change password link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_8(self, setup):
        self.account_overview_page.click_change_password()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_changepassword_url():
            WebHelper().report_allure("Change Password link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Change Password link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #9 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking recover playlists link")
    @allure.title("Clicking recover playlists link")
    @allure.description("Clicking recover playlists link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_9(self, setup):
        self.account_overview_page.click_recover_playlists()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_overview_url():
            WebHelper().report_allure("Recover Playlists link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Recover Playlists link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #10 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking redeem link")
    @allure.title("Clicking redeem link")
    @allure.description("Clicking redeem link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_10(self, setup):
        self.account_overview_page.click_redeem_link()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_overview_url():
            WebHelper().report_allure("Redeem link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Redeem link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #11 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking join premium button")
    @allure.title("Clicking join premium button")
    @allure.description("Clicking join premium button")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_11(self, setup):
        if ConstantsClass().get_premium("test9@test.com") is False:
            self.account_overview_page.click_join_premium_btn()
            self.driver.implicitly_wait(3)
            if self.driver.current_url == WebHelper().get_premium_url():
                WebHelper().report_allure("join premium button functional", self.driver)
                assert True
            else:
                WebHelper().report_allure("join premium button not functional", self.driver)
                self.exit_code = -1
            assert False
        elif ConstantsClass().get_premium("test9@test.com") is True:
            WebHelper().report_allure("join premium doesn't exist as account is already premium", self.driver)
            assert True

    # Test #12 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking edit profile button")
    @allure.title("Clicking edit profile button")
    @allure.description("Clicking edit profile button")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_12(self, setup):
        self.account_overview_page.click_edit_profile_btn()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_account_edit_url():
            WebHelper().report_allure("edit profile button functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("edit profile button not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #13 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking logout link")
    @allure.title("Clicking logout link")
    @allure.description("Clicking logout link")
    @pytest.mark.Do
    @pytest.mark.AccounOverview
    def test_case_13(self, setup):
        self.account_overview_page.click_logout()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_signup_url():
            WebHelper().report_allure("Logout link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Logout link not functional", self.driver)
            self.exit_code = -1
            assert False

    # Test #14 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking sign out button")
    @allure.title("Clicking sign out button")
    @allure.description("Clicking sign out button")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_14(self, setup_final):
        self.account_overview_page.click_signout_btn()
        self.driver.implicitly_wait(3)
        if self.driver.current_url == WebHelper().get_login_url():
            WebHelper().report_allure("sign out button functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("sign out button not functional", self.driver)
            self.exit_code = -1
            assert False
