README v0.0 / 15 APRIL 2019

# One Time Pad and Perfect Secrecy

## Introduction

The project is one of the experiments of the virtual lab (cryptography lab) of IIITH
Standard template of the frontend is used and the backend is made using python.

## Running the Experiment

Step1 --> Run the Experiment.py file using command :-
```python
					$ python3 run.py
```

Step2 --> Open the browser and open the following link
				
							"localhost:5000/"

## Testings

Step1 --> Run the Experiment.
(Testing is to be done on a new terminal) 

Testing is done in two steps:-
1) Test for all the links to pages
		Run the Links_Test.py file using command
```python
			 $ python3 links_test.py		
```

2) Unit testing for logic part of the Experiment
		Run the Unit_tests.py file using command
```python
			$ python3 tests_app.py				
```				

## Installing and Prerequisites

```bash
sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
pip3 install Flask
sudo apt-get install sqlite3
pip3 install sqlalchemy
pip3 install Markups
pip3 install requests
```

## Built With

* Python Flask
* javascript Ajax


## About the code



### The templates directory:- 
This contains all the html pages which form frontend of the experiment. It also containts the javascript and ajax code to generate requests to the app
experiment.html page has the experiment page which basically is composed of three forms and the quiz.html page has five questions which are retrieved at the frontend by ajax request to the app.py file
Rest all have only plain html which is used to display the content of the respective pages
Also the code in index.html is imported to all the html pages 

### The static directory:-
This directory contains all the required css javascript files used to make the frontend of the website
### The controllers.py file

It consists of three databases
The first one is for storing the  key and plaintext pairs which user enter
The second one is for the storing of the 2^8 plaintext for generating the encryption set
The third one is for storing the quiz questions

### The models.py file
The models.py is the file which contains all the backend of the experiment

It consits of four forms for handling the various buttons on the html page and also one check function which is used to evaluate the answers of the quiz and give you a score

form1 contains 3 buttons
form2 contains 1 button
form3 contains 1 button
form4 contains 2 buttons

All of these have a seperate redirection function so as to generate different request for each button
Also there are custom functions in this file and to make viewing what is stored in the database easier
All the fuctions and variables have intutive names so that debugging is easier

### The test_app.py
This file contains the unit test cases for form elements
This file contains the unit test cases for links 

### The createTextDatabase.py
This file can be run when one wants to generate the 2^8 plaintext database
### The createquizbasequiz.py
This file can be run when one wants to generate the quiz database

## Credits

Manish

Jasshan Goel

