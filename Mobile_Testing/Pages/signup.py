from Mobile_Testing.helper import Helper


class SignupPage:

    name_text_field_id = "com.example.projectx:id/signUpName_et"
    email_text_field_id = "com.example.projectx:id/signUpEmail_et"
    password_text_field_id = "com.example.projectx:id/signUpPassword_et"
    age_text_field_id = "com.example.projectx:id/signUpAge_et"
    male_gender_check_box_id = "com.example.projectx:id/signUpMale_rb"
    female_gender_check_box_id = "com.example.projectx:id/signUpFemale_rb"
    create_user_button_id = "com.example.projectx:id/createUser_bt"

    """
    A class used to represent the Sign up Page
    ...
    Attributes
    ----------
    
    name_text_field_id : string
        id of the name text box
    email_text_field_id : string
        id of the email text box
    password_text_field_id : string
        id of the password text box
    age_text_field_id : string
        id of the age text box
    male_gender_check_box_id : string
        id of the male check box
    female_gender_check_box_id : string
        id of the female check box
    create_user_button_id : string
        id of the create user button

    Methods
    -------
    fill_name()
        fills name text box
    fill_email()
        fills email text box
    fill_password()
        fills password text box 
    fill_age()
        fills age check box
    choose_male()
        choose male checkbox
    choose_female()
        choose female checkbox

    click_create_user()
        clicks the create button
    do_the_signup()
        does the whole signup process
    """
    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def fill_name(self, name):
        """
        fills the name text box
        :param name : the string that is filled in the text box
        :type name: string
        """
        Helper.find_element_by_id(self.driver, self.name_text_field_id).send_keys(name)

    def fill_email(self, email):
        """
        fills the email text box
        :param email : the string that is filled in the text box
        :type email: string
        """
        Helper.find_element_by_id(self.driver, self.email_text_field_id).send_keys(email)

    def fill_password(self, password):
        """
        fills the password text box
        :param password : the string that is filled in the text box
        :type password: string
        """
        Helper.find_element_by_id(self.driver, self.password_text_field_id).send_keys(password)

    def fill_age(self, age):
        """
        fills the age text box
        :param age : the int that is filled in the text box
        :type age: int
        """
        Helper.find_element_by_id(self.driver, self.age_text_field_id).send_keys(age)

    def choose_male(self):
        """
        chooses male gender
        """
        Helper.find_element_by_id(self.driver, self.male_gender_check_box_id).click()

    def choose_female(self):
        """
        chooses female gender
        """
        Helper.find_element_by_id(self.driver, self.female_gender_check_box_id).click()

    def click_create_user(self):
        """
        clicks create user button
        """
        Helper.find_element_by_id(self.driver, self.create_user_button_id).click()

    def do_the_signup(self, name, email, password, age, gender):
        """
        does the whole sign up process using given info
        :param name : the string that is filled in the text box
        :type name: string
        :param email : the string that is filled in the text box
        :type email: string
        fills the password text box
        :param password : the string that is filled in the text box
        :type password: string
         fills the age text box
        :param age : the int that is filled in the text box
        :type age: int
        :param gender : the gender chosen
        :type age: string
        """
        self.fill_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_age(age)
        if gender == "M":
            self.choose_male()
        elif gender == "F":
            self.choose_female()

        self.click_create_user()
