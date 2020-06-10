"""
Liked songs Testing

This script tests the like and unlike of songs and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import allure
import pytest

from Web_Testing.helperClasses import WebHelper, ConstantsClass, login

from Web_Testing.Pages.LikedSongs import LikedSongs


@allure.parent_suite("End to End testing")
@allure.suite("Liked songs page test")
@allure.feature("Liked songs page test")
@allure.severity(allure.severity_level.CRITICAL)
class TestLikedSongs:
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    ls = LikedSongs(driver)
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

    # Test #1 ->Checking that like song is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Liked songs tests")
    @allure.sub_suite("Like new song")
    @allure.title("Like new song")
    @allure.description("Like new song")
    @pytest.mark.Do
    @pytest.mark.LikeSong
    def test_case_1(self, setup_begin):
        self.driver.implicitly_wait(5)
        self.ls.overview()
        self.helper.report_allure("overview for liked songs before like new one", self.driver)
        if self.ls.like_song():
            self.helper.report_allure("Like song successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to like song", self.driver)
            assert False

    # Test #2 ->Checking that unlike song is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Liked songs tests")
    @allure.sub_suite("Unlike song")
    @allure.title("Unlike song")
    @allure.description("Unlike song")
    @pytest.mark.Do
    @pytest.mark.UnlikeSong
    def test_case_2(self, setup_final):
        self.driver.implicitly_wait(5)
        self.ls.overview()
        self.helper.report_allure("overview for liked songs before unlike one", self.driver)
        if self.ls.unlike_song():
            self.helper.report_allure("Unlike song successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to unlike song", self.driver)
            assert False
