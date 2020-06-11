from Mobile_Testing.helper import Helper
from appium.webdriver.common.touch_action import TouchAction
import time


class PlayList:
    """
    A class used to represent the Play List Page
    ...
    Attributes
    ----------

    create_playlist_textbox_id : string
        xpath of the text box for new playlist
    create_album_button_xpath : string
        xpath of the create album button
    first_element_xpath : string
        xpath of the first play list in the play lists
    save_new_playlist_button_id: string
        id of the create/save button of the create new playlist popup
    cancel_creation_button_id: string
        id of the cancel button of the create new playlist popup
    edit_button_id : string
        id of the edit button
    like_button_id : string
        id of the like button
    share_button_id : string
        id of the share button
    add_song_button_id : string
        id of the add song button in edit playlist
    edit_playlist_button_id : string
        id of the edit palylist button
    first_song_in_edit_xpath : string
        xpath of the first song in the edit view
    rename_box_id  : string
        id of the rename box in edit playlist
    cancel_rename_id  : string
        cancel button id in the rename playlist
    rename_id  : string
        rename button id in the playlist rename
    delete_track_id : string
        delete track button id
    Methods
    -------

    create_button()
        Checks that the create button exists
    first_element()
        Checks that the first element exists
    cancel_button()
        Checks that the cancel button exists
    save_button()
        Checks that the save button exists
    create_new_playlist()
        Goes thought the whole process of creating a new playlist

    check_edit_button()
        Checks that the edit button exists and is click-able
    check_like_button()
        Checks that the like button exists and is click-able
    check_share_button()
        Checks that the share button exists and is click-able
    check_add_song()
        checks add song button in edit playlist
    edit_playlist()
       checks the edit playlist button
    first_song_in_edit()
        checks the first song in edit playlist
    cancel_rename()
        checks the cancel button in playlist rename
    rename()
        checks the rename button in the rename playlist
    delete_track()
        checks the delete track button

    """
    create_playlist_textbox_id = "com.example.projectx:id/playlistName_tiet"
    create_album_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.TextView"
    first_element_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView[1]"
    save_new_playlist_button_id = "com.example.projectx:id/createRename_tv"
    cancel_creation_button_id = "com.example.projectx:id/cancel_tv"
    edit_button_id = "com.example.projectx:id/editPlaylist_button_bt"
    like_button_id = "com.example.projectx:id/likeButton2_ib"
    share_button_id = "com.example.projectx:id/sharePlaylist_ibt"
    add_song_button_id = "com.example.projectx:id/button"
    edit_playlist_button_id = "com.example.projectx:id/editPlaylist_ibt"
    first_song_in_edit_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout"
    rename_box_id = "com.example.projectx:id/playlistName_tiet"
    cancel_rename_id = "com.example.projectx:id/cancel_tv"
    rename_id = "com.example.projectx:id/createRename_tv"
    delete_track_id = "android:id/text1"
    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def create_button(self):
        """
        checks that the create button exists
        """
        element = Helper.find_element_by_xpath(self.driver, self.create_album_button_xpath)
        if element is not None:
            return True
        else:
            return False

    def first_element(self):
        """
        checks that the first playlist exists
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is not None:
            return True
        else:
            return False

    def cancel_button(self):
        """
        checks that the cancel button exists
        """
        element = Helper.find_element_by_xpath(self.driver, self.create_album_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.cancel_creation_button_id)
        if element is not None:
            return True
        else:
            return False

    def save_button(self):
        """
        checks that the save button exists
        """
        element = Helper.find_element_by_xpath(self.driver, self.create_album_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.save_new_playlist_button_id)
        if element is not None:
            return True
        else:
            return False

    def create_new_playlist(self, playlist_name):
        """
        goes through the whole process of playlist creation
        :param playlist_name : the string that is filled in the text box for the new play list
        :type playlist_name: string
        """
        element = Helper.find_element_by_xpath(self.driver, self.create_album_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.create_playlist_textbox_id)
        if element is None:
            return False
        element.click()
        element.send_keys(playlist_name)
        element = Helper.find_element_by_id(self.driver, self.save_new_playlist_button_id)
        if element is None:
            return False
        else:
            element.click()
            return True

    def check_edit_button(self):
        """
        Checks that the edit button exists and is click-able
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        else:
            return True

    def check_like_button(self):
        """
        Checks that the like button exists and is click-able
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.like_button_id)
        if element is None:
            return False
        else:
            return True

    def check_share_button(self):
        """
        Checks that the share button exists and is click-able
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.share_button_id)
        if element is None:
            return False
        else:
            return True

    def check_add_song(self):
        """
        checks add song button in edit playlist
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.add_song_button_id)
        if element is None:
            return False
        else:
            return True

    def edit_playlist(self):
        """
        checks the edit playlist button
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_playlist_button_id)
        if element is None:
            return False
        else:
            return True

    def first_song_in_edit(self):
        """
        checks the first song in edit playlist
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_xpath(self.driver, self.first_song_in_edit_xpath)
        if element is None:
            return False
        else:
            return True

    def cancel_rename(self):
        """
        checks the first song in edit playlist
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_playlist_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.cancel_rename_id)
        if element is None:
            return False
        else:
            return True

    def rename(self):
        """
        checks the rename button in the rename playlist
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_playlist_button_id)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.rename_id)
        if element is None:
            return False
        else:
            return True

    def delete_track(self):
        """
        checks the delete track button
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_element_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.edit_button_id)
        if element is None:
            return False
        element.click()
        time.sleep(2)
        element = Helper.find_element_by_xpath(self.driver, self.first_song_in_edit_xpath)
        if element is None:
            return False
        time.sleep(2)
        actions = TouchAction(self.driver)
        actions.long_press(element)
        actions.perform()
        element = Helper.find_element_by_id(self.driver, self.delete_track_id)
        if element is None:
            return False
        else:
            return True


