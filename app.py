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
def index():
    return render_template('test.html')


@app.route('/form1b3',methods= ['POST'])
def form1b3():
    plainText1 = request.form['plainText1']
    key1 = request.form['key1']

	# adding plaintext and key pair to the database
    addInDb(plainText1,key1)

    output = str(int(plainText1) + int(key1))
    if key1 and plainText1:
        return jsonify({'output':output})
    return jsonify({'error' : 'Missing data!'})

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

	# adding plaintext and key pair to the database
    addInDb(PlainText,Key)

    output = str(int(PlainText) ^ int(Key))
    if PlainText and Key:
        return jsonify({'output':output})
    return jsonify({'error' : 'Missing data!'})


@app.route('/form4b',methods= ['POST'])
def form4b():
    CypherText = request.form['CypherText']
    Key = request.form['Key']
    output = str(int(CypherText) ^ int(Key))
    if CypherText and Key:
        return jsonify({'output':output})
    return jsonify({'error' : 'Missing data!'})
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

if __name__ == '__main__':
    app.run(debug=True)