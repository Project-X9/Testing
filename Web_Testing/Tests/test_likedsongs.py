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

from Web_Testing.Pages.LikedSongs import LikedSongs


@allure.parent_suite("End to End testing")
@allure.suite("Playlist page test")
@allure.feature("Playlist page test")
@allure.severity(allure.severity_level.CRITICAL)
class TestLikedSongs:
    # TODO: change Firefox executable path to your needs
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    liked_songs = LikedSongs(driver)

    @pytest.yield_fixture
    def setup(self):
        self.driver.get(self.helper.get_login_url())
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.stop_display()

    # Test #1 -> Check Liked Songs
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Testing  Play Button")
    @allure.title("Playlist Play Button")
    @allure.description("Testing Playlist Play Button")
    @pytest.mark.Do
    @pytest.mark.YourLibrary
    def test_case_1(self, setup):
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.login_to_spotify("abdallah@gmail.com", "1234567")
        time.sleep(3)
        self.driver.get(self.helper.base_url + "webplayer/home")
        time.sleep(3)
        web_player_home = WebPlayerHome(self.driver)
        web_player_home.click_liked_songs()
        if self.liked_songs.check_liked_songs():
            self.helper.report_allure("SUCCESS: Liked Songs are correct")
            assert True
        else:
            self.helper.report_allure("FAILURE: Liked Songs are not correct")
            assert False
