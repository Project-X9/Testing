"""
Web Player Home and Menu Testing

This script tests the Web Player home page and menu functions and report the results to allure

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
@allure.suite("Web Player Home and Menu")
@allure.feature("Web Player Home Page and Menu")
@allure.severity(allure.severity_level.BLOCKER)
class TestWebPlayerHomeWithMenu:
    exit_code = 0
    helper = WebHelper()
    driver = helper.firefox_driver_init()

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
        self.helper.stop_display()
        if self.exit_code == -1:
            exit(-1)

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
        lp.login_to_spotify("test1@test.com", "test123")
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
            self.exit_code = -1
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
            self.exit_code = -1
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
            self.exit_code = -1
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
            self.exit_code = -1
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
            self.exit_code = -1
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
            self.exit_code = -1
            assert False
        else:
            self.helper.report_allure("SUCCESS: Elements are still visible after refresh", self.driver)
            assert True

    # Test #7 -> Logout Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Logout button")
    @allure.title("Logout button")
    @allure.description("Testing Logout button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_7(self, setup):
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        if web_player_home.check_sign_out():
            self.helper.report_allure("SUCCESS: Sign out button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Sign out button is not functional")
            self.exit_code = -1
            assert False

    # Test #8 -> Test signup Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Sign up button")
    @allure.title("Testing Sign up button")
    @allure.description("Testing Sign up button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_8(self, setup):
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.click_signup()
        time.sleep(3)
        if self.helper.url_has("signup"):
            self.helper.report_allure("SUCCESS: Sign up button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Sign up button is not functional")
            self.exit_code = -1
            assert False

    # Test #9 -> Test login Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing Login button")
    @allure.title("Testing Login button")
    @allure.description("Testing Login button")
    @pytest.mark.Do
    @pytest.mark.WebPlayerHome
    def test_case_9(self, setup_final):
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.click_login()
        time.sleep(3)
        if self.helper.url_has("signin"):
            self.helper.report_allure("SUCCESS: Login button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Login button is not functional")
            self.exit_code = -1
            assert False
