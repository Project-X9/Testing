from appium import webdriver
import pytest
import time
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.premium import PremiumPage
from Mobile_Testing.Pages.library import LibraryPage
from Mobile_Testing.Pages.album import AlbumPage
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Album Testing")
@allure.feature("Album Testing")
@allure.severity(allure.severity_level.CRITICAL)
class TestPremium:
    """
         A class used to represent the premium tests
         ...
         Attributes
         ----------
         driver: webdriver
              A web driver element to control the android app

         Methods
         -------

         test_case_1()
               checks the first album exists
         test_case_2()
              checks the first song in the first album
         test_case_3()
              checks the like button in the album
         test_case_4()
              checks the share button in the album

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

        # Test #1 ->Checks the first album exists and click-able

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Album Tests")
    @allure.sub_suite("Checking first album")
    @allure.title("Checking first album")
    @allure.description("Checking first album exists and is click-able")
    @pytest.mark.Do
    @pytest.mark.Album
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Checking first album exists and is click-able
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        lp = LibraryPage(self.driver)
        lp
        if not lp.open_albums():
            assert False
        ap = AlbumPage(self.driver)
        if ap.open_first_album():
            Helper.report_allure(self.driver, "first album exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "first album doesnot exist")
            assert False

        # Test #2 ->Checks the first song exists and click-able
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Album Tests")
    @allure.sub_suite("Checking first song")
    @allure.title("Checking first song")
    @allure.description("Checking first song exists and is click-able")
    @pytest.mark.Do
    @pytest.mark.Album
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Checking first song exists and is click-able
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        lp = LibraryPage(self.driver)
        if not lp.open_albums():
            assert False
        ap = AlbumPage(self.driver)
        if ap.open_first_song():
            Helper.report_allure(self.driver, "first song exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "first song does not exist")
            assert False

        # Test #3 ->Checks the  like and click-able
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Album Tests")
    @allure.sub_suite("Checking like")
    @allure.title("Checking like")
    @allure.description("Checking like exists and is click-able")
    @pytest.mark.Do
    @pytest.mark.Album
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Checking like exists and is click-able
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        lp = LibraryPage(self.driver)
        if not lp.open_albums():
            assert False
        ap = AlbumPage(self.driver)
        if ap.check_like_button():
            Helper.report_allure(self.driver, "like exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "like does not exist")
            assert False

        # Test #4 ->Checks the  share and click-able
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Album Tests")
    @allure.sub_suite("Checking share")
    @allure.title("Checking share")
    @allure.description("Checking share exists and is click-able")
    @pytest.mark.Do
    @pytest.mark.Album
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Checking like share and is click-able
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        lp = LibraryPage(self.driver)
        if not lp.open_albums():
            assert False
        ap = AlbumPage(self.driver)
        if ap.check_share_button():
            Helper.report_allure(self.driver, "share exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "share does not exist")
            assert False

