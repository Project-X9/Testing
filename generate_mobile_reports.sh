#!/bin/bash

#Connects to virtual environment
source venv/bin/activate




allure-docx  ./Reports/Mobile_Reports/Login_Reports/allurefiles ./Reports/Mobile_Reports/Authentication_Reports/Login_Report.docx

allure-docx  ./Reports/Mobile_Reports/Authentication_Reports/allurefiles ./Reports/Mobile_Reports/Authentication_Reports/Authentication_Report.docx

allure-docx  ./Reports/Mobile_Reports/Extra_Reports/allurefiles ./Reports/Mobile_Reports/Extra_Reports/Extra_Report.docx

allure-docx  ./Reports/Mobile_Reports/Home_Reports/allurefiles ./Reports/Mobile_Reports/Home_Reports/Home_Report.docx

allure-docx  ./Reports/Mobile_Reports/Player_Reports/allurefiles ./Reports/Mobile_Reports/Player_Reports/Player_Report.docx

allure-docx  ./Reports/Mobile_Reports/Signup_Reports/allurefiles ./Reports/Mobile_Reports/Signup_Reports/Signup_Report.docx

allure-docx  ./Reports/All_Reports/allurefiles ./Reports/All_Reports/Final_Report.docx

allure-docx  ./Reports/Mobile_Reports/allurefiles ./Reports/Mobile_Reports/Final_Mobile_Report.docx


