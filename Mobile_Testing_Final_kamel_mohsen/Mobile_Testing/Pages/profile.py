from Mobile_Testing.helper import Helper
import time

class ProfilePage:
    """
       A class used to represent the Profile Page
       ...
       Attributes
       ----------

        edit_profile_button_id : string
            edit profile button id
        first_play_list_xpath : string
            first playlist xpath
        notifications_check_id : string
            notification check box id
        change_name_button : string
            change name button _xpath
        change_password_button : string
            change password button _xpath
        change_email_button_xpath : string
            change email button _xpath
        change_name_textbox_id : string
            change name textbox id
        change_name_confirm_id : string
            change name confirm id
        change_name_cancel_id : string
            change name cancel id
        change_password_textbox_id : string
            change password textbox id
        change_password_confirm_id : string
            change password confirm id
        change_password_cancel_id : string
            change password confirm id
        change_email_textbox_id : string
            change email textbox id
        change_email_confirm_id : string
            change email confirm id
        change_email_cancel_id : string
            change email cancel id


       Methods
       -------


        check_edit_profile_button()
            checks the edit profile exists
        check_first_playlist()
            checks the first playlist exists
        check_notifications()
            checks the notifications checkbox is clickable
        check_change_user_name_button()
            checks change user name button
        check_change_user_password_button()
            checks change user password button
        check_change_user_email_button()
            checks change user email button
        change_name()
            changes the user name
        change_the_password()
            changes the user name password
        change_the_email()
            change the user email

       """

    edit_profile_button_id = "com.example.projectx:id/edit_button_bt"
    first_play_list_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup"
    notifications_check_id = "android:id/checkbox"
    change_name_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout"
    change_password_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView[1]"
    change_email_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.RelativeLayout"
    change_name_textbox_id = "android:id/edit"
    change_name_confirm_id = "android:id/button1"
    change_name_cancel_id = "android:id/button2"
    change_password_textbox_id = "android:id/edit"
    change_password_confirm_id = "android:id/button1"
    change_password_cancel_id = "android:id/button2"
    change_email_textbox_id = "android:id/edit"
    change_email_confirm_id = "android:id/button1"
    change_email_cancel_id = "android:id/button2"

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver


    def check_edit_profile_button(self):
        """     checks the edit profile exists   """
        element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def check_first_playlist(self):
        """checks the first playlist exists"""
        element = Helper.find_element_by_xpath(self.driver, self.first_play_list_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_notifications(self):
        """checks the notifications checkbox is clickable"""
        element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
        if element is None:
            return False
        time.sleep(5)
        element.click()
        element = Helper.find_element_by_id(self.driver, self.notifications_check_id)
        if element is None:
            return False
        else:
            return True
    def check_change_user_name_button(self):
        """checks change user name button"""
        element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
        if element is None:
            return False
        time.sleep(5)
        element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_name_button_xpath)
        if element is None:
            return False
        else:
            return True

    def check_change_user_password_button(self):
        """checks change user password button"""
        element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
        if element is None:
            return False
        time.sleep(5)
        element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_password_button_xpath)
        if element is None:
            return False
        else:
            return True

    def check_change_user_email_button(self):
        """checks change user name button"""
        element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
        if element is None:
            return False
        time.sleep(5)
        element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_email_button_xpath)
        if element is None:
            return False
        else:
            return True

    def change_name(self, name,choice):
        """changes the user name"""
        if choice is "or":
            element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
            if element is None:
                return False
            time.sleep(5)
            element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_name_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.change_name_textbox_id)
        if element is None:
            return False
        element.click()
        element.clear()
        element.send_keys(name)
        element = Helper.find_element_by_id(self.driver, self.change_name_confirm_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.notifications_check_id)
        if element is not None:
            return True
        else:
            return False

    def change_the_password(self, password,choice):
        """changes the user name password"""
        if choice is "or":
            element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
            if element is None:
                return False
            time.sleep(5)
            element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_password_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.change_password_textbox_id)
        if element is None:
            return False
        element.click()
        element.clear()
        element.send_keys(password)
        element = Helper.find_element_by_id(self.driver, self.change_password_confirm_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.notifications_check_id)
        if element is not None:
            return True
        else:
            return False

    def change_the_email(self, email,choice):
        """change the user email"""
        if choice is "or":
            element = Helper.find_element_by_id(self.driver, self.edit_profile_button_id)
            if element is None:
                return False
            time.sleep(5)
            element.click()
        element = Helper.find_element_by_xpath(self.driver, self.change_email_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.change_email_textbox_id)
        if element is None:
            return False
        element.click()
        element.clear()
        element.send_keys(email)
        element = Helper.find_element_by_id(self.driver, self.change_email_confirm_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.notifications_check_id)
        if element is not None:
            return True
        else:
            return False