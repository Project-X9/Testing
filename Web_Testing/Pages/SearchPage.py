import time

from Web_Testing.helperClasses import WebHelper


class SearchPage(WebHelper):

    """
    A class used to represent Search Page
    ...

    Attributes
    ----------
    search_bar : WebDriver Element
        A web element that represents the search text field
    ...

    Methods
    ----------
    is_song()
        Checks if the results returned a song
    is_artist()
        Checks if the results returned an artist
    get_search_result()
        Gets the search results
    search_for(text: str, type: str)
        Searches for a given text and type (song or artist)
    """

    def __init__(self, driver):
        """
        Initializes the class elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.search_bar = self.find_element_by_xpath("//*[@placeholder='Search for Artists, Songs, or Podcasts']")

    def is_song(self):
        """
        Checks if the results returned a song
        :returns: True if the results returned a song, False otherwise
        :rtype: bool
        """
        return self.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[2]/div").text.find("SONG") != -1

    def is_artist(self):
        """
        Checks if the results returned an artist
        :returns: True if the results returned an artist, False otherwise
        :rtype: bool
        """
        return self.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[2]/div").text.find("ARTIST") != -1

    def get_search_result(self) -> str:
        """
        Gets the search results
        :returns: The top search result
        :rtype: str
        """
        self.top_search = self.find_elements_by_xpath(
        "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[2]")
        return self.top_search[0].text

    def search_for(self, text: str, type: str):
        """
        Searches for a given text and type (song or artist)

        :param text: the text to search for
        :type text: str

        :param type: the type of search (Song or Artist)
        :type type: str

        :returns: True if the search results were relevant, False otherwise
        :rtype: bool
        """
        self.clear_txt_safe(self.search_bar)
        self.fill(self.search_bar, text)
        time.sleep(2)
        top_result = self.get_search_result()

        if type.lower() == "artist":
            if not self.is_artist():
                self.report_allure("Searched for an artist but the search result did not get artist")
        else:
            if not self.is_song():
                self.report_allure("Searched for an artist but the search result did not get artist")

        # print("Top result = " + top_result)
        if top_result.lower().find(text.lower()) != -1 or text.lower().find(top_result.lower()) != -1:
            return True
        else:
            return False

