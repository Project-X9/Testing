#!/bin/bash

#Connects to virtual environment
source venv/bin/activate


################Constants#############
path="/Users/KIMO/Desktop/Final_Assesment/E2E_testing_kamel_mohsen/"
sel="Do"
_Reports="_Reports"
_py=".py"
_test="test_"

################VARS##################
feature="Premium"
featuresmall="premium"
#Makes $feature_Reports directory
rm -rf ./Reports/Mobile_Reports/$feature$_Reports/
mkdir ./Reports/Mobile_Reports/$feature$_Reports/
#Makes $feature_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/$feature$_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/$feature$_Reports/allurefiles" ./Mobile_Testing/Tests/$_test$featuresmall$_py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/$feature$_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles




################VARS##################
feature="Playlist"
featuresmall="playlist"
#Makes $feature_Reports directory
rm -rf ./Reports/Mobile_Reports/$feature$_Reports/
mkdir ./Reports/Mobile_Reports/$feature$_Reports/
#Makes $feature_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/$feature$_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/$feature$_Reports/allurefiles" ./Mobile_Testing/Tests/$_test$featuresmall$_py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/$feature$_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles



################VARS##################
feature="Album"
featuresmall="album"
#Makes $feature_Reports directory
rm -rf ./Reports/Mobile_Reports/$feature$_Reports/
mkdir ./Reports/Mobile_Reports/$feature$_Reports/
#Makes $feature_Reports/allurefiles directory
mkdir ./Reports/Mobile_Reports/$feature$_Reports/allurefiles
#Runs tests for this function
python3 -m pytest --alluredir="./Reports/Mobile_Reports/$feature$_Reports/allurefiles" ./Mobile_Testing/Tests/$_test$featuresmall$_py -m $sel
#Copies allure files to all more general palce
cp -a $path/Reports/Mobile_Reports/$feature$_Reports/allurefiles/. $path/Reports/Mobile_Reports/allurefiles












