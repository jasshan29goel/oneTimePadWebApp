from flask import Flask, request, render_template, jsonify
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

    def __init__(self, Question, Option1, Option2, Option3, Answer):
        self.Question = Question
        self.Option1 = Option1
        self.Option2 = Option2
        self.Option3 = Option3
        self.Answer = Answer


@app.route('/')
def Quizzes():
    return render_template('Quizzes.html')


def addInquiz(Question, Option1, Option2, Option3, Answer):
    quiz.create_all()
    allUsers = Questionclass.query.all()
    new_item = Questionclass(Question, Option1, Option2, Option3, Answer)
    quiz.session.add(new_item)
    quiz.session.commit()

    def __repr__(self):
        return '<User %r>' % self.Question


@app.route("/view")
def userFetch():
    quiz.create_all()
    allUsers = Questionclass.query.all()
    diction = {"Questions": []}
    for x in allUsers:
        diction["Questions"].append({"Question": x.Question,
                                     "Option1": x.Option1,
                                     "Option2": x.Option2,
                                     "Option3": x.Option3,
                                     "Answer": x.Answer})
    return jsonify(diction)


addInquiz(
    "For a perfect encryption scheme, the number of keys is at least the size of the message space",
    "True",
    "False",
    "No encryption scheme is perfect",
    1)
addInquiz(
    "Calculate the vernam cipher of 101010(plaintext) and 010101(key)",
    "000000",
    "111111",
    "The input given is invalid",
    2)
addInquiz("What is one time pad", "Destroying the key after it's use",
          "Using one key for all the encryption", "None of the above", 1)
addInquiz(
    "Which of the following is not a requirement of perfect secrecy",
    "key should be truly random",
    "Plaintext should be atleast as long as key",
    "The keys should be destroyed after use",
    2)
addInquiz(
    "Which of the following is a not a correct drawback of One time pad(OTP)",
    "Truly random key is impossible",
    "Secure transfer of key which is as long as plaintext",
    "The ciphertext can be decrypted with infinite computational power",
    3)
addInquiz(
    "Calculate the vernam cipher of 101010(plaintext) and 010(key)",
    "000000",
    "111111",
    "The input given is invalid",
    3)
addInquiz(
    "In an encryption scheme where the key is reused 10010 and 01010 both have the same cipher text",
    "The key may be 00011 and the algorithm may be AND",
    "The key may be 00011 and the algorithm may be XOR",
    "The key may be 11111 and the algorithm may be OR",
    7)
addInquiz(
    "If perfect secrecy is possible why dont people/organization use it everywhere",
    "A lot of people need to know the key hence the security of the encryption is compromised",
    "Transferring the correct key which is as long as the message is not possible",
    "Both of the above",
    3)
addInquiz(
    "Calculate the vernam cipher of 111(plaintext) and 10100(key)",
    "010",
    "011",
    "The input given is invalid",
    1)
addInquiz(
    "In an encryption scheme two plaintext have the same cipher text.Is this encryption scheme good one to use",
    "Yes",
    "NO",
    "Depends on other parameters",
    2)

if __name__ == '__main__':
    app.run(port='8080')
