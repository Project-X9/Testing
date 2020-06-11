from Mobile_Testing.helper import Helper
import time


class LibraryPage:
    """
    A class used to represent the Library Page
    ...
    Attributes
    ----------

    playlists_tab_xpath : string
        xpath for the playlists tab
    artists_xpath : string
        xpath for the artists tab
    albums_xpath : string
        xpath of the albums tab


    Methods
    -------

        open_playlists()
            opens playlists tab
        open_artists()
            opens artists tab
        open_albums()
            opens albums tab


    """

    playlists_tab_xpath = "//androidx.appcompat.app.ActionBar.Tab[@content-desc='Playlist']/android.widget.TextView"
    artists_xpath = "//androidx.appcompat.app.ActionBar.Tab[@content-desc='Artist']"
    albums_xpath = "//androidx.appcompat.app.ActionBar.Tab[@content-desc='Albums']/android.widget.TextView"


    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def open_playlists(self):
        """
            opens playlists tab
        """
        element = Helper.find_element_by_xpath(self.driver, self.playlists_tab_xpath)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def open_artists(self):
        """
            opens artists tab
        """
        element = Helper.find_element_by_xpath(self.driver, self.artists_xpath)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def open_albums(self):
        """
            opens albums tab
        """
        element = Helper.find_element_by_xpath(self.driver, self.albums_xpath)
        if element is None:
            return False
        else:
            element.click()
            return True