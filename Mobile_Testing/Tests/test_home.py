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
@allure.suite("Home Page Testing")
@allure.feature("Home Page Testing")
@allure.severity(allure.severity_level.BLOCKER)
class TestHome:
    """
       A class used to represent the Home page test
       ...
       Attributes
       ----------
       driver: webdriver
            A web driver element to control the android app

       Methods
       -------

       test_case_1()
            Clicks on the log out button and checks that it works
       test_case_2()
            checking the New  releases works
       test_case_3()
            checking the Liked tracks works
       test_case_4()
            checking the Popular tracks works
       test_case_5()
            checking the Recommended tracks works
       test_case_6()
            checking the About works
       test_case_7()
            checking the Home works
       test_case_8()
            checking the Search works

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

        # Test #1 ->checking that Logout music works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Logout clicking")
    @allure.title("Logout clicking")
    @allure.description("Logout clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Clicks on the log out button and checks that it works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_logout_button()
        if Helper.element_exists_by_id(self.driver, ap.signin_button_id):
            Helper.report_allure(self.driver, "Home page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False

        # Test #2 ->checking that new  releases works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("New releases clicking")
    @allure.title("New releases clicking")
    @allure.description("New releases clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
            checking the New  releases works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_new_releases_button()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True

        # Test #3 ->checking that liked tracks works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Liked tracks clicking")
    @allure.title("Liked tracks clicking")
    @allure.description("Liked tracks clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
            checking the Liked tracks works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_liked_tracks_button()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True

        # Test #4 ->checking that popular  works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Popular tracks clicking")
    @allure.title("Popular tracks clicking")
    @allure.description("Popular tracks clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
            checking the Popular tracks works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_popular_tracks_button()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True

        # Test #5 ->checking that recommended works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Recommended tracks clicking")
    @allure.title("Recommended tracks clicking")
    @allure.description("Recommended tracks clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
            checking the Recommended tracks works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_recommended_tracks()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True

        # Test #6 ->checking that about works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("About  clicking")
    @allure.title("About clicking")
    @allure.description("About clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
            checking the About works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_about_button()
        time.sleep(2)
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True

        # Test #7 ->checking that Home  works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Home  clicking")
    @allure.title("Home clicking")
    @allure.description("Home clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
            checking the Home works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_home_button()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            Helper.report_allure(self.driver, "Home page test passed")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False

        # Test #8 ->checking that search works

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Home Page Tests")
    @allure.sub_suite("Search  clicking")
    @allure.title("Search clicking")
    @allure.description("Search clicking and check that it works")
    @pytest.mark.Do
    @pytest.mark.HomePage
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
            checking the Search works
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        time.sleep(10)
        hp.click_search_button()
        if Helper.element_exists_by_id(self.driver, HomePage.about_button_id):
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "Home page test failed")
            assert False
        else:
            Helper.report_allure(self.driver, "Home page test passed")
            assert True
