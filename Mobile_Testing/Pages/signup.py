from Mobile_Testing.helper import Helper


class SignupPage:

    name_text_field_id = "com.example.projectx:id/signUpName_et"
    email_text_field_id = "com.example.projectx:id/signUpEmail_et"
    password_text_field_id = "com.example.projectx:id/signUpPassword_et"
    age_text_field_id = "com.example.projectx:id/signUpAge_et"
    male_gender_check_box_id = "com.example.projectx:id/signUpMale_rb"
    female_gender_check_box_id = "com.example.projectx:id/signUpFemale_rb"
    create_user_button_id = "com.example.projectx:id/createUser_bt"

    def __init__(self, driver):
        self.driver = driver

    def fill_name(self, name):
        Helper.find_element_by_id(self.driver, self.name_text_field_id).send_keys(name)

    def fill_email(self, email):
        Helper.find_element_by_id(self.driver, self.email_text_field_id).send_keys(email)

    def fill_password(self, password):
        Helper.find_element_by_id(self.driver, self.password_text_field_id).send_keys(password)

    def fill_age(self, age):
        Helper.find_element_by_id(self.driver, self.age_text_field_id).send_keys(age)

    def choose_male(self):
        Helper.find_element_by_id(self.driver, self.male_gender_check_box_id).click()

    def choose_female(self):
        Helper.find_element_by_id(self.driver, self.female_gender_check_box_id).click()

    def click_create_user(self):
        Helper.find_element_by_id(self.driver, self.create_user_button_id).click()

    def do_the_signup(self, name, email, password, age, gender):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_age(age)
        if gender == "M":
            self.choose_male()
        else:
            self.choose_female()

        self.click_create_user()