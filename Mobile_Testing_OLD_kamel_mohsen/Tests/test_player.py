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
@allure.suite("Player Page Testing")
@allure.feature("Player Page Testing")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlayer:
    """
       A class used to represent the Login page test
       ...
       Attributes
       ----------
       driver: webdriver
            A web driver element to control the android app

       Methods
       -------

       test_case_1()
            Checks that play button is visible and enabled
       test_case_2()
            Checks that Previous button is visible and enabled
       test_case_3()
            Checks that Next button is visible and enabled
       test_case_4()
            Checks that Love button is visible and enabled
       test_case_5()
            Checks that Download button is visible and enabled
       test_case_6()
            Checks that Repeat button is visible and enabled
       test_case_7()
            Checks that Share button is visible and enabled
       test_case_8()
            Checks that minimize button is  working
       test_case_9()
            Checks that Minimize button is visible and enabled
       test_case_10()
            Checks that Blacklist button is visible and enabled
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

        # Test #1 ->checking the play button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Play button checking")
    @allure.title("Play button checking")
    @allure.description("Checking that the Play button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Checks that play button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(8)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.play_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #2 ->checking the previous button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Previous button checking")
    @allure.title("Previous button checking")
    @allure.description("Checking that the Previous button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Checks that Previous button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.previous_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #3 ->checking the Next button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Next button checking")
    @allure.title("Next button checking")
    @allure.description("Checking that the Next button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Checks that Next button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.next_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #4 ->checking the Love button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Love button checking")
    @allure.title("Love button checking")
    @allure.description("Checking that the Love button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Checks that Love button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.love_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #5 ->checking the Download button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Download button checking")
    @allure.title("Download button checking")
    @allure.description("Checking that the Download button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        Checks that Download button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.download_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #6 ->checking the repeat button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Repeat button checking")
    @allure.title("Repeat button checking")
    @allure.description("Checking that the repeat button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        Checks that Repeat button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.repeat_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #7 ->checking the Share button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Share button checking")
    @allure.title("Share button checking")
    @allure.description("Checking that the Share button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        Checks that Share button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.share_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #8 ->checking the minimize button is working

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Minimize button clicking")
    @allure.title("Minimize button checking")
    @allure.description("Checking that the Minimize button is working")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
        Checks that minimize button is  working
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.minimize_player_id)
        element.click()
        if Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist):
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #9 ->checking the minimize button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Minimize button checking")
    @allure.title("Minimize button checking")
    @allure.description("Checking that the Minimize button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test9
    def test_case_9(self, setup):
        """
        Checks that Minimize button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.minimize_player_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False

        # Test #10 ->checking the blacklist button is visible

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Player Page Tests")
    @allure.sub_suite("Blacklist button checking")
    @allure.title("Blacklist button checking")
    @allure.description("Checking that the Blacklist button is visible")
    @pytest.mark.Do
    @pytest.mark.Player
    @pytest.mark.Test10
    def test_case_10(self, setup):
        """
        Checks that Blacklist button is visible and enabled
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        time.sleep(2)
        Helper.find_element_by_xpath(self.driver, Constants.first_song_playlist).click()
        time.sleep(2)
        element = Helper.find_element_by_id(self.driver, PlayMusicPage.black_list_song_id)
        if element.is_displayed() and element.is_enabled():
            Helper.report_allure(self.driver, "Player page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Player page test failed")
            assert False
