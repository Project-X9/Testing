from Mobile_Testing.helper import Helper
import time


class AlbumPage:
    """
    A class used to represent the Albums/Album Page
    ...
    Attributes
    ----------

    first_album_xpath : string
        xpath for the first album
    first_song_xpath : string
        xpath for the first song
    heart_button_id : string
        id of the like button
    share_button_id : string
        id for the share button

    Methods
    -------

    open_first_album()
        opens first album
    open_first_song()
        opens first song
    check_like_button()
        checks the like button exists
    check_share_button()
        checks the share button exists

    """
    first_album_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout"
    first_song_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.RelativeLayout"
    heart_button_id = "com.example.projectx:id/likeButton2_ib"
    share_button_id = "com.example.projectx:id/sharePlaylist_ibt"

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def open_first_album(self):
        """
            opens first album
        """
        element = Helper.find_element_by_xpath(self.driver, self.first_album_xpath)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def open_first_song(self):
        """
        opens first song
        """
        time.sleep(1)
        element = Helper.find_element_by_xpath(self.driver, self.first_album_xpath)
        if element is None:
            return False
        time.sleep(1)
        element.click()
        time.sleep(1)
        element = Helper.find_element_by_xpath(self.driver, self.first_song_xpath)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def check_like_button(self):
        """
        checks the like button exists
        """
        time.sleep(1)
        element = Helper.find_element_by_xpath(self.driver, self.first_album_xpath)
        if element is None:
            return False
        time.sleep(1)
        element.click()
        time.sleep(1)
        element = Helper.find_element_by_id(self.driver, self.heart_button_id)
        if element is not None:
            return True
        else:
            return False

    def check_share_button(self):
        """
        checks the share button exists
        """
        time.sleep(2)
        element = Helper.find_element_by_xpath(self.driver, self.first_album_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.share_button_id)
        if element is not None:
            return True
        else:
            return False