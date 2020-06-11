
"""
Web PLayer Play Footer Testing

This script tests the Web Player's Play Footer and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""

import time

import allure
import pytest

from Web_Testing.Pages.PlayFooter import PlayFooter
from Web_Testing.helperClasses import WebHelper, DOB


class TestPlayFooter:

    helper = WebHelper()
    helper.firefox_driver_init()

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

    def click_song(self):
        cards = self.helper.find_elements_by_class_name("f79dd23c27c3352da3ac3ba62d78f8ea-scss")
        play_btn = self.helper.find_element_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[3]/div[4]/div[1]/div[1]/div[2]/section[1]/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
        self.helper.hover_to_element(cards[0])
        time.sleep(2)
        self.helper.click_button_safe(play_btn)

    @pytest.yield_fixture
    def setup_initial(self):
        self.login()
        self.helper.driver.get("https://open.spotify.com/")
        time.sleep(6)
        yield

    @pytest.yield_fixture
    def setup(self):
        yield

    @pytest.yield_fixture
    def setup_final(self):
        yield
        self.helper.driver.close()

    # Test #1 -> Play and Progress bar
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Play Footer")
    @allure.sub_suite("Play Footer")
    @allure.title("Play Footer testing Play button and progress")
    @allure.description("Play Footer testing Play button and progress bar")
    @pytest.mark.Do
    @pytest.mark.PlayFooter
    def test_case_1(self, setup_initial):
        self.click_song()
        time.sleep(3)
        play_footer = PlayFooter(self.helper.driver)
        time1 = play_footer.get_consumed_time()
        time.sleep(10)
        time2 = play_footer.get_consumed_time()
        if time2.is_greater_than(time1.minutes, time1.seconds):
            self.helper.report_allure("Play button working and the song has progress")
            assert True
        else:
            self.helper.report_allure("Play button failure and the song has no progress")
            assert False

    # Test #2 -> Pause and progress bar
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Play Footer")
    @allure.sub_suite("Play Footer")
    @allure.title("Play Footer testing Pause button and progress")
    @allure.description("Play Footer testing Pause button and progress bar")
    @pytest.mark.Do
    @pytest.mark.PlayFooter
    def test_case_2(self, setup):
        play_footer = PlayFooter(self.helper.driver)
        play_footer.click_play_or_pause()
        time1 = play_footer.get_consumed_time()
        time.sleep(5)
        time2 = play_footer.get_consumed_time()
        if time1.is_equal_to(time2.minutes, time2.seconds):
            self.helper.report_allure("Pause button working and the song has stopped")
            assert True
        else:
            self.helper.report_allure("Play button failure")
            assert False

    # Test #3 -> Next and Previous Song Buttons
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Play Footer")
    @allure.sub_suite("Play Footer")
    @allure.title("Play Footer Next and Previous Song Buttons")
    @allure.description("Play Footer Next and Previous Song Buttons")
    @pytest.mark.Do
    @pytest.mark.PlayFooter
    def test_case_3(self, setup):
        success = True
        play_footer = PlayFooter(self.helper.driver)
        song1 = play_footer.get_song_name()
        play_footer.click_next_song()
        time.sleep(2)
        song2 = play_footer.get_song_name()
        if song1 == song2:
            self.helper.report_allure("Next Song button failure, same song is still playing")
            success = False
        else:
            self.helper.report_allure("Next Song button success. Started playing the next song")

        play_footer.click_prev_song()
        time.sleep(2)
        song3 = play_footer.get_song_name()
        if song3 != song2 and song3 == song1:
            self.helper.report_allure("Previous Song button success. Returned back to playing the previous song")
        else:
            self.helper.report_allure("Previous Song button failure, did not go back to the previous song")
            success = False

        assert success

    # Test #4 -> Queue Button
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Play Footer")
    @allure.sub_suite("Play Footer")
    @allure.title("Play Footer Queue Button")
    @allure.description("Play Footer Queue Button checks if it goes to the right page")
    @pytest.mark.Do
    @pytest.mark.PlayFooter
    def test_case_4(self, setup_final):
        play_footer = PlayFooter(self.helper.driver)
        play_footer.click_queue()
        time.sleep(3)
        if self.helper.url_has("/queue"):
            self.helper.report_allure("Queue Button working and went to the correct page")
            assert True
        else:
            self.helper.report_allure("Queue Button failure. Did not go to the right page")
            assert False


