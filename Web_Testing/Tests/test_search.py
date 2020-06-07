
"""
Web PLayer Search Testing

This script tests the Web Player's Search and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

import time

import allure
import pytest

from Web_Testing.Pages.EditProfilePage import EditProfilePage
from Web_Testing.Pages.SearchPage import SearchPage
from Web_Testing.helperClasses import WebHelper, DOB


class TestSearch:
    helper = WebHelper()
    helper.chrome_driver_init()

    helper.driver.maximize_window()
    helper.driver.get(
        "https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Feg-en%2Faccount%2Foverview%2F")
    time.sleep(3)

    def login(self):
        login_email = self.helper.find_element_by_id("login-username")
        login_pass = self.helper.find_element_by_id("login-password")
        login_btn = self.helper.find_element_by_id("login-button")

        self.helper.fill(login_email, "test_projectX@hotmail.com")
        self.helper.fill(login_pass, "TestingTeamMKE")
        self.helper.click_button(login_btn)
        time.sleep(3)

    @pytest.yield_fixture
    def setup_initial(self):
        self.login()
        self.helper.driver.get("https://open.spotify.com/search")
        time.sleep(3)
        yield
        self.helper.driver.refresh()

    @pytest.yield_fixture
    def setup(self):
        self.helper.driver.get("https://open.spotify.com/search")
        time.sleep(2)
        yield
        self.helper.driver.close()

    # Test #1 -> Edit with already used email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Search Page")
    @allure.sub_suite("Search feature with artist")
    @allure.title("Search feature with artist")
    @allure.description("Checking search feature with artist")
    @pytest.mark.Do
    @pytest.mark.SearchPage
    def test_case_1(self, setup_initial):
        search_page = SearchPage(self.helper.driver)
        search_success = search_page.search_for("Amr diab", "Artist")
        if search_success:
            self.helper.report_allure("Successful search result for artist")
            assert True
        else:
            self.helper.report_allure("Irrelevant search result for artist")
            assert False

    # Test #2 -> Edit with already used email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Search Page")
    @allure.sub_suite("Search feature with song")
    @allure.title("Search feature with song")
    @allure.description("Checking search feature with song")
    @pytest.mark.Do
    @pytest.mark.SearchPage
    def test_case_2(self, setup):
        search_page = SearchPage(self.helper.driver)
        search_success = search_page.search_for("Elevated", "Song")
        if search_success:
            self.helper.report_allure("Successful search result for song")
            assert True
        else:
            self.helper.report_allure("Irrelevant search result for song")
            assert False



