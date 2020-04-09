"""
Web Player Home Testing

This script tests the Web Player home page functions and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import time

import allure
import pytest
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
    @allure.story("Testing Your Library Button")
    @allure.title("Your Library Button")
    @allure.description("Testing Your Library Button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_1(self, setup_initial):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.login_to_spotify("abdallah@gmail.com", "123456")
        time.sleep(3)
        self.driver.get(self.helper.base_url + "webplayer/home")
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.your_library_button.click()
        time.sleep(2)
        if web_player_home.is_in_your_library():
            self.helper.report_allure("SUCCESS: Your Library button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Your Library button is not functional")
            assert False

    # Test #2 -> Liked Songs Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Liked Songs Button")
    @allure.title("Liked Songs Button")
    @allure.description("Testing Liked Songs Button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_2(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.liked_songs_link.click()
        time.sleep(2)
        if web_player_home.is_in_liked_songs():
            self.helper.report_allure("SUCCESS: Liked Songs button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Liked Songs button is not functional")
            assert False

    # Test #3 -> Playlists Cards
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing playlists cards")
    @allure.title("Playlists cards")
    @allure.description("Testing Playlists cards")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_3(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)

        if web_player_home.check_card_click('Rock', 0, True):
            self.helper.report_allure("SUCCESS: Playlist cards are functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Playlist cards are not functional")
            assert False

    # Test #4 -> Artists Cards
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Artist cards Button")
    @allure.title("Artist cards button")
    @allure.description("Testing Artists cards Button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_4(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)

        if web_player_home.check_card_click('Popular Artists', 0, True):
            self.helper.report_allure("SUCCESS: Artists cards are functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Artists cards are not functional")
            assert False

    # Test #5 -> Albums Cards
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Albums cards")
    @allure.title("Albums cards")
    @allure.description("Testing Albums cards")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_5(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)

        if web_player_home.check_card_click('Popular albums', 0, True):
            self.helper.report_allure("SUCCESS: Albums cards are functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Albums cards are not functional")
            assert False

    # Test 6 -> Refresh Test
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Refresh")
    @allure.title("Refresh Page")
    @allure.description("Testing Refresh and make sure that elements are visible")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_6(self, setup):
        self.driver.refresh()
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)
        if (web_player_home.home_link is None) or (web_player_home.your_library_button is None) \
                or (web_player_home.liked_songs_link is None) or (web_player_home.profile_btn is None):
            self.helper.report_allure("FAILURE: Refresh caused some elements to disappear", self.driver)
            assert False
        else:
            self.helper.report_allure("SUCCESS: Elements are still visible after refresh", self.driver)
            assert True

    # Test 7 -> Back button Test 1
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Back/Forward Button")
    @allure.title("Back/Forward Button")
    @allure.description("Testing Back/Forward Button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_7(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.check_card_click('Rock', 0, False)
        time.sleep(2)
        web_player_home.click_back_button()
        time.sleep(2)
        if not self.helper.url_has("webplayer/home"):
            self.helper.report_allure("FAILURE: Sequence -> 1. Web Player Home, 2. Clicked a Card"
                                      + ", 3. Clicked back button but did not return to Web Player Home", self.driver)
            assert False
        else:
            self.helper.report_allure("Back button working for same tab but different page", self.driver)
            web_player_home.click_forward_button()
            time.sleep(2)
            if self.helper.url_has("webplayer/nowplay"):
                self.helper.report_allure("Forward Button SUCCESS: Forward button working for same tab but different page",
                                          self.driver)
                assert True
            else:
                self.helper.report_allure("Forward Button FAILURE: Forward button not working for same tab but different page",
                                          self.driver)
                assert False

    # Test 8 -> Back/Forward button Test 2
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Back/Forward Button 2")
    @allure.title("Back/Forward Button 2")
    @allure.description("Testing Back/Forward Button 2")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_8(self, setup):
        time.sleep(2)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.liked_songs_link.click()
        time.sleep(2)
        web_player_home.click_your_library()
        time.sleep(2)
        web_player_home.click_back_button()
        time.sleep(2)
        if not self.helper.url_has("webplayer/likedplay"):
            self.helper.report_allure("Back Button FAILURE: Sequence -> 1. Web Player Home, 2. Liked Songs, 3. Your Library"
                                      + ", 4. Clicked back button but did not return to Liked Songs", self.driver)
            assert False
        else:
            self.helper.report_allure("Back Button SUCCESS: Back button working for different tabs", self.driver)
            web_player_home.click_forward_button()
            time.sleep(2)
            if self.helper.url_has("webplayer/librarypage"):
                self.helper.report_allure("Forward Button SUCCESS: Forward button working for different tabs", self.driver)
                assert True
            else:
                self.helper.report_allure("Forward Button FAILURE: Forward button not working for different tabs",
                                          self.driver)
                assert False

    # Test #9 -> Logout Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Logout button")
    @allure.title("Logout button")
    @allure.description("Testing Logout button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_9(self, setup_final):
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        if web_player_home.check_sign_out():
            self.helper.report_allure("SUCCESS: Sign out button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Sign out button is not functional")
            assert False
