import requests

BASE_URL = "http://127.0.0.1:5000"  #LOCAL HOST

def test_checkServer():
	timeout=5
	try:
		_= requests.get(BASE_URL, timeout=timeout)
		print("SERVER responding as expected!!")
		return True
	except requests.ConnectionError:
		print("Server Not Connected")
		return False


links = [ "/","/Introduction.html","/Theory.html","/Objective.html","/Experiment.html","/Quizzes.html","/Procedure.html","/Further.html"]
def test_root():

	response = requests.get(BASE_URL + links[0])
	assert response.status_code == 200,links[0]
	code = str(response.status_code)
	print(BASE_URL + links[0] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_intro():

	response = requests.get(BASE_URL + links[1])
	assert response.status_code == 200,links[1]
	code = str(response.status_code)
	print(BASE_URL + links[1] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_theory():

	response = requests.get(BASE_URL + links[2])
	assert response.status_code == 200,links[2]
	code = str(response.status_code)
	print(BASE_URL + links[2] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_objective():

	response = requests.get(BASE_URL + links[3])
	assert response.status_code == 200,links[3]
	code = str(response.status_code)
	print(BASE_URL + links[3] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_exp():

	response = requests.get(BASE_URL + links[4])
	assert response.status_code == 200,links[4]
	code = str(response.status_code)
	print(BASE_URL + links[4] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_Quizzes():

	response = requests.get(BASE_URL + links[5])
	assert response.status_code == 200,links[5]
	code = str(response.status_code)
	print(BASE_URL + links[5] + " : ")
	print("status code=" + code + "; Link responding as expected!!")

def test_proc():

	response = requests.get(BASE_URL + links[6])
	assert response.status_code == 200,links[6]
	code = str(response.status_code)
	print(BASE_URL + links[6] + " : ")
	print("status code=" + code + "; Link responding as expected!!")


def test_further():

	response = requests.get(BASE_URL + links[7])
	assert response.status_code == 200,links[7]
	code = str(response.status_code)
	print(BASE_URL + links[7] + " : ")
	print("status code=" + code + "; Link responding as expected!!")
