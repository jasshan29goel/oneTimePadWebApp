from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# database initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Error(Exception):
   """Base class for other exceptions"""
   pass
class NullError(Error):
   """Raised when the input value is Null"""
   pass
class BinaryError(Error):
   """Raised when the input value is Null"""
   pass
class KeyToSmallError(Error):
   """Raised when the input value is Null"""
   pass



class binaryString(object):
    def __init__(self, text):
        if not text : 	
            raise NullError
        if not check_valid_text(text) : 
            raise BinaryError
        self.text = text

	# new should be the key and self can be plaintext or ciphertext
    def __xor__(self,new):
        if len(self.text) > len(new.text):
        	raise KeyToSmallError
        addInDb(self.text,new.text)
        output=""
        for i in range(0,len(self.text)):
            output+=xor(self.text[i],new.text[i])
       	return output

        



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
@app.route('/Further.html')
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

    try:
	    text1=binaryString(PlainText)
	    text2=binaryString(Key)
	    output=text1^text2
	    return jsonify({'output':output})	
    except NullError:
	    return jsonify({'output':"Missing data!"})	
    except BinaryError:
	    return jsonify({'output':"Enter binary string!"})	
    except KeyToSmallError:
	    return jsonify({'output':"Key too small!"})	


@app.route('/form4b',methods= ['POST'])
def form4b():
    CypherText = request.form['CypherText']
    Key = request.form['Key']

    try:
	    text1=binaryString(CypherText)
	    text2=binaryString(Key)
	    output=text1^text2
	    return jsonify({'output':output})	
    except NullError:
	    return jsonify({'output':"Missing data!"})	
    except BinaryError:
	    return jsonify({'output':"Enter binary string!"})	
    except KeyToSmallError:
	    return jsonify({'output':"Key too small!"})

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


if __name__ == '__main__':
    app.run(debug=True)