
"""
Web PLayer Search Testing

This script tests the Web Player's Album operations (Add/remove albums to/from your library) and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

import time

import allure
import pytest

from Web_Testing.Pages.AlbumPage import AlbumPage
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
        self.helper.fill(login_pass, "TestingTeamMKE20")
        self.helper.click_button(login_btn)
        time.sleep(3)

    @pytest.yield_fixture
    def setup_initial(self):
        self.login()
        self.helper.driver.get("https://open.spotify.com/album/2IV13wMMDBs2OyqNdAswSP") # Page of the Album 'Sarhan'
        time.sleep(7)
        yield

    @pytest.yield_fixture
    def setup(self):
        self.helper.driver.get("https://open.spotify.com/album/2IV13wMMDBs2OyqNdAswSP") # Page of the Album 'Sarhan'
        time.sleep(7)
        yield
        self.helper.driver.close()

    # Test #1 -> Test adding album to library
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Albums Page")
    @allure.sub_suite("Adding album to library")
    @allure.title("Adding album to library")
    @allure.description("Testing saving an album to library")
    @pytest.mark.Do
    @pytest.mark.AlbumsPage
    def test_case_1(self, setup_initial):
        albums_page = AlbumPage(self.helper.driver)
        albums_page.add_album_to_library()
        self.helper.driver.get("https://open.spotify.com/collection/albums")
        time.sleep(3)
        if albums_page.assert_albums_has("Sahran"):
            self.helper.report_allure("Correct Album added to library")
            assert True
        else:
            self.helper.report_allure("Album not added to library")
            assert False

    # Test #2 -> Test removing album to library
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Albums Page")
    @allure.sub_suite("Removing album from library")
    @allure.title("Removing album from library")
    @allure.description("Removing saved album from library")
    @pytest.mark.Do
    @pytest.mark.AlbumsPage
    def test_case_2(self, setup):
        albums_page = AlbumPage(self.helper.driver)
        albums_page.remove_album_from_library()
        self.helper.driver.get("https://open.spotify.com/collection/albums")
        time.sleep(3)
        if not albums_page.assert_albums_has("Sahran"):
            self.helper.report_allure("Album removed from library")
            assert True
        else:
            self.helper.report_allure("Album not removed from library")
            assert False



