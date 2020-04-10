from appium import webdriver
import pytest
from Mobile_Testing.helper import Helper,Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.signup import SignupPage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.play_music import PlayMusicPage
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Home Page Testing")
@allure.feature("Home Page Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestAuthentication:
    driver = None

    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

        # Test #1 ->checking that play music works
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Play Music clicking")
    @allure.title("Play Music clicking")
    @allure.description("Play Music clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        clicks on the play music button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_play_music_button()
        if Helper.element_exists_by_id(self.driver, PlayMusicPage.play_song_id):
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False

        # Test #2 ->checking that Logout music works
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Logout clicking")
    @allure.title("Logout clicking")
    @allure.description("Logout clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Clicks on the log out button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_play_music_button()
        if Helper.element_exists_by_id(self.driver, HomePage.play_music_button_id()):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            assert True


        # Test #3 ->checking that Logout music works
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("PlayList clicking")
    @allure.title("PlayList clicking")
    @allure.description("PlayList clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Clicks on the Playlist button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_play_music_button()
        if Helper.element_exists_by_id(self.driver, HomePage.play_music_button_id()):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            assert True