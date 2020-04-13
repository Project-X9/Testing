#!/bin/bash

#Connects to virtual environment
source venv/bin/activate


rm -rf ./Documentation
mkdir -p Documentation

mkdir -p Documentation/Mobile
mkdir -p Documentation/Mobile/Helper
mkdir -p Documentation/Mobile/Tests
mkdir -p Documentation/Mobile/Pages

mkdir -p Documentation/Web
mkdir -p Documentation/Web/helper
mkdir -p Documentation/Web/Tests
mkdir -p Documentation/Web/Pages



python -m pydoc -w ./Mobile_Testing/*.py
mv *.html Documentation/Mobile/Helper

python -m pydoc -w ./Mobile_Testing/Tests/*.py
mv *.html Documentation/Mobile/Tests

python -m pydoc -w ./Mobile_Testing/Pages/*.py
mv *.html Documentation/Mobile/Pages


python -m pydoc -w ./Web_Testing/*.py
mv *.html Documentation/Web/Helper

python -m pydoc -w ./Web_Testing/Tests/*.py
mv *.html Documentation/Web/Tests

python -m pydoc -w ./Web_Testing/Pages/*.py
mv *.html Documentation/Web/Pages
