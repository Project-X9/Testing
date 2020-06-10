"""
Playlist songs Testing

This script tests the addition and removal of playlist songs and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

import allure
import pytest

from Web_Testing.helperClasses import WebHelper, ConstantsClass, login

from Web_Testing.Pages.PlaylistSongs import PlaylistSongs


@allure.parent_suite("End to End testing")
@allure.suite("Playlist songs test")
@allure.feature("Playlist songs test")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlaylistSongs:
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    ps = PlaylistSongs(driver)
    lp = login(driver)

    def login_first(self):
        lp = login(self.driver)
        lp.login_to_spotify()

    @pytest.yield_fixture
    def setup_begin(self):
        self.driver.get("https://accounts.spotify.com/en/login")
        self.driver.maximize_window()
        self.login_first()
        yield
        self.driver.refresh()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("https://open.spotify.com/")
        yield
        self.driver.close()

    # Test #1 ->Checking that add song to playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Playlist songs tests")
    @allure.sub_suite("Add song to playlist")
    @allure.title("Add song to playlist")
    @allure.description("Add song to playlist")
    @pytest.mark.Do
    @pytest.mark.PlaylistSong
    def test_case_1(self, setup_begin):
        self.driver.implicitly_wait(5)
        self.ps.overview()
        self.helper.report_allure("overview for playlist songs before add new one", self.driver)
        if self.ps.add_song_to_playlist():
            self.helper.report_allure("Add song to playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to add song to playlist", self.driver)
            assert False

    # Test #2 ->Checking that remove song from playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Playlist songs tests")
    @allure.sub_suite("Remove song from playlist")
    @allure.title("Remove song from playlist")
    @allure.description("Remove song from playlist")
    @pytest.mark.Do
    @pytest.mark.PlaylistSong
    def test_case_2(self, setup_final):
        self.driver.implicitly_wait(5)
        self.ps.overview()
        self.helper.report_allure("overview for playlist songs before remove one", self.driver)
        if self.ps.remove_song_from_playlist():
            self.helper.report_allure("Remove song from playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to remove song from playlist", self.driver)
            assert False