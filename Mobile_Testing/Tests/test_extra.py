from appium import webdriver
import pytest
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.signup import SignupPage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.player import PlayMusicPage
from allure_commons.types import AttachmentType
import allure
import time

@allure.parent_suite("End to End testing - Android")
@allure.suite("Extra  Testing")
@allure.feature("Extra  Testing")
@allure.severity(allure.severity_level.MINOR)
class TestPlayer:
    """
       A class used to represent the Authentication test
       ...
       Attributes
       ----------
       driver: webdriver
            A web driver element to control the android app

       Methods
       -------

       test_case_1()
            checking the artist button
       """
    driver = None



    @pytest.yield_fixture
    def setup(self):
        """
        initiates the driver
        """
        self.driver = Helper.driver_init()
        yield
        self.driver.quit()

        # Test #1 ->checking the artist button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Extra Tests")
    @allure.sub_suite("checking the artist button")
    @allure.title("checking the artist button")
    @allure.description("checking the artist button")
    @pytest.mark.Do
    @pytest.mark.Extra
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        checking the artist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_search_button()
        time.sleep(2)
        open_artist_button = Helper.find_element_by_id(self.driver, "com.example.projectx:id/openArtist")
        if open_artist_button.is_displayed() and open_artist_button.is_enabled():
            Helper.report_allure(self.driver, "Extra test1 passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Extra test1 failed")
            assert False
        open_artist_button.click()

        artist_image = Helper.find_element_by_id(self.driver, "com.example.projectx:id/hostImage")
        if artist_image.is_displayed() and artist_image.is_enabled():
            Helper.report_allure(self.driver, "Extra test2 passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Extra test2 failed")
            assert False
        artist_image.click()

        artist_bio = Helper.find_element_by_id(self.driver, "com.example.projectx:id/artistBio")
        if artist_bio.is_displayed() and artist_bio.is_enabled():
            Helper.report_allure(self.driver, "Extra test3 passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Extra test3 failed")
            assert False
        artist_bio.click()



