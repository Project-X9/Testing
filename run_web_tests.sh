#!/bin/bash

#Connects to virtual environment
source venv/bin/activate

path="/Users/KIMO/Desktop/Testing/"
sel="Do"

#Makes Login_Reports directory
rm -rf ./Reports/Web_Reports/Login_Reports/
mkdir ./Reports/Web_Reports/Login_Reports
#Makes Login_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Login_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Login_Reports/allurefiles" ./Web_Testing/Tests/test_login.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Login_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Login_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Account_OverView_Reports directory
rm -rf ./Reports/Web_Reports/Account_Overview_Reports/
mkdir ./Reports/Web_Reports/Account_Overview_Reports
#Makes Account_Overview_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Account_Overview_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Account_Overview_Reports/allurefiles" ./Web_Testing/Tests/test_accountoverview.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Account_Overview_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Account_Overview_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Artist_Reports directory
rm -rf ./Reports/Web_Reports/Artist_Reports/
mkdir ./Reports/Web_Reports/Artist_Reports
#Makes Artist_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Artist_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Artist_Reports/allurefiles" ./Web_Testing/Tests/test_artist.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Artist_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Artist_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Change_Password_Reports directory
rm -rf ./Reports/Web_Reports/Change_Password_Reports/
mkdir ./Reports/Web_Reports/Change_Password_Reports
#Makes Change_Password_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Change_Password_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Change_Password_Reports/allurefiles" ./Web_Testing/Tests/test_changePassword.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Change_Password_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Change_Password_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Liked_Songs_Reports directory
rm -rf ./Reports/Web_Reports/Liked_Songs_Reports/
mkdir ./Reports/Web_Reports/Liked_Songs_Reports
#Makes Liked_Songs_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Liked_Songs_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Liked_Songs_Reports/allurefiles" ./Web_Testing/Tests/test_likedsongs.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Liked_Songs_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Liked_Songs_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Logged_Out_Home_Reports directory
rm -rf ./Reports/Web_Reports/Logged_Out_Home_Reports/
mkdir ./Reports/Web_Reports/Logged_Out_Home_Reports
#Makes Logged_Out_Home_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Logged_Out_Home_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Logged_Out_Home_Reports/allurefiles" ./Web_Testing/Tests/test_loggedOutHome.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Logged_Out_Home_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Logged_Out_Home_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Playlist_Reports directory
rm -rf ./Reports/Web_Reports/Playlist_Reports/
mkdir ./Reports/Web_Reports/Playlist_Reports
#Makes Playlist_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Playlist_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Playlist_Reports/allurefiles" ./Web_Testing/Tests/test_playlist.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Playlist_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Playlist_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Premium_Reports directory
rm -rf ./Reports/Web_Reports/Premium_Reports/
mkdir ./Reports/Web_Reports/Premium_Reports
#Makes Premium_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Premium_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Premium_Reports/allurefiles" ./Web_Testing/Tests/test_premium.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Premium_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Premium_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Signup_Reports directory
rm -rf ./Reports/Web_Reports/Signup_Reports/
mkdir ./Reports/Web_Reports/Signup_Reports
#Makes Signup_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Signup_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Signup_Reports/allurefiles" ./Web_Testing/Tests/test_signup.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Signup_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Signup_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Web_Player_Home_Reports directory
rm -rf ./Reports/Web_Reports/Web_Player_Home_Reports/
mkdir ./Reports/Web_Reports/Web_Player_Home_Reports
#Makes Web_Player_Home_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Web_Player_Home_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Web_Player_Home_Reports/allurefiles" ./Web_Testing/Tests/test_webplayerHome.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Web_Player_Home_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Web_Player_Home_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles

#Makes Your_Library_Reports directory
rm -rf ./Reports/Web_Reports/Your_Library_Reports/
mkdir ./Reports/Web_Reports/Your_Library_Reports
#Makes Your_Library_Reports/allurefiles directory
mkdir ./Reports/Web_Reports/Your_Library_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Web_Reports/Your_Library_Reports/allurefiles" ./Web_Testing/Tests/test_yourLibrary.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Web_Reports/Your_Library_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Web_Reports/Your_Library_Reports/allurefiles/. $path/Reports/Web_Reports/allurefiles