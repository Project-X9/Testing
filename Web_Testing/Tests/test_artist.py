"""
Artist Testing

This script tests the follow and unfollow of artists and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import allure
import pytest

from Web_Testing.helperClasses import WebHelper, ConstantsClass,login

from Web_Testing.Pages.artist import Artist



@allure.parent_suite("End to End testing")
@allure.suite("Artist test")
@allure.feature("Artist test")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlaylistSongs:
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    fa = Artist(driver)
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

    # Test #1 ->Checking that follow artist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Artist tests")
    @allure.sub_suite("follow artist")
    @allure.title("follow artist")
    @allure.description("follow artist")
    @pytest.mark.Do
    @pytest.mark.Artist
    def test_case_1(self, setup_begin):
        self.driver.implicitly_wait(5)
        self.fa.overview()
        self.helper.report_allure("overview for artists before follow new one", self.driver)
        if self.fa.follow_artist():
            self.helper.report_allure("follow artist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to follow artist", self.driver)
            assert False

    # Test #2 ->Checking that unfollow artist is functio
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer Artist tests")
    @allure.sub_suite("Unfollow artist")
    @allure.title("Unfollow artist")
    @allure.description("Unfollow artist")
    @pytest.mark.Do
    @pytest.mark.Artist
    def test_case_2(self, setup_final):
        self.driver.implicitly_wait(5)
        self.fa.overview()
        self.helper.report_allure("overview for artists before unfollow one", self.driver)
        if self.fa.unfollow_artist():
            self.helper.report_allure("Unfollow artist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to unfollow artist", self.driver)
            assert False
