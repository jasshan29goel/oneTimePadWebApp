from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import itertools

app = Flask(__name__)
                                    

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
quiz = SQLAlchemy(app)
class Questionclass(quiz.Model):
    id = quiz.Column(quiz.Integer, primary_key=True)
    Question = quiz.Column(quiz.String)
    Option1 = quiz.Column(quiz.String)
    Option2 = quiz.Column(quiz.String)
    Option3 = quiz.Column(quiz.String)
    Answer = quiz.Column(quiz.String)

    def __init__(self,Question, Option1,Option2, Option3,Answer):
        self.Question = Question
        self.Option1 = Option1
        self.Option2 = Option2
        self.Option3 = Option3
        self.Answer = Answer


@app.route('/')
def Quizzes():
    return render_template('Quizzes.html')

def addInquiz(Question,Option1,Option2,Option3,Answer):
    quiz.create_all()
    allUsers=Questionclass.query.all()
    new_item=Questionclass(Question,Option1,Option2,Option3,Answer)
    quiz.session.add(new_item)
    quiz.session.commit()
    def __repr__(self):
        return '<User %r>' % self.Question

@app.route("/view")
def userFetch():
    quiz.create_all()
    allUsers=Questionclass.query.all()
    diction = {"Questions":[]}
    for x in allUsers:
        diction["Questions"].append({"Question":x.Question,"Option1":x.Option1,"Option2":x.Option2,"Option3":x.Option3, "Answer":x.Answer})
    return jsonify(diction)

addInquiz("Q1", 1,2,3,1)
addInquiz("Q2", 1,2,3,2)
addInquiz("Q3", 1,2,3,3)
addInquiz("Q4", 1,2,3,4)
addInquiz("Q5", 1,2,3,5)
addInquiz("Q6", 1,2,3,6)
addInquiz("Q7", 1,2,3,7)
addInquiz("Q8", 1,2,3,8)
addInquiz("Q9", 1,2,3,9)
addInquiz("Q10", 1,2,3,10)

if __name__ == '__main__':
    app.run(port='8080')
