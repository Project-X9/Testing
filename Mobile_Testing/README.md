# Testing

Android application testing code for Project_X (Spotify Mock)

For Android Testing You need to install SDK a this have to be done manually

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

1-First you install the requirements using the following command
pip3 install -r requirements.txt

2.a)
Second run the tests using the following commands in terminal ont the root directory of testing
python3 -m pytest --alluredir="./Mobile_Testing/Reports" ./Mobile_Testing/Tests/ -m Do 
2.b)
to run test for specific Function you can use 
python3 -m pytest --alluredir="./Mobile_Testing/Reports" ./Mobile_Testing/Tests/ -m <NAME of you test function>
2.c)
to run a specific test of a specific fuction use 
python3 -m pytest --alluredir="./Mobile_Testing/Reports" ./Mobile_Testing/Tests/<NAme of you test file i.e: test_home.py> -m Test<number of your test>


3.a)
Third you generate the word and pdf Report using the following Command
allure-docx --pdf Reports Test_Results.docx
3.b)
to generate the word only use
allure-docx Reports Test_Results.docx

4-(Optional)Fourth you run the allure server on chrome browser using the following command
allure serve "./Reports"
