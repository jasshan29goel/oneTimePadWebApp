from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, validators,TextField
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
class Form_1(FlaskForm):
    """
    form1 class will have Plaintext and key
    """
    plaintext1 = IntegerField('Plain Text',[validators.InputRequired()], default="1101") 
    key1 = IntegerField('Key',[validators.InputRequired()], default="100001") 
    ciphertext1 = IntegerField('Ciphertext')

class Form_2(FlaskForm):
    """
    form2 class will have Plaintext and key
    """
    key2= TextField('Key',[validators.InputRequired()], default="100001") 
    pairs2 = TextField('Pairs')

@app.route('/', methods = ['GET','POST'] )
def index():
    """
    View will render index.html page.
    """
    answer=Answer()
    vernam = Vernam()
    form_1=Form_1()
    form_2=Form_2()
    """
    Temprorily printing plaintext in ciphertext vernam . Later on we can modify what we want to print. 
    """
    vernam.ciphertext=vernam.plaintext 
    """
    Temprorily printing plaintext +100 in ciphertext  . Later on we can modify what we want to print. 
    """
    form_1.ciphertext1.data=(int(form_1.plaintext1.data)+100) 

    """
    Temprorily printing key,key pair thrice  in ciphertext  . Later on we can modify what we want to print. 
    """

    form_2.pairs2.data=str(form_2.key2.data)+","+str(form_2.key2.data)+"\n"
    form_2.pairs2.data+=str(form_2.key2.data)+","+str(form_2.key2.data)+"\n"
    form_2.pairs2.data+=str(form_2.key2.data)+","+str(form_2.key2.data)+"\n"

    if vernam.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer,form1=form_1,form2=form_2)
    if  answer.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer,form1=form_1,form2=form_2)
    if  form_1.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer,form1=form_1,form2=form_2)
    if  form_2.validate_on_submit():
        return render_template('test.html', form4 = vernam, form3 = answer,form1=form_1,form2=form_2)
    return render_template('test.html',form4 = vernam, form3 =answer,form1=form_1,form2=form_2)           

if __name__ == '__main__':
    app.run(debug= True, port =8092)