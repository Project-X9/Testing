import time

from Web_Testing.Pages.AccountOverviewPage import AccountOverviewPage
from Web_Testing.helperClasses import WebHelper


class EditProfilePage(WebHelper):

    def __init__(self, driver):
        self.email_text = self.find_element_by_id("email")
        self.username_text = self.find_element_by_id("ID")
        self.age_text = self.find_element_by_id("age")
        self.cancel_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[4]/div[1]/button/a")
        self.save_changes_btn = self.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[4]/div[2]/button")

    def clear_all(self):
        self.clear_txt_safe(self.email_text)
        self.clear_txt_safe(self.username_text)
        self.clear_txt_safe(self.age_text)

    def edit_profile(self, username: str, email: str, age: int):
        self.fill(self.username_text, username)
        self.fill(self.email_text, email)
        self.fill(self.age_text, str(age))

        self.save_changes_btn.click()


