"""
Home Page Testing

This script tests the Change Password page, its functions and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import time

import allure
import pytest

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.Pages.ChangePasswordPage import ChangePasswordPage
from Web_Testing.helperClasses import WebHelper
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.Pages.WebPlayerHome import WebPlayerHome
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from selenium import webdriver
from Web_Testing.helperClasses import ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Change Password Page")
@allure.feature("Change Password")
@allure.severity(allure.severity_level.BLOCKER)
class TestChangePassword:
    helper = WebHelper()
    driver = helper.firefox_driver_init()
    helper.set_driver(driver)

    email = "test14@test.com"
    new_password = "12345678"
    old_password = "test141516"

    @pytest.yield_fixture
    def setup_initial(self):
        self.driver.get(WebHelper().get_login_url())
        self.driver.maximize_window()
        yield

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(self.helper.get_account_overview_url())
        time.sleep(2)
        self.driver.get(self.helper.base_url + "account/changepassword")
        time.sleep(2)
        yield
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        yield
        self.driver.close()
        self.driver.stop_display()

    # Test #1 -> Change password with empty password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing change password with empty password")
    @allure.title("Change Password with empty password")
    @allure.description("Testing change password with empty password")
    @pytest.mark.Do
    @pytest.mark.ChangePassword
    def test_case_1(self, setup_initial):
        time.sleep(2)
        lp = LoginPage(self.driver)
        lp.login_to_spotify(self.email, self.old_password)
        # time.sleep(3)
        account_overview = AccountOverviewPage(self.driver)
        account_overview.click_change_password()
        time.sleep(2)
        change_password_page = ChangePasswordPage(self.driver)
        did_change_password = change_password_page.change_password("", self.new_password)
        text_dangers_appeared = not did_change_password

        if not text_dangers_appeared:
            self.helper.report_allure("ERROR: Text warnings did not appear with empty password", self.driver)
        else:
            self.helper.report_allure("SUCCESS: Text warnings appeared with empty password", self.driver)

        self.driver.get(self.helper.get_account_overview_url())
        time.sleep(2)
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_logout()
        time.sleep(3)
        self.driver.get(self.helper.get_login_url())
        time.sleep(2)
        login_page = LoginPage(self.driver)
        did_login_new = login_page.login_to_spotify(self.email, self.new_password)
        if did_login_new:
            self.helper.report_allure("ERROR: Changed password with empty password text")
        else:
            login_page.login_to_spotify(self.email, self.old_password)

        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_change_password()

        time.sleep(2)

        assert (not did_login_new)

    # Test #2 -> Change Password with empty confirmation password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Change Password with empty confirmation password")
    @allure.title("Change Password with empty confirmation password")
    @allure.description("Change Password with empty confirmation password")
    @pytest.mark.Do
    @pytest.mark.ChangePassowrd
    def test_case_2(self, setup):
        change_password_page = ChangePasswordPage(self.driver)
        did_change_password = change_password_page.change_password(self.new_password, "")
        text_dangers_appeared = not did_change_password

        if not text_dangers_appeared:
            self.helper.report_allure("ERROR: Text warnings did not appear with empty confirmation password",
                                      self.driver)
        else:
            self.helper.report_allure("SUCCESS: Text warnings appeared with empty confirmation password", self.driver)

        self.driver.get(self.helper.get_account_overview_url())
        time.sleep(2)
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_logout()
        time.sleep(3)
        self.driver.get(self.helper.get_login_url())
        time.sleep(2)
        login_page = LoginPage(self.driver)
        did_login_new = login_page.login_to_spotify(self.email, self.new_password)
        if did_login_new:
            self.helper.report_allure("ERROR: Changed password with empty confirmation password")
        else:
            login_page.login_to_spotify(self.email, self.old_password)

        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_change_password()

        time.sleep(2)

        assert (not did_login_new)

    # Test #3 -> Change Password with different confirmation password
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Change Password with different confirmation password")
    @allure.title("Change Password with different confirmation password")
    @allure.description("Change Password with different confirmation password")
    @pytest.mark.Do
    @pytest.mark.ChangePassowrd
    def test_case_3(self, setup):
        change_password_page = ChangePasswordPage(self.driver)
        did_change_password = change_password_page.change_password(self.new_password, self.new_password + "t")
        text_dangers_appeared = not did_change_password

        if not text_dangers_appeared:
            self.helper.report_allure("ERROR: Text warnings did not appear with different confirmation password",
                                      self.driver)
        else:
            self.helper.report_allure("SUCCESS: Text warnings appeared with different confirmation password",
                                      self.driver)

        self.driver.get(self.helper.get_account_overview_url())
        time.sleep(2)
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_logout()
        time.sleep(3)
        self.driver.get(self.helper.get_login_url())
        time.sleep(2)
        login_page = LoginPage(self.driver)
        did_login_new = login_page.login_to_spotify(self.email, self.new_password)
        if did_login_new:
            self.helper.report_allure("ERROR: Changed password with empty confirmation password")
        else:
            login_page = LoginPage(self.driver)
            login_page.set_credentials(self.email, self.old_password)
            login_page.click_login()
            time.sleep(3)

        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_change_password()

        assert (not did_login_new)

    # Test #4 -> Change Password with correct credentials
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Change Password with correct credentials")
    @allure.title("Change Password with correct credentials")
    @allure.description("Change Password with correct credentials")
    @pytest.mark.Do
    @pytest.mark.ChangePassowrd
    def test_case_4(self, setup_final):
        change_password_page = ChangePasswordPage(self.driver)
        did_change_password = change_password_page.change_password(self.new_password, self.new_password)
        text_dangers_appeared = not did_change_password

        if text_dangers_appeared:
            self.helper.report_allure("ERROR: Text warnings appeared with correct credentials", self.driver)
        else:
            self.helper.report_allure("SUCCESS: Text warnings did not appear with correct credentials", self.driver)

        self.driver.get(self.helper.get_account_overview_url())
        time.sleep(2)
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_logout()
        time.sleep(2)
        self.driver.get(self.helper.get_login_url())
        time.sleep(2)
        login_page = LoginPage(self.driver)
        did_login_new = login_page.login_to_spotify(self.email, self.new_password)
        if did_login_new:
            self.helper.report_allure("SUCCESS: Logged in with new password")

        assert did_login_new
