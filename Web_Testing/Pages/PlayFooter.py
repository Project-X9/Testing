import time

from Web_Testing.helperClasses import WebHelper, CustomTime


class PlayFooter(WebHelper):
    """
    A class used to represent Play Footer
    ...

    Attributes
    ----------
    pictureInPictureButtonControlButton_button : WebDriver Element
        A web element that represents the Picture in Picture button
    playbackBarProgressTime_div : WebDriver Element
        A web element that represents the Progress Times
    queue_button : WebDriver Element
        A web element that represents the queue button
    enableShuffle_button : WebDriver Element
        A web element that represents the enable shuffle button
    enableRepeat_button : WebDriver Element
        A web element that represents the enable repeat button
    play_pause_btn : WebDriver Element
        A web element that represents the Play/Pause button
    next_song_btn : WebDriver Element
        A web element that represents the next song button
    prev_song_btn : WebDriver Element
        A web element that represents the previous song button

    Methods
    -------
    click_song()
        Clicks on a song to start playing
    click_play_or_pause()
        Clicks on the Play/Pause button
    click_queue()
        Clicks on the Queue button
    get_song_name()
        Gets the currently playing song name
    get_artist_name()
        Gets the artist name of the currently playing song
    get_consumed_time()
        Gets the consumed time of the currently playing song
    get_remaining_time()
        Gets the remaining time of the currently song
    click_next_song()
        Clicks on the next song button
    click_prev_song()
        Clicks on the previous song button

    """

    def __init__(self, driver):
        """
        Initializes the class elements

        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        super().__init__()
        self.set_driver(driver)
        self.pictureInPictureButtonControlButton_button = self.find_element_by_class_name(
            "picture-in-picture-button control-button")
        self.playbackBarProgressTime_div = self.find_elements_by_class_name("playback-bar__progress-time")
        self.queue_button = self.find_element_by_xpath("//button[@title='Queue']")
        self.enableShuffle_button = self.find_element_by_xpath("//button[@title='Enable shuffle']")
        self.enableRepeat_button = self.find_element_by_xpath("//button[@title='Enable repeat']")
        self.play_pause_btn = self.find_element_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[3]/div[3]/footer[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
        self.next_song_btn = self.find_element_by_xpath("//button[@title='Next']")
        self.prev_song_btn = self.find_element_by_xpath("//button[@title='Previous']")

    def click_song(self):
        """
        Clicks on a song to start playing
        """
        cards = self.find_elements_by_class_name("f79dd23c27c3352da3ac3ba62d78f8ea-scss")
        play_btn = self.find_element_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[3]/div[4]/div[1]/div[1]/div[2]/section[1]/section[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
        self.hover_to_element(cards[0])
        time.sleep(2)
        self.click_button_safe(play_btn)

    def click_play_or_pause(self):
        """
        Clicks on the Play/Pause button
        """
        self.click_button_safe(self.play_pause_btn)

    def click_queue(self):
        """
        Clicks on the Queue button
        """
        self.click_button_safe(self.queue_button)

    def get_song_name(self):
        """
        Gets the currently playing song name

        :returns: The song name
        :rtype: str
        """
        song_name = (self.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div[3]/footer/div[1]/div[1]/div/div[2]/div[1]")).text
        return song_name

    def get_artist_name(self):
        """
        Gets the artist name of the currently playing song

        :returns: The song name
        :rtype: str
        """
        artist_name = (self.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div[3]/footer/div[1]/div[1]/div/div[2]/div[2]")).text
        return artist_name

    def get_consumed_time(self):
        """
        Gets the consumed time of the currently playing song

        :returns: The consumed time of the currently playing song
        :rtype: CustomTime
        """
        consumed_time = str(self.playbackBarProgressTime_div[0].text)
        consumed_time_arr = consumed_time.split(":")
        return CustomTime(int(consumed_time_arr[0]), int(consumed_time_arr[1]))

    def get_remaining_time(self):
        """
        Gets the remaining time of the currently song

        :returns: The remaining time of the currently playing song
        :rtype: CustomTime
        """
        return self.playbackBarProgressTime_div[1].text

    def click_next_song(self):
        """
        Clicks on the next song button
        """
        self.click_button_safe(self.next_song_btn)

    def click_prev_song(self):
        """
        Clicks on the previous song button
        """
        self.click_button_safe(self.prev_song_btn)
