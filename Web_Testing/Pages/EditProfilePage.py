import time

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.helperClasses import WebHelper, DOB


class EditProfilePage(WebHelper):
    """
    A class used to represent Edit Profile Page
    ...

    Attributes
    ----------
    cancel_link : WebDriver Element
        A web element that represents the cancel button
    saveProfile_button : WebDriver Element
        A web element that represents the Save button
    profileMobileNumber_textbox : WebDriver Element
        A web element that represents the Mobile Number text field
    profileCountry_listbox : WebDriver Element
        A web element that represents the Country drop down
    profileBirthdateYear_listbox : WebDriver Element
        A web element that represents the Birthday year drop down
    profileBirthdateDay_listbox : WebDriver Element
        A web element that represents the Birthday day drop down
    profileBirthdateMonth_listbox : WebDriver Element
        A web element that represents the Birthday month drop down
    profileGender_listbox : WebDriver Element
        A web element that represents the gender drop down
    weReSorryThat_any : WebDriver Element
        A web element that represents the error message
    profileEmail_email_textbox : WebDriver Element
        A web element that represents the email text field
    confirm_password : WebDriver Element
        A web element that represents the Confirm Password text field

    Methods
    -------
    already_taken_email_appeared()
        Checks if the error message appeared
    clear_all()
        Clears the Mobile Number and Email text fields
    success_msg_appeared()
        Checks if the success message appeared
    edit_profile(email: str, gender: str, dob: DOB, phone: str)
        Edits the profile with the new given parameters
    """

    def __init__(self, driver):
        """
        Initializes the class elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.cancel_link = self.find_element_by_xpath("//a[text()='Cancel']")
        self.saveProfile_button = self.find_element_by_xpath("//button[text()='Save profile']")
        self.profileMobileNumber_textbox = self.find_element_by_xpath(
            "//input[@type='text'][@name='profile[mobile][number]']")
        self.profileCountry_listbox = self.find_element_by_xpath("//select[@name='profile[country]']")
        self.profileBirthdateYear_listbox = self.find_element_by_xpath("//select[@name='profile[birthdate][year]']")
        self.profileBirthdateDay_listbox = self.find_element_by_xpath("//select[@name='profile[birthdate][day]']")
        self.profileBirthdateMonth_listbox = self.find_element_by_xpath("//select[@name='profile[birthdate][month]']")
        self.profileGender_listbox = self.find_element_by_xpath("//select[@name='profile[gender]']")
        self.weReSorryThat_any = self.find_element_by_xpath("has-error control-label-validation")
        self.profileEmail_email_textbox = self.find_element_by_xpath("//input[@type='email'][@name='profile[email]']")
        self.confirm_password = self.find_element_by_id("profile_confirmPassword")

    def already_taken_email_appeared(self) -> bool:
        """
        Checks if the error message appeared
        :returns: True if the error message appeared, False otherwise
        :rtype: bool
        """
        return self.find_elements_by_class_name("has-error control-label-validation") is not None

    def clear_all(self):
        """
        Clears the Mobile Number and Email text fields
        """
        self.clear_txt_safe(self.profileEmail_email_textbox)
        self.clear_txt_safe(self.profileMobileNumber_textbox)

    def success_msg_appeared(self) -> bool:
        """
        Checks if the success message appeared
        :returns: True if the success message appeared, False otherwise
        :rtype: bool
        """
        return self.find_element_by_xpath("//p[text()='Profile saved']") is not None

    def edit_profile(self, email: str, gender: str, dob: DOB, phone: str, cancel: bool = False):
        """
        Edits the profile with the new given parameters

        :param email: the new email
        :type email: str

        :param gender: the new gender
        :type gender: str

        :param dob: the new birth date
        :type dob: DOB

        :param cancel: Should the edit be cancelled or confirmed
        :type cancel: bool

        :param phone: the new phone number
        :type phone: str
        """
        spotify_email = self.profileEmail_email_textbox.text.lower()
        new_email = email.lower()
        self.clear_all()
        if spotify_email != new_email:
            self.fill(self.profileEmail_email_textbox, email)
            self.fill_safe(self.confirm_password, "TestingTeamMKE")
        self.select_element_by_text(self.profileGender_listbox, gender)
        self.select_element_by_index(self.profileBirthdateDay_listbox, dob.day-1)
        self.select_element_by_index(self.profileBirthdateMonth_listbox, dob.month-1)
        self.select_element_by_text(self.profileBirthdateYear_listbox, str(dob.year))
        self.fill(self.profileMobileNumber_textbox, phone)
        # time.sleep(2)
        # self.fill_safe(self.confirm_password, "TestingTeamMKE")
        if not cancel:
            self.click_button(self.saveProfile_button)
        else:
            self.click_button(self.cancel_link)
        # self.fill(self.username_text, username)
        # self.fill(self.email_text, email)
        # self.fill(self.age_text, str(age))
        #
        # self.save_changes_btn.click()

