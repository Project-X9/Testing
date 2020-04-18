from Mobile_Testing.helper import Helper


class PlayMusicPage:
    """
    A class used to represent the Play Song Page
    ...
    Attributes
    ----------
    play_song_id : string
        id of play song button
    previous_song_id : string
        id of previous  song button
    next_song_id : string
        id of next song button
    love_song_id : string
        id of love song button
    download_song_id : string
        id of download song button
    repeat_song_id : string
        id of repeat song button
    share_song_id : string
        id of share song button
    help_button_id : string
        id of help button
    minimize_player_id : string
        id of minimize player button
    black_list_song_id : string
        id of block song button


    Methods
    -------
        None
    """

    play_song_id = "com.example.projectx:id/playSong_ib"
    previous_song_id = "com.example.projectx:id/previousSong_ib"
    next_song_id = "com.example.projectx:id/nextSong_ib"
    love_song_id = "com.example.projectx:id/likeButton_ib"
    download_song_id = "com.example.projectx:id/downloadButton_ib"
    repeat_song_id = "com.example.projectx:id/repeatButton_ib"
    share_song_id = "com.example.projectx:id/shareButton_ib"
    help_button_id = "com.example.projectx:id/more_ib"
    minimize_player_id = "com.example.projectx:id/collapse_ib"
    black_list_song_id = "com.example.projectx:id/blackListSong_ib"

    def __init__(self, driver):
        """
        Initializes the page elements
        :param driver : the driver to which the super class' driver is to be set
        :type driver: WebDriver
        """
        self.driver = driver
