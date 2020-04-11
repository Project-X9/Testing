
"""
Premium page Testing

This script tests the premium page buttons and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from allure_commons.types import AttachmentType
import allure
import pytest

from Web_Testing.helperClasses import WebHelper, ConstantsClass

from Web_Testing.Pages.LoginPage import LoginPage

from Web_Testing.Pages.WebPlayerPlaylist import WebPlayerPlaylist

from Web_Testing.Pages.WebPlayerHome import WebPlayerHome


@allure.parent_suite("End to End testing")
@allure.suite("Playlist page test")
@allure.feature("Playlist page test")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlaylist:
    # TODO: change Firefox executable path to your needs
    driver = WebHelper().chrome_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    playlist = WebPlayerPlaylist(driver)

    def login_first(self):
        lp = LoginPage(self.driver)
        lp.set_credentials("abdallah@gmail.com", ConstantsClass().get_pass("abdallah@gmail.com"))
        lp.click_login()
        self.driver.implicitly_wait(3)
        self.playlist.click_webplayer()
        self.driver.implicitly_wait(3)

    @pytest.yield_fixture
    def setup_initial(self):
        self.driver.get(self.helper.get_login_url())
        self.driver.maximize_window()
        yield
        self.driver.refresh()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(self.helper.base_url + "webplayer/librarypage")
        self.driver.maximize_window()
        yield
        # self.driver.close()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(self.helper.base_url + "webplayer/librarypage")
        self.driver.maximize_window()
        yield
        self.driver.close()

 # Test #1 -> Play Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing  Play Button")
    @allure.title("Playlist Play Button")
    @allure.description("Testing Playlist Play Button")
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
        self.playlist.click_playlist_play_btn()
        time.sleep(5)
        if self.helper.url_has("webplayer/nowplay"):
            self.helper.report_allure("SUCCESS: Play button is functional")
            assert True
        else:
            self.helper.report_allure("FAILURE: Play button is not functional")
            assert False

# Test #2 -> Check Playlist card go to the right playlist
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing playlists cards")
    @allure.title("Playlists cards")
    @allure.description("Testing  Playlists cards")
    @pytest.mark.Do
    @pytest.mark.YourLibrary
    def test_case_2(self, setup_final):
        if self.playlist.check_playlist(0, True):
            self.helper.report_allure("SUCCESS:Playlist card goes to the right playlist")
            assert True
        else:
            self.helper.report_allure("FAILURE: Playlist card doesn't go to the right playlist")
            assert False



