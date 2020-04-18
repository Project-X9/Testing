from Mobile_Testing.helper import Helper


class HomePage:
    """
       A class used to represent the Home Page
       ...
       Attributes
       ----------
       logout_button_id : string
           A string containing the id of logout button

       new_releases_button_id : string
           A string containing the id of new releases button

       liked_tracks_button_id : string
           A string containing the id of liked tracks button

       popular_tracks_button_id : string
           A string containing the id of popular tracks button

       recommended_tracks_id : string
           A string containing the id of recommended tracks button

       about_button_id : string
           A string containing the id of about button

       home_button_id : string
           A string containing the id of home button

       search_button_id : string
           A string containing the id of search button

       library_button_id : string
           A string containing the id of library button

       premium_button_id : string
           A string containing the id of premium button


       Methods
       -------

       click_logout_button()
           Clicks on the logout button

       click_new_releases_button()
           Clicks on the new releases button

       click_liked_tracks_button()
           Clicks on the liked tracks button

       click_popular_tracks_button()
           Clicks on the popular tracks button

       click_recommended_tracks()
           Clicks on the recommended tracks

       click_about_button()
           Clicks on the about button

       click_home_button()
           Clicks on the home button

       click_search_button()
           Clicks on the search button

       click_library_button()
           Clicks on the library button


       click_premium_button()
           Clicks on the premium button

       """
    logout_button_id = "com.example.projectx:id/logOut"
    new_releases_button_id = "com.example.projectx:id/newReleases"
    liked_tracks_button_id = "com.example.projectx:id/likedTracks"
    popular_tracks_button_id = "com.example.projectx:id/popular"
    recommended_tracks_id = "com.example.projectx:id/recommended"
    about_button_id = "com.example.projectx:id/about"
    home_button_id = "com.example.projectx:id/navigation_home"
    search_button_id = "com.example.projectx:id/navigation_dashboard"
    library_button_id = "com.example.projectx:id/navigation_notifications"
    premium_button_id = "com.example.projectx:id/premium"


    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def click_logout_button(self):
        """
        Clicks on the logout button
        """
        element = Helper.find_element_by_id(self.driver, self.logout_button_id)
        if element is not None:
            element.click()

    def click_new_releases_button(self):
        """
        Clicks on the new releases button
        """
        element = Helper.find_element_by_id(self.driver, self.new_releases_button_id)
        if element is not None:
            element.click()

    def click_liked_tracks_button(self):
        """
        Clicks on the liked tracks button
        """
        element = Helper.find_element_by_id(self.driver, self.liked_tracks_button_id)
        if element is not None:
            element.click()

    def click_popular_tracks_button(self):
        """
        Clicks on the popular tracks button
        """
        element = Helper.find_element_by_id(self.driver, self.popular_tracks_button_id)
        if element is not None:
            element.click()

    def click_recommended_tracks(self):
        """
        Clicks on the recommended tracks
        """
        element = Helper.find_element_by_id(self.driver, self.recommended_tracks_id)
        if element is not None:
            element.click()

    def click_about_button(self):
        """
        Clicks on the about button
        """
        element = Helper.find_element_by_id(self.driver, self.about_button_id)
        if element is not None:
            element.click()

    def click_home_button(self):
        """
        Clicks on the home button
        """
        element = Helper.find_element_by_id(self.driver, self.home_button_id)
        if element is not None:
            element.click()

    def click_search_button(self):
        """
        Clicks on the search button
        """
        element = Helper.find_element_by_id(self.driver, self.search_button_id)
        if element is not None:
            element.click()

    def click_library_button(self):
        """
        Clicks on the library button
        """
        element = Helper.find_element_by_id(self.driver, self.library_button_id)
        if element is not None:
            element.click()

    def click_premium_button(self):
        """
        Clicks on the premium button
        """
        element = Helper.find_element_by_id(self.driver, self.premium_button_id)
        if element is not None:
            element.click()
