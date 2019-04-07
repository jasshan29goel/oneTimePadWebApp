from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# database element class
class text_key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plainText = db.Column(db.String)
    key = db.Column(db.String)

    def __init__(self,plainText, key):
        self.plainText = plainText
        self.key = key

    def __repr__(self):
        return '<User %r>' % self.plainText


@app.route('/')
def Root():
    return render_template("Introduction.html")
@app.route('/Introduction.html')
def Introduction():
    return render_template("Introduction.html")
@app.route('/Objective.html')
def Objective():
    return render_template("Objective.html")
@app.route('/Experiment.html')
def Experiment():
    return render_template("Experiment.html")
@app.route('/Theory.html')
def Theory():
    return render_template('Theory.html')
@app.route('/Manual.html')
def Manual():
    return render_template('Manual.html')
@app.route('/Quizzes.html')
def Quizzes():
    return render_template('Quizzes.html')
@app.route('/Procedure.html')
def Procedure():
    return render_template('Procedure.html')
@app.route('/Further Readings.html')
def Further():
    return render_template('Further Readings.html')    
@app.route('/Feedback.html')
def Feedback():
    return render_template('Feedback.html')

@app.route('/form1b3',methods= ['POST'])
def form1b3():
    plainText1 = request.form['plainText1']
    key1 = request.form['key1']

    return vernam_cipher(plainText1,key1)


@app.route('/form1b2',methods= ['POST'])
def form1b2():
    dummy = request.form['dummy']
    if dummy :
        return jsonify({'output':1000})
    return jsonify({'error' : 'Missing data!'})

@app.route('/form1b1',methods= ['POST'])
def form1b1():
    dummy = request.form['dummy']
    if dummy :
        return jsonify({'output':1000})
    return jsonify({'error' : 'Missing data!'})

@app.route('/form2b1',methods= ['POST'])
def form2b1():
    dummy = request.form['dummy']
    if dummy :
        return jsonify({'output':99999})
    return jsonify({'error' : 'Missing data!'})

@app.route('/form4a',methods= ['POST'])
def form4a():
    PlainText = request.form['PlainText']
    Key = request.form['Key']

    return vernam_cipher(PlainText,Key)


@app.route('/form4b',methods= ['POST'])
def form4b():
    CypherText = request.form['CypherText']
    Key = request.form['Key']

    return vernam_cipher(CypherText,Key)

@app.route('/form3',methods= ['POST'])
def form3():
    m1 = request.form['m1']
    m2 = request.form['m2']
    if m1 and m2:
        return jsonify({'output':"Wow At Last you have done it"})
    return jsonify({'error' : 'Missing data!'})


#function to add plaintext and key value to the database
def addInDb(plaintext,key):
    db.create_all()
    allUsers=text_key.query.all()
    flag=0
    for x in allUsers:
    	if x.plainText==plaintext and x.key==key:
    		flag=1
    if flag==0:
    	new_item=text_key(plaintext,key)
    	db.session.add(new_item)
    	db.session.commit()

# temporary function to view what is stored in the database
@app.route("/view")
def userFetch():
    db.create_all()
    allUsers=text_key.query.all()
    diction = {"pairs":[]}
    for x in allUsers:
        diction["pairs"].append({"plaintext":x.plainText,"key":x.key})
        # strf += str(x.rollnumber)+" "+x.name+" "+x.email + "\n"
    return jsonify(diction)


# function to check whether the text passed as parameter consists of something other than the binary bits
# if it consists of something else then the function will return 0 else it will return 1
# example usage a=check_valid_text("100010") :: here a = 1
# example usage a=check_valid_text("102010") :: here a = 0

def check_valid_text(text):
	for x in text:
		if x!='1' and x!='0':
			return 0
	return 1
# function to calculate xor of two characters
def xor(a, b):
    if a == '0' and b == '0':
        return "0" 
    if a == '0' and b == '1':
        return "1" 
    if a == '1' and b == '0':
        return "1" 
    if a == '1' and b == '1':
        return "0" 
# overall function to check the validity of plain text and cipher text in vernam cipher 
# it displays the appropriate text message 
# if valid the function automatically commits to the database also
def vernam_cipher(plaintext,key):
	if key and plaintext:
		if check_valid_text(plaintext) and check_valid_text(key):
			if len(plaintext)<=len(key):
				# adding plaintext and key pair to the database
				addInDb(plaintext,key)
				# calculating the output by calling the xor funciton repetedly
				output=""
				for i in range(0,len(plaintext)):
					output+=xor(plaintext[i],key[i])
				return jsonify({'output':output})
			return jsonify({'output':"Length of key >= PlainText!"})	
		return jsonify({'output':"Enter binary string!"})	
	return jsonify({'output':"Missing data!"})	


if __name__ == '__main__':
    app.run(debug=True)