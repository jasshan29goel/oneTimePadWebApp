import requests

BASE_URL = "http://127.0.0.1:5000"  #LOCAL HOST

def checkServer():
	timeout=5
	try:
		_= requests.get(BASE_URL, timeout=timeout)
		print("SERVER responding as expected!!")
		return True
	except requests.ConnectionError:
		print("Server Not Connected")
		return False



links = ["/Introduction.html","/Theory.html","/Objective.html","/Experiment.html","/Quizzes.html","/Procedure.html","/Further.html"]

for current in links:
	response = requests.get(BASE_URL + current)
	assert response.status_code == 200,current
	code = str(response.status_code)
	print(BASE_URL + current + " : ")
	print("status code=" + code + "; Link responding as expected!!")


print("All links are functional!!")
