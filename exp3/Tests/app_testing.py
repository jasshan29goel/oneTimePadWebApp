from flask import request, jsonify
import requests

c=0;

def test_form4a(var1,var2,var3):
	files = {
	    'PlainText': (None, var1),
	    'Key': (None, var2),
	}

	response = requests.post('http://127.0.0.1:5000/form4a', files=files)
	try :
		assert response.json()["output"]==var3
		print("Test passed")
	except AssertionError:
		print ("form4a test failed")
		global c
		c=c+1

def test_form4b(var1,var2,var3):
	files = {
	    'CypherText': (None, var1),
	    'Key': (None, var2),
	}

	response = requests.post('http://127.0.0.1:5000/form4b', files=files)
	try :
		assert response.json()["output"]==var3
		print("Test passed")
	except AssertionError:
		print ("form4b test failed")
		global c
		c=c+1

def test_form3(var1,var2,var3,var4,var5):
	files = {
	    'key2': (None, var1),
	    'response': (None, var2),
	    'm1': (None, var3),
	    'm2': (None, var4),
	}

	response = requests.post('http://127.0.0.1:5000/form3', files=files)
	try :
		assert response.json()["output"]==var5
		print("Test passed")
	except AssertionError:
		print ("form3 test failed")
		global c
		c=c+1
def test_form1b3(var1,var2,var3):
	files = {
	    'plainText1': (None, var1),
	    'key1': (None, var2),
	}

	response = requests.post('http://127.0.0.1:5000/form1b3', files=files)
	try :
		if var3:
			assert response.json()["output"]==var3
			print("Test passed")
	except AssertionError:
		print ("form1b3 test failed")
		global c
		c=c+1

def test_form1b2(var1):
	files = {
	    'plainText1': (None, var1),
	}

	response = requests.post('http://127.0.0.1:5000/form1b2', files=files)
	
	if not response.json()["output"]:
	    print ("form1b2 test failed")
	    global c
	    c=c+1

def test_form1b1(var1):
	files = {
	    'key1': (None, var1),
	}

	response = requests.post('http://127.0.0.1:5000/form1b1', files=files)
	
	if not response.json()["output"]:
	    print ("form1b1 test failed")
	    global c
	    c=c+1


test_form4a("10","10","00")
test_form4a("100","10","Key too small!")
test_form4a("10","1a","Enter binary string!")
test_form4a("10","","Missing data!")

test_form4b("10","10","00")
test_form4b("100","10","Key too small!")
test_form4b("10","1a","Enter binary string!")
test_form4b("10","","Missing data!")

test_form3("","Yes","00000000","10101010","Please enter key")
test_form3("10101010","","00000000","10101010","Please Enter Yes/No!")
test_form3("10101010","YES","00000000","10101010","Please Enter Yes/No")

test_form1b3("100","10","Key too small!")
test_form1b3("10","1a","Enter binary string!")
test_form1b3("10","","Missing data!")
test_form1b3("10","10","")

test_form1b2("10")
test_form1b1("10")

print("Tests Failed = "+str(c))