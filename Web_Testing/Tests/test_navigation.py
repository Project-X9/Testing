
"""
Web PLayer Navigation Testing

This script tests the Web Player Navigation functions (Forward and backward buttons) and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

import time

import allure
import pytest

from Web_Testing.Pages.Navigation import Navigation
from Web_Testing.helperClasses import WebHelper


class TestNavigation:
    helper = WebHelper()
    helper.firefox_driver_init()

    helper.driver.maximize_window()
    helper.driver.get(
        "https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Feg-en%2Faccount%2Foverview%2F")
    time.sleep(3)

    def click_song(self):
        cards = self.helper.find_elements_by_class_name("f79dd23c27c3352da3ac3ba62d78f8ea-scss")
        play_btn = self.helper.find_element_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[3]/div[4]/div[1]/div[1]/div[2]/section[1]/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
        self.helper.hover_to_element(cards[0])
        time.sleep(2)
        self.helper.click_button_safe(play_btn)

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
        self.helper.driver.get("https://open.spotify.com/")
        time.sleep(2)
        yield

    @pytest.yield_fixture
    def setup(self):
        yield

    @pytest.yield_fixture
    def setup_final(self):
        time.sleep(3)
        yield
        self.helper.driver.close()

    # Test #1 -> Checking back button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Navigation Buttons Functions")
    @allure.sub_suite("Navigation Buttons Functions")
    @allure.title("Checking if back button works")
    @allure.description("Checking if back button works")
    @pytest.mark.Do
    @pytest.mark.Navigation
    def test_case_1(self, setup_initial):
        # 1. Home
        # 2. Liked Songs
        # 3. Search
        # 4. Your Library
        # 5. Queue
        self.click_song()
        time.sleep(3)
        liked_songs_btn = self.helper.find_element_by_xpath("//text()[.='Liked Songs']/ancestor::a[1]")
        your_library_btn = self.helper.find_element_by_xpath("//text()[.='Your Library']/ancestor::a[1]")
        search_btn = self.helper.find_element_by_xpath("//text()[.='Search']/ancestor::div[1]")
        home_btn = self.helper.find_element_by_xpath("//text()[.='Home']/ancestor::a[1]")
        create_playlist_btn = self.helper.find_element_by_xpath("//text()[.='Create Playlist']/ancestor::button[1]")
        queue_button = self.helper.find_element_by_xpath("//button[@title='Queue']")
        liked_songs_btn.click()
        time.sleep(3)
        search_btn.click()
        time.sleep(3)
        your_library_btn.click()
        time.sleep(3)
        queue_button.click()
        time.sleep(3)
        navigation = Navigation(self.helper.driver)
        navigation.click_back()
        time.sleep(5)
        if (not self.helper.url_has("/collection/playlists")):
            self.helper.report_allure("Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back")
            assert False

        navigation.click_back()
        time.sleep(5)
        if (not self.helper.url_has("/search")):
            self.helper.report_allure(
                "Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back (2 times)")
            assert False

        navigation.click_back()
        time.sleep(5)
        if (not self.helper.url_has("/collection/tracks")):
            self.helper.report_allure(
                "Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back (3 times)")
            assert False

        self.helper.report_allure("Back button working for 3 stacked actions")
        assert True


    # Test #2 -> Checking forward button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Navigation Buttons Functions")
    @allure.sub_suite("Navigation Buttons Functions")
    @allure.title("Checking if forward button works")
    @allure.description("Checking if forward button works")
    @pytest.mark.Do
    @pytest.mark.Navigation
    def test_case_2(self, setup_final):
        # 1. Home
        # 2. Liked Songs - Where the previous test case stopped
        # 3. Search
        # 4. Your Library
        # 5. Queue
        navigation = Navigation(self.helper.driver)
        navigation.click_forward() # should go to search
        time.sleep(5)
        if (not self.helper.url_has("/search")):
            self.helper.report_allure("Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back(3 times), 6. Click forward")
            assert False

        navigation.click_forward() # should go to your library
        time.sleep(5)
        if (not self.helper.url_has("/collection/playlists")):
            self.helper.report_allure(
                "Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back (3 times), 6. Clicking Forward (2 times)")
            assert False

        navigation.click_forward() # should go to queue
        time.sleep(5)
        if (not self.helper.url_has("/queue")):
            self.helper.report_allure(
                "Error returning back. Sequence => 1. Click liked songs, 2. Click search, 3. Click your library, 4. Click liked songs, 5. Click back (3 times), 6. Clicking Forward (3 times)")
            assert False

        self.helper.report_allure("Forward button working for 3 stacked actions")
        assert True

