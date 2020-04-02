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
    driver = WebHelper().chrome_driver_init()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get("http://localhost:3000/premium")
        self.driver.maximize_window()
        yield
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.delete_all_cookies()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("http://localhost:3000/premium")
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
        pp = PremiumPage(self.driver)

        pp.click_spotify_logo()
        if self.driver.current_url == "http://localhost:3000/signup":
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
        pp = PremiumPage(self.driver)
        pp.click_profile_link()
        pp.click_account_link()
        if self.driver.current_url == "http://localhost:3000/accountoverview":
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
        pp = PremiumPage(self.driver)
        pp.click_download_link()
        if self.driver.current_url == "http://localhost:3000/download":
            assert True
        else:
            WebHelper().report_allure("Download not functional", self.driver)
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
        pp = PremiumPage(self.driver)
        pp.click_help_link()
        if self.driver.current_url == "http://localhost:3000/help":
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
        pp = PremiumPage(self.driver)
        pp.click_home_link()
        if self.driver.current_url == "http://localhost:3000/home":
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
        pp = PremiumPage(self.driver)
        pp.click_profile_link()
        pp.click_logout_button()
        if self.driver.current_url == "http://localhost:3000/signin":
            assert True
        else:
            WebHelper().report_allure("Logout button not functional", self.driver)
            assert False

    # Test #7 ->Checking that all buttons and links work
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium tests")
    @allure.sub_suite("Clicking profile link")
    @allure.title("Clicking profile link")
    @allure.description("Clicking profile link")
    @pytest.mark.Do
    @pytest.mark.Premium
    def test_case_7(self, setup):
        pp = PremiumPage(self.driver)
        pp.click_profile_link()
        pp.click_account_link()
        if self.driver.current_url == "http://localhost:3000/accountoverview":
            assert True
        else:
            WebHelper().report_allure("Profile link not functional", self.driver)
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
        pp = PremiumPage(self.driver)
        pp.get_premium_button
        if self.driver.current_url == "http://localhost:3000/getpremium":
            assert True
        else:
            WebHelper().report_allure("Premium button not functional", self.driver)
            assert False