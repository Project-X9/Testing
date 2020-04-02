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
    driver = WebHelper().chrome_driver_init()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get("http://localhost:3000/account/overview")
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("http://localhost:3000/account/overview")
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Test #1 ->Check all information in account overview page
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Check right information")
    @allure.title("Check right information")
    @allure.description("Check user information and signing in with the following credentials email : "
                        "test_projectX@hotmail.com & password: ")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_1(self, setup):
        #logged_out_page = LoggedOutHome(self.driver)
        #logged_out_page.tb_login_btn.click()
        #time.sleep(3)
        #lp = LoginPage(self.driver)
        #lp.set_email('test_projectX@hotmail.com')
        #lp.set_password(ConstantsClass().get_pass("test_projectX@hotmail.com"))
        # lp.set_credentials("test_projectX@hotmail.com", ConstantsClass().get_pass("test_projectX@hotmail.com"))
        #lp.click_login()
        account_overview_page = AccountOverviewPage(self.driver)
        #account_overview_page.click_profile()
        #account_overview_page.click_account()
        #time.sleep(3)

        if account_overview_page.account_overview_check("test_projectX@hotmail.com",
                                                        ConstantsClass().get_pass("test_projectX@hotmail.com"),
                                                        ConstantsClass().get_dob("test_projectX@hotmail.com"),
                                                        ConstantsClass().get_name("test_projectX@hotmail.com")):
            WebHelper().report_allure("SUCCESS: All information is correct", self.driver)
            assert True
        else:
            WebHelper().report_allure("ERROR: Incorrect information", self.driver)
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
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_profile()
        account_overview_page.click_account()
        if self.driver.current_url == "http://localhost:3000/accountoverview":
            assert True
        else:
            WebHelper().report_allure("Account link not functional", self.driver)
            assert False

    # Test #3 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking logout link")
    @allure.title("Clicking logout link")
    @allure.description("Clicking logout link")
    @pytest.mark.Do
    @pytest.mark.AccounOverview
    def test_case_3(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_profile()
        account_overview_page.click_logout()
        if self.driver.current_url == "http://localhost:3000/signin":
            assert True
        else:
            WebHelper().report_allure("Logout link not functional", self.driver)
            assert False

    # Test #4 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking Download link")
    @allure.title("Clicking Download link")
    @allure.description("Clicking Download link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_4(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_download_link()
        if self.driver.current_url == "http://localhost:3000/download":
            assert True
        else:
            WebHelper().report_allure("Download not functional", self.driver)
            assert False

    # Test #5 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking help link")
    @allure.title("Clicking help link")
    @allure.description("Clicking help link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_5(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_help_link()
        if self.driver.current_url == "http://localhost:3000/help":
            assert True
        else:
            WebHelper().report_allure("Help link not functional", self.driver)
            assert False

    # Test #6 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview Tests")
    @allure.sub_suite("Clicking premium link")
    @allure.title("Clicking premium link")
    @allure.description("Clicking premium link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_6(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_premium_link()
        if self.driver.current_url == "http://localhost:3000/premium":
            assert True
        else:
            WebHelper().report_allure("Premium link not functional", self.driver)
            assert False

    # Test #7 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking get premium link")
    @allure.title("Clicking get premium link")
    @allure.description("Clicking get premium link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_7(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_get_premium_btn()
        if self.driver.current_url == "http://localhost:3000/premium":
            assert True
        else:
            WebHelper().report_allure("Get premium button not functional", self.driver)
            assert False

    # Test #8 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking account overview link")
    @allure.title("Clicking account overview link")
    @allure.description("Clicking account overview link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_8(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_account_overview()
        if self.driver.current_url == "http://localhost:3000/accountoverview":
            assert True
        else:
            WebHelper().report_allure("Account Overview link not functional", self.driver)
            assert False

    # Test #9 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking change password link")
    @allure.title("Clicking change password link")
    @allure.description("Clicking change password link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_9(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_change_password()
        if self.driver.current_url == "http://localhost:3000/changepassword":
            assert True
        else:
            WebHelper().report_allure("change password link not functional", self.driver)
            assert False

    # Test #10 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking recover playlists link")
    @allure.title("Clicking recover playlists link")
    @allure.description("Clicking recover playlists link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_10(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_recover_playlists()
        if self.driver.current_url == "http://localhost:3000/reccoverplaylists":
            assert True
        else:
            WebHelper().report_allure("recover playlists link not functional", self.driver)
            assert False

    # Test #11 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking redeem link")
    @allure.title("Clicking redeem link")
    @allure.description("Clicking redeem link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_9(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_redeem_link()
        if self.driver.current_url == "http://localhost:3000/redeem":
            assert True
        else:
            WebHelper().report_allure("Redeem link not functional", self.driver)
            assert False

    # Test #12 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking join premium link")
    @allure.title("Clicking join premium link")
    @allure.description("Clicking join premium link")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_12(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_join_premium_btn()
        if self.driver.current_url == "http://localhost:3000/premium":
            assert True
        else:
            WebHelper().report_allure("change password link not functional", self.driver)
            assert False

    # Test #13 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Account Overview tests")
    @allure.sub_suite("Clicking edit profile button")
    @allure.title("Clicking edit profile button")
    @allure.description("Clicking edit profile button")
    @pytest.mark.Do
    @pytest.mark.AccountOverview
    def test_case_13(self, setup):
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_edit_profile_btn()
        if self.driver.current_url == "http://localhost:3000/editprofile":
            assert True
        else:
            WebHelper().report_allure("edit profile button not functional", self.driver)
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
        account_overview_page = AccountOverviewPage(self.driver)
        account_overview_page.click_signout_btn()
        if self.driver.current_url == "http://localhost:3000/signin":
            assert True
        else:
            WebHelper().report_allure("sign out button not functional", self.driver)
            assert False
