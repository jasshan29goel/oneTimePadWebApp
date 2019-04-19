README v0.0 / 15 APRIL 2019

# One Time Pad and Perfect Secrecy

## Introduction

The project is one of the experiments of the virtual lab (cryptography lab) of IIITH
Standard template of the frontend is used and the backend is made using python.

## Usage

First go to the directory which you have cloned just now
Run this command on terminal

python3 app.py

then open localhost:5000 on your web browser

## Installation
python version 3.5.0 or above
flask
flask_sqlAlchemy

## About the code

### The templates directory:- 
This contains all the html pages which form frontend of the experiment. It also containts the javascript and ajax code to generate requests to the app
experiment.html page has the experiment page which basically is composed of three forms and the quiz.html page has five questions which are retrieved at the frontend by ajax request to the app.py file
Rest all have only plain html which is used to display the content of the respective pages
Also the code in index.html is imported to all the html pages 

### The static directory:-
This directory contains all the required css javascript files used to make the frontend of the website

### The app.py file
The app.py is the file which contains all the backend of the experiment

It consists of three databases
The first one is for storing the  key and plaintext pairs which user enter
The second one is for the storing of the 2^8 plaintext for generating the encryption set
The third one is for storing the quiz questions

It consits of four forms for handling the various buttons on the html page and also one check function which is used to evaluate the answers of the quiz and give you a score

form1 contains 3 buttons
form2 contains 1 button
form3 contains 1 button
form4 contains 2 buttons

All of these have a seperate redirection function so as to generate different request for each button
Also there are custom functions in this file and to make viewing what is stored in the database easier
All the fuctions and variables have intutive names so that debugging is easier

### The test_app.py
This file contains the unit test cases

### The createdatabasequiz.py
This file can be run when one wants to generate the database

## Credits

Manish

Jasshan Goel

