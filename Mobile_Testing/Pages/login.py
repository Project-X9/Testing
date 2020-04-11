from Mobile_Testing.helper import Helper


class LoginPage:
    email_text_field_id = "com.example.projectx:id/email_et"
    password_text_field_id = "com.example.projectx:id/password_et"
    login_button_id = "com.example.projectx:id/login_bt"

    """
    A class used to represent the Login Page
    ...
    Attributes
    ----------
    email_text_field_id : string
        id of the email text field
    password_text_field_id : string
        id of the password text field
    login_button_id : string
        id of the login button


    Methods
    -------
    fill_email()
        Fills the email field with the gievn string
        
    fill_password()
        fills the password field with the give string
    click_login()
        clicks the login password
    do_the_login()
        given an email and password this function makes a sign in 
    """

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def fill_email(self, email):
        """
        fills the email text box
        :param email : the string that is filled in the text box
        :type email: string
        """
        element = Helper.find_element_by_id(self.driver, self.email_text_field_id)
        if element is not None:
            element.send_keys(email)


    def fill_password(self, password):
        """
        fills the password text box
        :param password : the string that is filled in the text box
        :type password: string
        """
        element = Helper.find_element_by_id(self.driver, self.password_text_field_id)
        if element is not None:
            element .send_keys(password)


    def click_login(self):
        """
        clicks the login button
        """
        element = Helper.find_element_by_id(self.driver, self.login_button_id)
        if element is not None:
            element.click()

    def do_the_login(self, email, password):
        """
        makes a login process
        :param email : the string that is filled in the text box
        :type email: string
        :param password : the string that is filled in the text box
        :type password: string
        """
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()
