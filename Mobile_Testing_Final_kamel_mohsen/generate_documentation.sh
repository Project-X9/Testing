#!/bin/bash

#Connects to virtual environment
source venv/bin/activate


rm -rf ./Documentation
mkdir -p Documentation

mkdir -p Documentation/Mobile
mkdir -p Documentation/Mobile/Helper
mkdir -p Documentation/Mobile/Tests
mkdir -p Documentation/Mobile/Pages




python -m pydoc -w ./Mobile_Testing/*.py
mv *.html Documentation/Mobile/Helper

python -m pydoc -w ./Mobile_Testing/Tests/*.py
mv *.html Documentation/Mobile/Tests

python -m pydoc -w ./Mobile_Testing/Pages/*.py
mv *.html Documentation/Mobile/Pages

