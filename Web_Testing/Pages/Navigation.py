from Web_Testing.helperClasses import WebHelper


class Navigation(WebHelper):

    """
    A class representing the Web Player Navigation
    ...

    Attributes
    ----------
    back_btn : WebDriver Element
        A web element that represents the back button
    forward_btn : WebDriver Element
        A web element that represents the forward button

    Methods
    -------
    click_back()
        Clicks on the back button
    click_forward()
        Clicks on the forward button
    """

    def __init__(self, driver):
        """
        Initializes the class elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.back_btn = self.find_element_by_xpath("//button[@title='Go back']")
        self.forward_btn = self.find_element_by_xpath("//button[@title='Go forward']")

    def click_back(self):
        """
        Clicks on the back button
        """
        self.click_button(self.back_btn)

    def click_forward(self):
        """
        Clicks on the forward button
        """
        self.click_button(self.forward_btn)

