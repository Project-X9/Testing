from appium import webdriver
import pytest
import time
from Mobile_Testing.helper import Helper, Constants
from Mobile_Testing.Pages.authentication import AuthenticationPage
from Mobile_Testing.Pages.home import HomePage
from Mobile_Testing.Pages.login import LoginPage
from Mobile_Testing.Pages.premium import PremiumPage
from allure_commons.types import AttachmentType
import allure


@allure.parent_suite("End to End testing - Android")
@allure.suite("Premium Testing")
@allure.feature("Premium Testing")
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
               Checking Ad breaks | Ad Free music box exists
         test_case_2()
              Checking play in shuffle box exists
         test_case_3()
              Checking unlimited skips box exists
         test_case_4()
              Checking offline testing box exists
         test_case_5()
              Checking high audio quality box exists
         test_case_6()
              Checking get premium button exists
         test_case_7()
              Checking free box exists
         test_case_8()
              Checking premium individual box exists
         test_case_9()
              canceling premium
         test_case_10()
              getting premium

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

        # Test #1 ->Checks that ad_breaks/ad_free music

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking ad breaks | ad free music box")
    @allure.title("Checking ad breaks | ad free music box")
    @allure.description("Checking ad breaks | ad free music box exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test1
    def test_case_1(self, setup):
        """
        Checks that the ad-break/free box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_ad_break_box():
            Helper.report_allure(self.driver, "break box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "break box does not exists")
            assert False

        # Test #2 ->Checks the play in shuffle

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking play in shuffle box")
    @allure.title("Checking play in shuffle box")
    @allure.description("Checking play in shuffle box exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test2
    def test_case_2(self, setup):
        """
        Checks that the play in shuffle box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_play_in_shuffle_box():
            Helper.report_allure(self.driver, "play in shuffle box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "play in shuffle box does not exists")
            assert False

        # Test #3 ->Checks the unlimited skips

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking unlimited skips box")
    @allure.title("Checking unlimited skips box")
    @allure.description("Checking unlimited skips exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test3
    def test_case_3(self, setup):
        """
        Checks that the unlimited skips button exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_unlimited_skips_box():
            Helper.report_allure(self.driver, "unlimited skips box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "unlimited skips box does not exists")
            assert False

        # Test #4 ->Checks the offline listening

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking offline listening box")
    @allure.title("Checking offline listening box")
    @allure.description("Checking offline listening exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test4
    def test_case_4(self, setup):
        """
        Checks that the offline listening box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_offline_listening_box():
            Helper.report_allure(self.driver, "offline listening box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "offline listening box does not exists")
            assert False

        # Test #5 ->Checks the high audio quality

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking high audio quality box")
    @allure.title("Checking high audio quality box")
    @allure.description("Checking high audio quality exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test5
    def test_case_5(self, setup):
        """
        Checks that the high audio quality box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_high_audio_quality_box():
            Helper.report_allure(self.driver, "high audio quality box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "high audio quality box does not exists")
            assert False

        # Test #6 ->Checks the get premium button

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking get premium button")
    @allure.title("Checking get premium button")
    @allure.description("Checking get premium button exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test6
    def test_case_6(self, setup):
        """
        Checks that the get premium button exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_get_premium_button():
            Helper.report_allure(self.driver, "get premium button exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "get premium button does not exists")
            assert False

        # Test #7 ->Checks the free box
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking free box")
    @allure.title("Checking free box")
    @allure.description("Checking free box exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test7
    def test_case_7(self, setup):
        """
        Checks that the free box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_free_box():
            Helper.report_allure(self.driver, "free box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "free box does not exists")
            assert False

        # Test #8 ->Checks the premium individual

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking premium individual box")
    @allure.title("Checking premium individual box")
    @allure.description("Checking premium individual box exists")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test8
    def test_case_8(self, setup):
        """
        Checks that the premium individual box exists
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if pp.check_premium_individual_box():
            Helper.report_allure(self.driver, "premium individual box exists")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "premium individual box does not exists")
            assert False

        # Test #9 ->cancel premium

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking canceling premium")
    @allure.title("Checking canceling premium")
    @allure.description("Checking canceling premium")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test9
    def test_case_9(self, setup):
        """
        canceling premium
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if not pp.cancel_get_premium():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "premium did not cancel")
            assert False
        if pp.check_free_box():
            Helper.report_allure(self.driver, "premium canceled")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "premium did not cancel")
            assert False

        # Test #10 ->get premium

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Premium Tests")
    @allure.sub_suite("Checking getting premium")
    @allure.title("Checking getting premium")
    @allure.description("Checking getting premium")
    @pytest.mark.Do
    @pytest.mark.Premium
    @pytest.mark.Test10
    def test_case_10(self, setup):
        """
        getting premium
        """
        ap = AuthenticationPage(self.driver)
        ap.click_signin_button()
        lp = LoginPage(self.driver)
        lp.do_the_login(Constants.correct_credentials["email"], Constants.correct_credentials["password"])
        hp = HomePage(self.driver)
        hp.click_premium_button()
        pp = PremiumPage(self.driver)
        if not pp.cancel_get_premium():
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "premium did not activate")
            assert False
        if pp.check_free_box():
            Helper.report_allure(self.driver, "premium activated")
            assert True
        else:
            print(self.driver.current_activity)
            Helper.report_allure(self.driver, "premium did not activate")
            assert False
