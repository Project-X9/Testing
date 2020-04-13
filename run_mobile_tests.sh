#!/bin/bash

#Connects to virtual environment
source venv/bin/activate

path="/Users/KIMO/Desktop/Testing/"
sel="Do"


#Makes Login_Reports directory
rm -rf ./Reports/Mobile_Reports/Login_Reports/
mkdir ./Reports/Mobile_Reports/Login_Reports
#Makes Login_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Login_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Login_Reports/allurefiles" ./Mobile_Testing/Tests/test_login.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Login_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Login_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles


#Makes Authentication_Reports directory
rm -rf ./Reports/Mobile_Reports/Authentication_Reports/
mkdir ./Reports/Mobile_Reports/Authentication_Reports
#Makes Authentication_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Authentication_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Authentication_Reports/allurefiles" ./Mobile_Testing/Tests/test_authentication.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Authentication_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Authentication_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles

#Makes Extra_Reports directory
rm -rf ./Reports/Mobile_Reports/Extra_Reports/
mkdir ./Reports/Mobile_Reports/Extra_Reports
#Makes Extra_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Extra_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Extra_Reports/allurefiles" ./Mobile_Testing/Tests/test_extra.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Extra_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Extra_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles

#Makes Home_Reports directory
rm -rf ./Reports/Mobile_Reports/Home_Reports/
mkdir ./Reports/Mobile_Reports/Home_Reports
#Makes Home_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Home_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Home_Reports/allurefiles" ./Mobile_Testing/Tests/test_home.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Home_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Home_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles

#Makes Player_Reports directory
rm -rf ./Reports/Mobile_Reports/Player_Reports/
mkdir ./Reports/Mobile_Reports/Player_Reports
#Makes Player_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Player_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Player_Reports/allurefiles" ./Mobile_Testing/Tests/test_player.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Player_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Player_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles

#Makes Signup_Reports directory
rm -rf ./Reports/Mobile_Reports/Signup_Reports/
mkdir ./Reports/Mobile_Reports/Signup_Reports
#Makes Signup_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/Signup_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/Signup_Reports/allurefiles" ./Mobile_Testing/Tests/test_signup.py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/Signup_Reports/allurefiles/. $path/Reports/All_Reports/allurefiles
cp -a $path/Reports/Mobile_Reports/Signup_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles
