from Mobile_Testing.helper import Helper


class AuthenticationPage:
    signup_button_id = "com.example.projectx:id/signUp_bt"
    login_with_facebook_button_id = "com.example.projectx:id/login_button"
    signin_button_id = "com.example.projectx:id/signIn_bt"
    """
    A class used to represent the Authentication Page
    ...
    Attributes
    ----------

    signup_button_id : string
        A string containing the id of Sign up button
    login_with_facebook_button_id : string
        A string containing the id of login with facebook button
    signin_button_id : string
        A string containing the id of sign in button

    Methods
    -------
    click_signup_button()
        Clicks the sign up button
    click_login_with_facebook_button()
        Clicks the login with facebook button
    click_signin_button()
        Clicks the sign in button 
        
    """

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def click_signup_button(self):
        """
        Clicks sign up button
        """
        Helper.find_element_by_id(self.driver, self.signup_button_id).click()

    def click_login_with_facebook_button(self):
        """
        Clicks login with facebook  button
        """
        Helper.find_element_by_id(self.driver, self.login_with_facebook_button_id).click()

    def click_signin_button(self):
        """
        Clicks sign in button
        """
        Helper.find_element_by_id(self.driver, self.signin_button_id).click()