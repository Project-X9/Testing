"""
Playlist page Testing

This script tests the creation and deletion of playlists and report the results to allure

This script requires `allure` and `pytest` be installed within the Python environment you are running this script in
"""
import allure
import pytest

from Web_Testing.helperClasses import WebHelper, ConstantsClass,login


from Web_Testing.Pages.WebPlayerPlaylist import WebPlayerPlaylist



@allure.parent_suite("End to End testing")
@allure.suite("Playlist page test")
@allure.feature("Playlist page test")
@allure.severity(allure.severity_level.CRITICAL)
class TestPlaylists:
    driver = WebHelper().firefox_driver_init()
    helper = WebHelper()
    helper.set_driver(driver)
    pp = WebPlayerPlaylist(driver)
    lp = login(driver)

    def login_first(self):
        lp = login(self.driver)
        lp.login_to_spotify()

    @pytest.yield_fixture
    def setup_begin(self):
        self.driver.get("https://accounts.spotify.com/en/login")
        self.driver.maximize_window()
        self.login_first()
        yield
        self.driver.refresh()

    @pytest.yield_fixture
    def setup(self):
        self.driver.get("https://open.spotify.com/")
        self.driver.maximize_window()
        yield
        self.driver.refresh()

    @pytest.yield_fixture
    def setup_final(self):
        self.driver.get("https://open.spotify.com/")
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Test #1 ->Checking that create playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer playlist tests")
    @allure.sub_suite("Create new Playlist")
    @allure.title("Create new Playlist")
    @allure.description("Create new Playlist")
    @pytest.mark.Do
    @pytest.mark.CreatePlaylist
    def test_case_1(self, setup_begin):
        self.driver.implicitly_wait(5)
        self.pp.get_no_of_playlist()
        self.helper.report_allure("overview for playlists before creation", self.driver)
        if self.pp.create_playlist():
            self.helper.report_allure("create playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to create playlist ", self.driver)
            assert False

    # Test #2 ->Checking that cancel creation of playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer playlist tests")
    @allure.sub_suite("cancel creation of playlist")
    @allure.title("cancel creation of playlist")
    @allure.description("cancel creation of playlist")
    @pytest.mark.Do
    @pytest.mark.CancelPlaylist
    def test_case_2(self, setup):
        self.driver.implicitly_wait(5)
        self.pp.get_no_of_playlist()
        self.helper.report_allure("overview for playlists before cancel creation", self.driver)
        if self.pp.cancel_creation():
            self.helper.report_allure("cancel creation of playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to cancel creation of playlist", self.driver)
            assert False

    # Test #3 ->Checking that delete playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer playlist tests")
    @allure.sub_suite("delete playlist")
    @allure.title("delete playlist")
    @allure.description("delete playlist")
    @pytest.mark.Do
    @pytest.mark.DeletePlaylist
    def test_case_3(self, setup):
        self.driver.implicitly_wait(5)
        self.pp.get_no_of_playlist()
        self.helper.report_allure("overview for playlists before deletion", self.driver)
        if self.pp.delete_playlist():
            self.helper.report_allure("delete playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to delete playlist", self.driver)
            assert False

    # Test #4 ->Checking that cancel deletion of playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer playlist tests")
    @allure.sub_suite("cancel deletion of playlist")
    @allure.title("cancel deletion of playlist")
    @allure.description("cancel deletion of playlist")
    @pytest.mark.Do
    @pytest.mark.cancelDeletePlaylist
    def test_case_4(self, setup):
        self.driver.implicitly_wait(5)
        self.pp.get_no_of_playlist()
        self.helper.report_allure("overview for playlists before cancel deletion", self.driver)
        if self.pp.cancel_deletion():
            self.helper.report_allure("Cancel deletion of playlist successfully", self.driver)
            assert True
        else:
            self.helper.report_allure("Fail to cancel deletion of playlist", self.driver)
            assert False

    # Test #5 ->Checking that rename playlist is function
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Webplayer playlist tests")
    @allure.sub_suite("Rename playlist")
    @allure.title("Rename playlist")
    @allure.description("Rename playlist")
    @pytest.mark.Do
    @pytest.mark.renameplaylist
    def test_case_5(self, setup_final):
        self.driver.implicitly_wait(5)
        self.pp.name_overview()
        self.helper.report_allure("Overview for playlist's name before rename playlist", self.driver)
        ret = self.pp.rename_playlist()
        if ret == 0:
            self.helper.report_allure("Rename playlist successfully", self.driver)
            assert True
        else:
            if ret == 1:
                self.helper.report_allure("Fail to rename playlist ", self.driver)
            elif ret == 2:
                self.helper.report_allure("Rename playlist successfully but with wrong name", self.driver)
            assert False

