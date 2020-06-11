from appium import webdriver
import pytest
import time
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.premium import PremiumPage
from Mobile_Testing.Pages.playlist import PlayList
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Playlist Testing")
@allure.feature("Playlist Testing")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlaylist:
    """
         A class used to represent the Playlist test
         ...
         Attributes
         ----------
         driver: webdriver
              A web driver element to control the android app

         Methods
         -------

         test_case_1()
                Check that the create play list button exists
         test_case_2()
                Check that the save button works
         test_case_3()
                Check that the cancel button works
         test_case_4()
                Creates a new play list
         test_case_5()
                checks that the first play list exists
         test_case_6()
                Checks the edit playlist button
         test_case_7()
                Checks the like playlist button
         test_case_8()
                Checks the share playlist button
         test_case_9()
                Checks the add song playlist button
         test_case_10()
                Checks the edit playlist playlist button
         test_case_11()
                Checks first song in edit playlist exists
         test_case_12()
                Checks cancel rename exists
         test_case_13()
                Checks  rename exists
         test_case_14()
                Checks  delete track exists

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

        # Test #1 ->Checks that create playlist button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking create playlist button")
    @allure.title("Checking create playlist button")
    @allure.description("Checking create playlist button exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Checking create playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        pl = PlayList(self.driver)
        #time.sleep(10)
        if pl.create_button():
            Helper.report_allure(self.driver, "create button exist")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "create button does not exists")
            assert False

        # Test #2 ->Checks that save button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking save button")
    @allure.title("Checking save button")
    @allure.description("Checking save button exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Checking save button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.save_button():
            Helper.report_allure(self.driver, "save button exist")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "save button does not exists")
            assert False

        # Test #3 ->Checks that cancel button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking cancel button")
    @allure.title("Checking cancel button")
    @allure.description("Checking cancel button exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Checking cancel button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.cancel_button():
            Helper.report_allure(self.driver, "cancel button exist")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "cancel button does not exists")
            assert False

        # Test #4 ->Checks  the create playlist
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking create playlist")
    @allure.title("Checking create playlist")
    @allure.description("Checking create playlist")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Checking create playlist
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.create_new_playlist("Test Play List by Kamel"):
            Helper.report_allure(self.driver, "Creation done")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Creation failed")
            assert False

        # Test #5 ->Checks that first playlist button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the first playlist")
    @allure.title("Checking the first playlist")
    @allure.description("Checking the first playlist exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        Checking the first playlist exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.first_element():
            Helper.report_allure(self.driver, "first play list exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "first play list does not exist")
            assert False

        # Test #6 ->Checks that edit  button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the edit")
    @allure.title("Checking the edit")
    @allure.description("Checking the edit exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        Checks the edit playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.check_edit_button():
            Helper.report_allure(self.driver, "edit exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "edit does not exist")
            assert False

        # Test #7 ->Checks that like  button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the like")
    @allure.title("Checking the like")
    @allure.description("Checking the like exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        Checks the like playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.check_like_button():
            Helper.report_allure(self.driver, "like exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "like does not exist")
            assert False

        # Test #8 ->Checks that share  button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the share")
    @allure.title("Checking the share")
    @allure.description("Checking the share exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
        Checks the share playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.check_share_button():
            Helper.report_allure(self.driver, "share exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "share does not exist")
            assert False

        # Test #9 ->Checks that add song  button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the add song")
    @allure.title("Checking the add song")
    @allure.description("Checking the add song exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test9
    def test_case_9(self, setup):
        """
        Checks the add song playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.check_add_song():
            Helper.report_allure(self.driver, "add song exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "add song does not exist")
            assert False

        # Test #10 ->Checks that edit playlist  button exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking the edit playlist")
    @allure.title("Checking the edit playlist")
    @allure.description("Checking the edit playlist exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test10
    def test_case_10(self, setup):
        """
        Checks the edit playlist playlist button
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.edit_playlist():
            Helper.report_allure(self.driver, "edit playlist exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "edit playlist does not exist")
            assert False

        # Test #11 ->Checks first song in edit exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking first song in edit playlist")
    @allure.title("Checking first song in edit playlist")
    @allure.description("Checking first song in edit exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test11
    def test_case_11(self, setup):
        """
        Checks first song in edit playlist exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.first_song_in_edit():
            Helper.report_allure(self.driver, "first song in edit exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "first song in edit does not exist")
            assert False

        # Test #12 ->Checks cancel rename exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking cancel rename")
    @allure.title("Checking cancel rename")
    @allure.description("Checking cancel rename exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test12
    def test_case_12(self, setup):
        """
        Checks cancel rename exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.cancel_rename():
            Helper.report_allure(self.driver, "cancel rename exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "cancel rename does not exist")
            assert False

        # Test #13 ->Checks  rename exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking  rename")
    @allure.title("Checking  rename")
    @allure.description("Checking  rename exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test13
    def test_case_13(self, setup):
        """
        Checks  rename exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.rename():
            Helper.report_allure(self.driver, " rename exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, " rename does not exist")
            assert False

        # Test #14 ->Checks  delete track exists
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Playlist Tests")
    @allure.sub_suite("Checking  delete track")
    @allure.title("Checking  delete track")
    @allure.description("Checking  delete track exists")
    @pytest.mark.Do
    @pytest.mark.Playlist
    @pytest.mark.Test14
    def test_case_14(self, setup):
        """
        Checks  delete track exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        #time.sleep(10)
        hp = HomePage(self.driver)
        hp.click_library_button()
        #time.sleep(10)
        pl = PlayList(self.driver)
        if pl.delete_track():
            Helper.report_allure(self.driver, " delete track exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, " delete track does not exist")
            assert False
