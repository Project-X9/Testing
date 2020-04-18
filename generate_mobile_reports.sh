#!/bin/bash

#Connects to virtual environment
source venv/bin/activate




allure-docx --title="Login" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Login_Reports/allurefiles ./Reports/Mobile_Reports/Login_Reports/Login_Report.docx

allure-docx --title="Authentication" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Authentication_Reports/allurefiles ./Reports/Mobile_Reports/Authentication_Reports/Authentication_Report.docx

allure-docx --title="Extra" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Extra_Reports/allurefiles ./Reports/Mobile_Reports/Extra_Reports/Extra_Report.docx

allure-docx --title="Home" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Home_Reports/allurefiles ./Reports/Mobile_Reports/Home_Reports/Home_Report.docx

allure-docx --title="Player" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Player_Reports/allurefiles ./Reports/Mobile_Reports/Player_Reports/Player_Report.docx

allure-docx --title="Signup" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/Signup_Reports/allurefiles ./Reports/Mobile_Reports/Signup_Reports/Signup_Report.docx

allure-docx --title="ProjectX" --logo=./logo.jpg --logo-height=2 ./Reports/All_Reports/allurefiles ./Reports/All_Reports/Final_Report.docx

allure-docx --title="Mobile" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/allurefiles ./Reports/Mobile_Reports/Final_Mobile_Report.docx


