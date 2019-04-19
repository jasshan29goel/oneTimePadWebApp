from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import itertools

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
text = SQLAlchemy(app)

class combos(text.Model):
    id = text.Column(text.Integer, primary_key=True)
    plainText = text.Column(text.String)

    def __init__(self,plainText):
        self.plainText = plainText

    def __repr__(self):
        return '<User %r>' % self.plainText

@app.route("/")
def create():
    text.create_all()
    allUsers=combos.query.all()

    res=["".join(seq) for seq in itertools.product("01", repeat=8)]
    for x in res:
        addintext(x)
    return "0"



@app.route("/view1")
def userFetch1():
    text.create_all()
    allUsers=combos.query.all()
    diction = {"text":[]}
    for x in allUsers:
        diction["text"].append({"text":x.plainText})
    return jsonify(diction)
def addintext(plaintext):
    text.create_all()
    allUsers=combos.query.all()
    new_item=combos(plaintext)
    text.session.add(new_item)
    text.session.commit()
if __name__ == '__main__':
    app.run(port='8080')
