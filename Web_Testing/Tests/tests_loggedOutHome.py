import allure
import pytest
from Web_Testing.helperClasses import WebHelper
from Web_Testing.Pages.LoginPage import LoginPage
from Web_Testing.Pages.SignupPage import SignupPage
from Web_Testing.Pages.LoggedOutHome import LoggedOutHome
from Web_Testing.helperClasses import ConstantsClass


@allure.parent_suite("End to End testing")
@allure.suite("Home")
@allure.feature("Home Page")
@allure.severity(allure.severity_level.BLOCKER)
class TestLoggedOutHome:

    driver = WebHelper().firefox_driver_init()
    @pytest.yield_fixture
    def setup(self):
        self.driver.get(ConstantsClass().get_home_link())
        self.driver.maximize_window()
        yield

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get(ConstantsClass().get_home_link())
        self.driver.maximize_window()
        yield
        self.driver.close()

# Test #1 -> Different Confirmation email
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Clicking Signup")
    @allure.title("Testing Sign up Button")
    @allure.description("Testing Sign up button")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_1(self, setup):
        # logged_out_home = LoggedOutHome(self.driver)
        # logged_out_home.tb_signup_btn.click()
        self.driver.find_element_by_link_text("Sign up").click()
        self.driver.implicitly_wait(3)
        sp = SignupPage(self.driver)
        if sp.check_signup_page():
            WebHelper().report_allure("Signup button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Signup button failed", self.driver)
            assert False

# Test #2 -> Testing Login Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login Button")
    @allure.title("Testing Login Button")
    @allure.description("Testing Login Button")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_2(self, setup):
        self.driver.find_element_by_link_text("Log In").click()
        sp = LoginPage(self.driver)
        if sp.check_login_page():
            WebHelper().report_allure("Login button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Login button failed", self.driver)
            assert False

# Test #3 -> Testing Premium Button
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Premium Button")
    @allure.title("Testing Premium Button")
    @allure.description("Testing Premium Button")
    @pytest.mark.Do
    @pytest.mark.Signup
    def test_case_3(self, setup_final):
        self.driver.find_element_by_link_text("Premium").click()
        self.driver.implicitly_wait(3)

        if str(self.driver.current_url).find('premium') != -1:
            WebHelper().report_allure("Premium button working", self.driver)
            assert True
        else:
            WebHelper().report_allure("Premium button failed", self.driver)
            assert False