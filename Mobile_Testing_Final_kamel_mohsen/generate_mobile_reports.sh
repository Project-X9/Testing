#!/bin/bash

#Connects to virtual environment
source venv/bin/activate

_Reports="_Reports"
_docx=".docx"

feature="Premium"
allure-docx --title="Login" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/$feature$_Reports/allurefiles ./Reports/Mobile_Reports/$feature$_Reports/$feature$_Reports$_docx
feature="Playlist"
allure-docx --title="Login" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/$feature$_Reports/allurefiles ./Reports/Mobile_Reports/$feature$_Reports/$feature$_Reports$_docx
feature="Album"
allure-docx --title="Login" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/$feature$_Reports/allurefiles ./Reports/Mobile_Reports/$feature$_Reports/$feature$_Reports$_docx


allure-docx --title="Mobile" --logo=./logo.jpg --logo-height=2 ./Reports/Mobile_Reports/allurefiles ./Reports/Mobile_Reports/Final_Mobile_Report.docx


