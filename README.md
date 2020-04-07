# Testing

Web + Android application testing code for Project_X (Spotify Mock)

See command_to_use.txt for the cmd commands to use to run the tests and install and freeze dependencies and open Report in allure local host


1-First you install the requirements using the following command
pip3 install -r requirements.txt

2-Second run the tests using the following commands
python3 -m pytest --alluredir="./Reports" ./Mobile_Testing/Tests/ -m Do 
python3 -m pytest --alluredir="./Reports" ./Web_Testing/Tests/ -m Do

3-Third you generate the word and pdf Report using the following Command
allure-docx --pdf Reports Test_Results.docx

4-(Optional)Fourth you run the allure server on chrome browser using the following command
allure serve "./Reports"
