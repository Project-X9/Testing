
"""
Premium page Testing

This script tests the premium page buttons and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import pytest
from Web_Testing.Pages.premium import PremiumPage
import time
from Web_Testing.helperClasses import WebHelper, ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Premium page test")
@allure.feature("Premium page test")
@allure.severity(allure.severity_level.CRITICAL)
class TestPremium:
    # TODO: change Firefox executable path to your needs
    driver = WebHelper().chrome_driver_init()
    pp = PremiumPage(driver)

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(WebHelper().get_premium_url())
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(WebHelper().get_premium_url())
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Test #1 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Spotify logo")
    @allure.title("Spotify logo")
    @allure.description("Spotify logo")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_1(self, setup):
        self.pp.click_spotify_logo()
        if self.driver.current_url == WebHelper().get_signup_url():
            WebHelper().report_allure("Spotify logo functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Spotify logo not functional", self.driver)
            assert False

    # Test #2 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking account link")
    @allure.title("Clicking account link")
    @allure.description("Clicking account link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_2(self, setup):
        self.pp.click_account()
        if self.driver.current_url == WebHelper().get_account_overview_url():
            WebHelper().report_allure("Account link functional", self.driver)

            assert True
        else:
            WebHelper().report_allure("Account link not functional", self.driver)
            assert False

    # Test #3 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking Download link")
    @allure.title("Clicking Download link")
    @allure.description("Clicking Download link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_3(self, setup):
        self.pp.click_download_link()
        if self.driver.current_url == WebHelper().get_home_url():
            WebHelper().report_allure("Download link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Download link not functional", self.driver)
            assert False

    # Test #4 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking help link")
    @allure.title("Clicking help link")
    @allure.description("Clicking help link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_4(self, setup):
        self.pp.click_help_link()
        if self.driver.current_url == WebHelper().get_home_url():
            WebHelper().report_allure("Help link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Help link not functional", self.driver)
            assert False

    # Test #5 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking home link")
    @allure.title("Clicking home link")
    @allure.description("Clicking home link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_5(self, setup):
        self.pp.click_home_link()
        if self.driver.current_url == WebHelper().get_home_url():
            WebHelper().report_allure("Home link functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Home link not functional", self.driver)
            assert False

    # Test #6 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking logout link")
    @allure.title("Clicking logout link")
    @allure.description("Clicking logout link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_6(self, setup):
        self.pp.click_logout_button()
        if self.driver.current_url == WebHelper().get_login_url():
            WebHelper().report_allure("Logout button functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Logout button not functional", self.driver)
            assert False

    # Test #7 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking get premium link")
    @allure.title("Clicking get premium link")
    @allure.description("Clicking get premium link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_7(self, setup):
        self.pp.click_get_premium_button_1()
        if self.driver.current_url == WebHelper().get_premium_url():
            WebHelper().report_allure("Get Premium button functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Get Premium button not functional", self.driver)
            assert False

    # Test #8 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking get premium link")
    @allure.title("Clicking get premium link")
    @allure.description("Clicking get premium link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_8(self, setup_final):
        self.pp.click_get_premium_button_2()
        if self.driver.current_url == WebHelper().get_premium_url():
            WebHelper().report_allure("Get Premium button functional", self.driver)
            assert True
        else:
            WebHelper().report_allure("Get Premium button not functional", self.driver)
            assert False