from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, validators
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'

class Answer(FlaskForm):
    """
    Answer class will have response, m1, m2
    """
    response = StringField('Yes/No',[validators.InputRequired()]) 
    m1 = IntegerField('m1',[validators.InputRequired()]) 
    m2 = IntegerField('m2',[validators.InputRequired()])
class Vernam(FlaskForm):
    """
    vernam class will have Plaintext and key
    """
    plaintext = IntegerField('Plain Text',[validators.InputRequired()], default="10010011000110") 
    key = IntegerField('Key',[validators.InputRequired()], default="10101100110001") 
    ciphertext = IntegerField('Ciphertext')
@app.route('/', methods = ['GET','POST'] )
def index():
    """
    View will render index.html page.
    """
    answer=Answer()
    vernam = Vernam()
    """
    Temprorily printing plaintext in ciphertext. Later on we can modify what we want to print. 
    """
    vernam.ciphertext=vernam.plaintext 

    if vernam.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer)
    if  answer.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer)
    return render_template('test.html',form4 = vernam, form3 =answer)           

if __name__ == '__main__':
    app.run(debug= True, port =8092)