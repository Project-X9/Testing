# Testing

Web + Android application testing code for Project_X (Spotify Mock)
----------------------------------------------------------------------------
For Android Testing ONLY!!!!

You need to install SDK files as this have to be done manually

Then install appium using :
npm install -g appium

Then you run appium using the command
appium      
OR you can use the appium desktop App:
open the desktop App then press start 



Then you open the helper.py and manually write the name of you device in the CONSTANTS->desired_capabilities at the bottom of the file
!!!!!HINT: sometimes you need to run the app first on the target device using Android Studio
!!!!!HINT: You can get the name of your device from android studio

then we start to initiate our testing dependencies by foloowing this steps:
!!!!!PS:(it is preferred to use pycharm to create virtual env and then follow the steps below)

----------------------------------------------------------------------------



1-First you install the requirements using the following commands:
pip3 install -r requirements.txt



----------------------------------------------------------------------------


2-Second run the tests using the following commands

Recommended:


For Web Testing:
sudo bash run_web_tests.sh
or
sudo sh run_web_tests.sh

For Mobile Testing:
sudo bash run_mobile_tests.sh
or
sudo sh run_mobile_tests.sh




Not Recommended: (can be used to run separate tests)


For Web Testing:

(i.e)This runs all the web tests:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Web_Testing/Tests/ -m Do 

(i.e)This runs tests for specific function:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Web_Testing/Tests/test_login.py -m Do
 
(i.e)This runs specific test for specific function:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Web_Testing/Tests/test_login.py -m Test2




For Mobile Testing:

(i.e)This runs all the mobile tests:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Mobile_Testing/Tests/ -m Do 

(i.e)This runs tests for specific function:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Mobile_Testing/Tests/test_login.py -m Do
 
(i.e)This runs specific test for specific function:
python3 -m pytest --alluredir="./Reports/All_Reports/allurefiles" ./Mobile_Testing/Tests/test_login.py -m Test2

----------------------------------------------------------------------------



3-Third you generate the word and pdf Report using the following Command
{
!!!!!!!!Hint Run this first!!!!!!!! 
pip3 install git+https://github.com/typhoon-hil/allure-docx.git
}
Recommended:
	
For Web Testing:
sudo bash generate_web_reports.sh
or
sudo sh generate_web_reports.sh

For Mobile Testing:
sudo bash generate_mobile_reports.sh
or
sudo sh generate_mobile_reports.sh

*****

Not Recommended:

(i.e)This generates the report to a word file only:
allure-docx  ./Reports/All_Reports/allurefiles Test_Results.docx


(i.e)This generates the report to a word file and pdf:
allure-docx --pdf ./Reports/All_Reports/allurefiles Test_Results.docx

----------------------------------------------------------------------------

4-(Optional)Fourth you run the allure server on chrome browser using the following command
allure serve "./Reports"
