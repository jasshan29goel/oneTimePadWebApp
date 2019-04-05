from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')


@app.route('/form1b3',methods= ['POST'])
def form1b3():
    plainText1 = request.form['plainText1']
    key1 = request.form['key1']
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

if __name__ == '__main__':
    app.run(debug=True)