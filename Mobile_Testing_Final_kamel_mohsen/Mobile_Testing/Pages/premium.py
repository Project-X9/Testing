from Mobile_Testing.helper import Helper


class PremiumPage:
    """
       A class used to represent the Premium Page
       ...
       Attributes
       ----------

        free_plan_box_xpath : string
           A string containing the xpath of free plan box

        premium_individual_box_xpath : string
           A string containing the xpath of premium individual box

        ad_break_box_xpath : string
           A string containing the xpath of ad break box

        play_in_shuffle_box_xpath : string
           A string containing the xpath of play in shuffle box

        unlimited_skips_box_xpath : string
           A string containing the xpath of unlimited skips box

        offline_listening_box_xpath : string
           A string containing the xpath of offline listening box

        high_audio_quality_box_xpath : string
           A string containing the xpath of high audio quality box

        get_premium_button_xpath : string
           A string containing the xpath of get premium button

        confirm_cancel_id : string
            id of the confirm cancel get premium
        profile_button_id : ""
            id of the profile button
       Methods
       -------


        check_free_box()
            checks the free plan box
        check_premium_individual_box()
            checks the premium individual box
        check_ad_break_box()
           checks ad break box
        check_play_in_shuffle_box()
            checks play in shuffle box
        check_unlimited_skips_box()
            checks unlimited skips box
        check_offline_listening_box()
            checks offline listening box
        check_high_audio_quality_box()
            checks high audio quality box
        check_get_premium_button()
            clicks get premium button and checks that it exists
        cancel_get_premium()
            cancel or get premium

       """

    free_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]"
    premium_individual_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]"
    ad_break_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    play_in_shuffle_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    unlimited_skips_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    offline_listening_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    high_audio_quality_box_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]"
    get_premium_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button"
    confirm_cancel_id = "android:id/button1"
    profile_button_id = "com.example.projectx:id/settings_ib"

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver

    def check_free_box(self):
        """
        checks the free plan box
        """
        element = Helper.find_element_by_xpath(self.driver, self.free_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_premium_individual_box(self):
        """
        checks the premium individual box
        """
        element = Helper.find_element_by_xpath(self.driver, self.premium_individual_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_ad_break_box(self):
        """
        checks ad break box
        """
        element = Helper.find_element_by_xpath(self.driver, self.ad_break_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_play_in_shuffle_box(self):
        """
        checks play in shuffle box
        """
        element = Helper.find_element_by_xpath(self.driver, self.play_in_shuffle_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_unlimited_skips_box(self):
        """
        checks unlimited  skips box
        """
        element = Helper.find_element_by_xpath(self.driver, self.unlimited_skips_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_offline_listening_box(self):
        """
        checks offline listening box
        """
        element = Helper.find_element_by_xpath(self.driver, self.offline_listening_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_high_audio_quality_box(self):
        """
        checks high audio quality box
        """
        element = Helper.find_element_by_xpath(self.driver, self.high_audio_quality_box_xpath)
        if element is not None:
            return True
        else:
            return False

    def check_get_premium_button(self):
        """
        clicks get premium button and checks that it exists
        """
        element = Helper.find_element_by_xpath(self.driver, self.get_premium_button_xpath)
        if element is not None:
            element.click()
            return True
        else:
            return False

    def cancel_get_premium(self):
        """
        cancel/gets premium
        """
        element = Helper.find_element_by_xpath(self.driver, self.get_premium_button_xpath)
        if element is None:
            return False
        element.click()
        element = Helper.find_element_by_id(self.driver, self.confirm_cancel_id)
        if element is None:
            return False
        else:
            element.click()
            return True

    def enter_profile(self):
        """
        enters profile page
        """
        element = Helper.find_element_by_id(self.driver, self.profile_button_id)
        if element is None:
            return False
        else:
            element.click()
            return True
