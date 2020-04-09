"""
Your Library Page Testing

This script tests the Your Library Page functions and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import time

import allure
import pytest

from Web_Testing.Pages.WebPlayerLibrary import WebPlayerLibrary
from Web_Testing.helperClasses import WebHelper
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.Pages.WebPlayerHome import WebPlayerHome
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from selenium import webdriver
from Web_Testing.helperClasses import ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Web Player Home")
@allure.feature("Web Player Home Page")
@allure.severity(allure.severity_level.BLOCKER)
class TestWebPlayerHome:
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)

    @pytest.yield_fixture
    def setup_initial(self):
        self.driver.get(WebHelper().get_login_url())
        self.driver.maximize_window()
        yield
        self.driver.refresh()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(self.helper.base_url + "webplayer/home")
        self.driver.maximize_window()
        yield
        # self.driver.close()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(self.helper.base_url + "webplayer/home")
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Test #1 -> Your Library Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Your Library Liked Songs Button")
    @allure.title("Liked Songs Button")
    @allure.description("Testing Your Library Liked Songs Button")
    @pytest.mark.Do
    @pytest.mark.YourLibrary
    def test_case_1(self, setup_initial):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.login_to_spotify("abdallah@gmail.com", "123456")
        time.sleep(3)
        self.driver.get(self.helper.base_url + "webplayer/home")
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.click_your_library()
        time.sleep(2)
        web_player_library = WebPlayerLibrary(self.driver)
        if web_player_library.check_liked_songs_click():
            self.helper.report_allure("SUCCESS: Your Library Liked songs cards are functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Your Library Liked songs cards are not functional")
            assert False

# Test #2 -> Playlists Cards
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Your Library playlists cards")
    @allure.title("Playlists cards")
    @allure.description("Testing Your Library Playlists cards")
    @pytest.mark.Do
    @pytest.mark.YourLibrary
    def test_case_2(self, setup_final):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.click_your_library()
        time.sleep(2)
        web_player_library = WebPlayerLibrary(self.driver)

        if web_player_library.check_card_click(0, True):
            self.helper.report_allure("SUCCESS: Your Library page playlist cards are functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Your Library page playlist cards are not functional")
            assert False

