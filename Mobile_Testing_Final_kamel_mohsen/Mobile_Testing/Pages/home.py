from Mobile_Testing.helper import Helper


class HomePage:
    """
       A class used to represent the Home Page
       ...
       Attributes
       ----------

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


       click_home_button()
           Clicks on the home button

       click_search_button()
           Clicks on the search button

       click_library_button()
           Clicks on the library button

       click_premium_button()
           Clicks on the premium button

       """

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
