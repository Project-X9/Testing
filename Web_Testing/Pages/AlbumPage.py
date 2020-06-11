import time

from Web_Testing.helperClasses import WebHelper


class AlbumPage(WebHelper):
    """
    A class used to represent Album Page
    ...

    Methods
    ----------
    add_album_to_library()
        Adds the album (which is in the current album page) to your library
    remove_album_from_library()
        Removes the album (which is in the current album page) from your library
    assert_albums_has(name: str)
        Checks if Your Library Albums has the given album name
    """
    def __init__(self, driver):
        """
        Initializes the class elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.driver = driver


    def add_album_to_library(self):
        """
        Adds the album (which is in the current album page) to your library
        """
        menu_btn = self.find_elements_by_xpath("//div[@class='spoticon-ellipsis-32']")
        self.hover_to_element(menu_btn[0])
        menu_btn[0].click()
        time.sleep(2)
        save_to_library_btn = self.find_element_by_xpath("//span[text()='Save to Your Library']")
        save_to_library_btn.click()
        time.sleep(3)

    def remove_album_from_library(self):
        """
        Removes the album (which is in the current album page) from your library
        """
        menu_btn = self.find_element_by_xpath("//div[@class='spoticon-ellipsis-32']")
        self.hover_to_element(menu_btn)
        menu_btn.click()
        time.sleep(2)
        save_to_library_btn = self.find_element_by_xpath("//span[text()='Remove from Your Library']	")
        save_to_library_btn.click()
        time.sleep(3)

    def assert_albums_has(self, name: str):
        """
        Checks if Your Library Albums has the given album name
        :param name: the album name to be checked
        :type name: str
        :returns: True if it finds the album with the given name in the library, False otherwise
        :rtype: bool
        """
        cards = self.find_elements_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[2]/div[4]/div[1]/div[1]/div[2]/section[1]/div[1]")
        if cards is None or len(cards) == 0:
            return False
        for card in cards:
            cards_splitted = card.text.split("\n")
            card_text = cards_splitted[0]
            if card_text.lower() == name.lower():
                return True

        return False

