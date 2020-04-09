import time

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.helperClasses import WebHelper


class ChangePasswordPage(WebHelper):
    def __init__(self, driver):
        self.set_driver(driver)
        self.password_txt = self.find_element_by_id("password")
        self.confirm_password_txt = self.find_element_by_id("confirmPassword")
        self.change_password_btn = self.find_element_by_xpath("//button[text()='Change Password']")

    def clear_all(self):
        """
        clears all text fields in the page
        """
        self.clear_txt_safe(self.password_txt)
        self.clear_txt_safe(self.confirm_password_txt)

    def is_dangers_visible(self) -> bool:
        """
        checks if text dangers/warnings are visible

        :returns: a boolean True if visible, False otherwise
        :rtype: bool
        """
        danger_1 = self.find_element_by_xpath("//span[text()='Your password is too short']")
        danger_2 = self.find_element_by_xpath("//span[contains(text(),'Enter your password to continue,')]")
        danger_3 = self.find_element_by_xpath("//span[text()='Password does not match']")
        return (danger_1 is not None) or (danger_2 is not None) or (danger_3 is not None)

    def change_password(self, new_password, confirm_password) -> bool:
        """
        changes the user's password

        :param new_password: the new password of the user
        :type new_password: str

        :param confirm_password: the confirmation password
        :type confirm_password: str

        :returns: a boolean True if succeeded to change password, False otherwise
        :rtype: bool
        """
        self.clear_all()

        self.fill(self.password_txt, new_password)
        self.fill(self.confirm_password_txt, confirm_password)
        self.change_password_btn.click()
        time.sleep(3)
        dangers_visible = self.is_dangers_visible()

        return not dangers_visible



