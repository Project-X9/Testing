#!/bin/bash

#Connects to virtual environment
source venv/bin/activate


allure-docx  ./Reports/Web_Reports/Login_Reports/allurefiles ./Reports/Web_Reports/Login_Reports/Login_Report.docx

allure-docx  ./Reports/Web_Reports/Account_Overview_Reports/allurefiles ./Reports/Web_Reports/Account_Overview_Reports/Account_Overview_Report.docx

allure-docx  ./Reports/Web_Reports/Artist_Reports/allurefiles ./Reports/Web_Reports/Artist_Reports/Artist_Report.docx

allure-docx  ./Reports/Web_Reports/Change_Password_Reports/allurefiles ./Reports/Web_Reports/Change_Password_Reports/Login_Report.docx

allure-docx  ./Reports/Web_Reports/Liked_Songs_Reports/allurefiles ./Reports/Web_Reports/Liked_Songs_Reports/Liked_Songs_Report.docx

allure-docx  ./Reports/Web_Reports/Logged_Out_Home_Reports/allurefiles ./Reports/Web_Reports/Logged_Out_Home_Reports/Logged_Out_Home_Report.docx

allure-docx  ./Reports/Web_Reports/Playlist_Reports/allurefiles ./Reports/Web_Reports/Playlist_Reports/Playlist_Report.docx

allure-docx  ./Reports/Web_Reports/Premium_Reports/allurefiles ./Reports/Web_Reports/Premium_Reports/Premium_Report.docx

allure-docx  ./Reports/Web_Reports/Signup_Reports/allurefiles ./Reports/Web_Reports/Signup_Reports/Signup_Report.docx

allure-docx  ./Reports/Web_Reports/Web_Player_Home_Reports/allurefiles ./Reports/Web_Reports/Web_Player_Home_Reports/Web_Player_Home_Report.docx

allure-docx  ./Reports/Web_Reports/Your_Library_Reports/allurefiles ./Reports/Web_Reports/Your_Library_Reports/Your_Library_Report.docx

allure-docx  ./Reports/All_Reports/allurefiles ./Reports/All_Reports/Final_Report.docx

allure-docx  ./Reports/Web_Reports/allurefiles ./Reports/Mobile_Reports/Final_Web_Report.docx
