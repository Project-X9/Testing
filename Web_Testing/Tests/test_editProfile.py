
"""
Edit Profile Testing

This script tests the Edit Profile functions and report the results to allure

This script requires `allure`, `pytest` and `selenium` be installed within the Python environment you are running this script in
"""

import time

import allure
import pytest
from selenium.webdriver.chrome import webdriver

from Web_Testing.Pages.EditProfilePage import EditProfilePage
from Web_Testing.helperClasses import WebHelper, DOB
from selenium.webdriver.support.select import Select


class TestEditProfile:

    edit_profile_link = "https://www.spotify.com/eg-en/account/profile/"
    helper = WebHelper()
    helper.firefox_driver_init()

    helper.driver.maximize_window()
    helper.driver.get(
        "https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Feg-en%2Faccount%2Foverview%2F")
    time.sleep(3)

    def login(self):
        login_email = self.helper.find_element_by_id("login-username")
        login_pass = self.helper.find_element_by_id("login-password")
        login_btn = self.helper.find_element_by_id("login-button")

        self.helper.fill(login_email, "test_projectX@hotmail.com")
        self.helper.fill(login_pass, "TestingTeamMKE")
        self.helper.click_button(login_btn)
        time.sleep(3)

    @pytest.yield_fixture
    def setup_initial(self):
        self.login()
        self.helper.driver.get(self.edit_profile_link)
        time.sleep(2)
        yield
        # self.helper.driver.refresh()

    @pytest.yield_fixture
    def setup(self):
        time.sleep(2)
        # self.login()
        self.helper.driver.get(self.edit_profile_link)
        time.sleep(3)
        yield

    @pytest.yield_fixture
    def setup_final(self):
        time.sleep(2)
        # self.login()
        self.helper.driver.get(self.edit_profile_link)
        yield
        self.helper.driver.close()

    # Test #1 -> Edit with already used email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Edit Profile Page")
    @allure.sub_suite("Edit Profile feature with already used email")
    @allure.title("Edit Profile features with already used email")
    @allure.description("Checking edit profile if working with already used email, should not edit the profile")
    @pytest.mark.Do
    @pytest.mark.EditProfile
    def test_case_1(self, setup_initial):
        edit_profile_page = EditProfilePage(self.helper.driver)
        email = "mohdos_1999@hotmail.com"
        dob = DOB(21, 4, 1989)
        mobile = "01020304050"
        gender = "Female"
        edit_profile_page.edit_profile(email, gender, dob, mobile)
        time.sleep(2)
        if edit_profile_page.already_taken_email_appeared():
            self.helper.report_allure("Already taken message appeared")
            self.helper.driver.refresh()
            time.sleep(2)
            edit_profile_page = EditProfilePage(self.helper.driver)

        if (
                edit_profile_page.profileEmail_email_textbox.text == email and edit_profile_page.profileMobileNumber_textbox.text == mobile
                and edit_profile_page.profileGender_listbox.text == gender and edit_profile_page.profileBirthdateDay_listbox.text == dob.day
                and edit_profile_page.profileBirthdateMonth_listbox.text == dob.month
                and edit_profile_page.profileBirthdateYear_listbox.text == dob.year):
            self.helper.report_allure("Profile updated with already used email")
            assert False
        else:
            self.helper.report_allure("Profile not updated with already used email")
            assert True

    # Test #2 -> Cancelling editing profile
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Edit Profile Page")
    @allure.sub_suite("Edit Profile feature")
    @allure.title("Edit Profile features Cancel Button")
    @allure.description("Checking edit profile cancel is working")
    @pytest.mark.Do
    @pytest.mark.EditProfile
    def test_case_2(self, setup):
        edit_profile_page = EditProfilePage(self.helper.driver)
        email = "test_projectx@hotmail.com"
        dob = DOB(18, 3, 1984)
        mobile = "01020304054"
        gender = "Female"
        edit_profile_page.edit_profile(email, gender, dob, mobile, True)
        time.sleep(2)
        self.helper.driver.get(self.edit_profile_link)
        time.sleep(3)
        edit_profile_page = EditProfilePage(self.helper.driver)
        time.sleep(1)

        gender_select = Select(edit_profile_page.profileGender_listbox)
        selected_gender = gender_select.first_selected_option.text

        day_select = Select(edit_profile_page.profileBirthdateDay_listbox)
        selected_day = str(int(day_select.first_selected_option.text))

        month_select = Select(edit_profile_page.profileBirthdateMonth_listbox)
        selected_month = str(int(month_select.first_selected_option.text))

        year_select = Select(edit_profile_page.profileBirthdateYear_listbox)
        selected_year = str(int(year_select.first_selected_option.text))

        if (
                edit_profile_page.profileMobileNumber_textbox.get_attribute("value") == mobile
                and selected_gender == gender and selected_day == str(dob.day)
                and selected_month == str(dob.month)
                and selected_year == str(dob.year)):
            self.helper.report_allure("Profile updated after clicking Cancel")
            assert False
        else:
            self.helper.report_allure("Profile not updated after clicking Cancel")
            assert True

    # Test #3 -> Correctly editing profile
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Edit Profile Page")
    @allure.sub_suite("Edit Profile feature")
    @allure.title("Edit Profile features Correct")
    @allure.description("Checking edit profile if working")
    @pytest.mark.Do
    @pytest.mark.EditProfile
    def test_case_3(self, setup):
        edit_profile_page = EditProfilePage(self.helper.driver)
        email = "test_projectx@hotmail.com"
        dob = DOB(23, 3, 1991)
        mobile = "01020304054"
        gender = "Male"
        edit_profile_page.edit_profile(email, gender, dob, mobile)
        time.sleep(2)
        if edit_profile_page.success_msg_appeared():
            self.helper.report_allure("Profile Changed Successfully Message appeared")
            time.sleep(1)
            self.helper.driver.refresh()
            time.sleep(3)
            edit_profile_page = EditProfilePage(self.helper.driver)

        gender_select = Select(edit_profile_page.profileGender_listbox)
        selected_gender = gender_select.first_selected_option.text

        day_select = Select(edit_profile_page.profileBirthdateDay_listbox)
        selected_day = str(int(day_select.first_selected_option.text))

        month_select = Select(edit_profile_page.profileBirthdateMonth_listbox)
        selected_month = str(int(month_select.first_selected_option.text))

        year_select = Select(edit_profile_page.profileBirthdateYear_listbox)
        selected_year = str(int(year_select.first_selected_option.text))

        if (
                edit_profile_page.profileMobileNumber_textbox.get_attribute("value") == mobile
                and selected_gender == gender and selected_day == str(dob.day)
                and selected_month == str(dob.month)
                and selected_year == str(dob.year)):
            self.helper.report_allure("Profile updated with correct info")
            assert True
        else:
            self.helper.report_allure("Profile not updated with correct info")
            assert False

    # Test #4 -> Changing email
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Edit Profile Page")
    @allure.sub_suite("Edit Profile feature")
    @allure.title("Edit Profile Changing email")
    @allure.description("Changing spotify email in edit profile")
    @pytest.mark.Do
    @pytest.mark.EditProfile
    def test_case_4(self, setup_final):
        edit_profile_page = EditProfilePage(self.helper.driver)
        email = "mohd-1999@hotmail.com"
        dob = DOB(18, 3, 1988)
        mobile = "01020304053"
        gender = "Male"
        edit_profile_page.edit_profile(email, gender, dob, mobile)
        time.sleep(2)
        if edit_profile_page.success_msg_appeared():
            self.helper.report_allure("Profile Changed Successfully Message appeared")
            time.sleep(1)
            self.helper.driver.refresh()
            time.sleep(3)
            edit_profile_page = EditProfilePage(self.helper.driver)

        if edit_profile_page.profileEmail_email_textbox.get_attribute("value") == email:
            self.helper.report_allure("Profile updated with correct email")
            assert True
        else:
            self.helper.report_allure("Profile not updated with correct email")
            assert False

