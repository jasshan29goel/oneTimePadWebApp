from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import itertools
from exp3 import app
from exp3 import db, text, quiz
from exp3.models import binaryString, text_key, combos, Questionclass, Error, NullError, BinaryError, KeyToSmallError


class binaryString(object):
    def __init__(self, text):
        if not text:
            raise NullError
        if not check_valid_text(text):
            raise BinaryError
        self.text = text

        # new should be the key and self can be plaintext or ciphertext
    def __xor__(self, new):
        if len(self.text) > len(new.text):
            raise KeyToSmallError
        addInDb(self.text, new.text)
        output = ""
        for i in range(0, len(self.text)):
            output += xor(self.text[i], new.text[i])
        return output

    def __mod__(self, new):
        if len(self.text) > len(new.text):
            raise KeyToSmallError
        addInDb(self.text, new.text)
        output = ""
        for i in range(0, len(self.text)):
            if currentEncryptionScheme[i] == '0':
                # print("xor")
                output += xor(self.text[i], new.text[i])
            else:
                # print("And")

                output += And(self.text[i], new.text[i])
        return output
    # The functions below and above are almost same the only difference is that we are
    # adding the data into database in the function above whike nit in the
    # function below.

    def __mul__(self, new):
        if len(self.text) > len(new.text):
            raise KeyToSmallError
        output = ""
        for i in range(0, len(self.text)):
            if currentEncryptionScheme[i] == '0':
                # print("xor")
                output += xor(self.text[i], new.text[i])
            else:
                # print("And")

                output += And(self.text[i], new.text[i])
        return output




def randomNumberGenerator(arg):

    stri = ""
    if arg == 0:
        arg = 8
    for x in range(arg):
        stri += str(random.randint(0, 1))
    return stri


currentEncryptionScheme = randomNumberGenerator(100)





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


@app.route('/Quizzes.html', methods=['POST', 'GET'])
def Quizzes():
    quiz.create_all()
    allUsers = Questionclass.query.all()
    global arr
    arr = random.sample (range(0, 9), 5)
    return render_template('Quizzes.html', Question1=allUsers[arr[0]], Question2=allUsers[arr[1]],
                           Question3=allUsers[arr[2]], Question4=allUsers[arr[3]], Question5=allUsers[arr[4]])


@app.route('/Procedure.html')
def Procedure():
    return render_template('Procedure.html')


@app.route('/Further.html')
def Further():
    return render_template('Further Readings.html')


@app.route('/Feedback.html')
def Feedback():
    return render_template('Feedback.html')


@app.route('/form1b3', methods=['POST'])
def form1b3():
    plainText1 = request.form['plainText1']
    key1 = request.form['key1']
    try:
        text1 = binaryString(plainText1)
        text2 = binaryString(key1)
        output = text1 % text2
        return jsonify({'output': output})
    except NullError:
        return jsonify({'output': "Missing data!"})
    except BinaryError:
        return jsonify({'output': "Enter binary string!"})
    except KeyToSmallError:
        return jsonify({'output': "Key too small!"})


@app.route('/form1b2', methods=['POST'])
def form1b2():
    plainText1 = request.form['plainText1']
    return jsonify({'output': randomNumberGenerator(len(plainText1))})


@app.route('/form1b1', methods=['POST'])
def form1b1():
    key = request.form['key1']
    return jsonify({'output': randomNumberGenerator(len(key))})


@app.route('/form1b4', methods=['POST'])
def form1b4():
    global currentEncryptionScheme
    currentEncryptionScheme = randomNumberGenerator(80)
    return "0"


@app.route('/form2b1', methods=['POST'])
def form2b1():
    key = request.form['key2']
    try:
        text1 = binaryString(key)
    except NullError:
        return jsonify({'output': "Missing Key!"})
    except BinaryError:
        return jsonify({'output': "Enter binary string!"})
    except KeyToSmallError:
        return jsonify({'output': "Key too small!"})

    if key:
        output = ""
        # text.create_all()
        # allUsers=combos.query.all()
        res = ["".join(seq) for seq in itertools.product("01", repeat=8)]
        for x in res:
            # addintext(x)

            text1 = binaryString(x)
            text2 = binaryString(key)
            output += x + "," + text1 * text2 + "\n"
        return jsonify({'output': output})
    return jsonify({'output': 'Missing data!'})


@app.route('/form4a', methods=['POST'])
def form4a():
    PlainText = request.form['PlainText']
    Key = request.form['Key']

    try:
        text1 = binaryString(PlainText)
        text2 = binaryString(Key)
        output = text1 ^ text2
        return jsonify({'output': output})
    except NullError:
        return jsonify({'output': "Missing data!"})
    except BinaryError:
        return jsonify({'output': "Enter binary string!"})
    except KeyToSmallError:
        return jsonify({'output': "Key too small!"})


@app.route('/form4b', methods=['POST'])
def form4b():
    CypherText = request.form['CypherText']
    Key = request.form['Key']

    try:
        text1 = binaryString(CypherText)
        text2 = binaryString(Key)
        output = text1 ^ text2
        return jsonify({'output': output})
    except NullError:
        return jsonify({'output': "Missing data!"})
    except BinaryError:
        return jsonify({'output': "Enter binary string!"})
    except KeyToSmallError:
        return jsonify({'output': "Key too small!"})


@app.route('/form3', methods=['POST'])
def form3():
    key = request.form['key2']
    response = request.form['response']
    m1 = request.form['m1']
    m2 = request.form['m2']
    if not key:
        return jsonify({'output': "Please enter key"})
    if response:
        try:
            text2 = binaryString(key)
        except NullError:
            return jsonify({'output': "Missing data!"})
        except BinaryError:
            return jsonify({'output': "Enter binary string!"})
        except KeyToSmallError:
            return jsonify({'output': "Key too small!"})

        if response == 'Yes':
            text.create_all()
            allUsers = combos.query.all()
            for x in allUsers:
                text1 = binaryString(x.plainText)
                text2 = binaryString(key)
                ans = text1 * text2
                for y in allUsers:
                    text3 = binaryString(y.plainText)
                    text4 = binaryString(key)
                    ans1 = text3 * text4
                    if ans == ans1 and x.plainText != y.plainText:
                        return jsonify(
                            {'output': "Wrong Answer" + " " + x.plainText + " " + y.plainText})
            return jsonify({'output': "Right Answer"})
        elif response == 'No':
            if m1 and m2:
                try:
                    text1 = binaryString(m1)
                    text2 = binaryString(m2)
                    Key = binaryString(key)
                except NullError:
                    return jsonify({'output': "Missing data!"})
                except BinaryError:
                    return jsonify({'output': "Enter binary string!"})
                except KeyToSmallError:
                    return jsonify({'output': "Key too small!"})
                if text1 * Key == text2 * Key and m1 != m2:
                    return jsonify({'output': "Correct Answer"})
                else:
                    return jsonify({'output': "Wrong Answer"})
            else:
                return jsonify({'output': "Please enter m1 and m2"})
        else:
            return jsonify({'output': "Please Enter Yes/No"})
    return jsonify({'output': 'Please Enter Yes/No!'})


@app.route('/check', methods=['POST'])
def check():
    R1 = request.form['Q1']
    R2 = request.form['Q2']
    R3 = request.form['Q3']
    R4 = request.form['Q4']
    R5 = request.form['Q5']
    quiz.create_all()
    allUsers = Questionclass.query.all()
    Correct = "Correct Answers : "
    Wrong = "Wrong Answers : "
    Unattempted = "Unattempted  : "

    global arr
    if R1 == allUsers[arr[0]].Answer:
        Correct += "1 "
    elif R1 == '4':
        Unattempted += "1 "
    else:
        Wrong += "1 "
    if R2 == allUsers[arr[1]].Answer:
        Correct += "2 "
    elif R2 == '4':
        Unattempted += "2 "
    else:
        Wrong += "2 "
    if R3 == allUsers[arr[2]].Answer:
        Correct += "3 "
    elif R3 == '4':
        Unattempted += "3 "
    else:
        Wrong += "3 "
    if R4 == allUsers[arr[3]].Answer:
        Correct += "4 "
    elif R4 == '4':
        Unattempted += "4 "
    else:
        Wrong += "4 "
    if R5 == allUsers[arr[4]].Answer:
        Correct += "5 "
    elif R5 == '4':
        Unattempted += "5 "
    else:
        Wrong += "5 "
    Correct += "\n"
    Wrong += "\n"
    Unattempted += "\n"
    return jsonify({'output': Correct + Wrong + Unattempted})

# function to add plaintext and key value to the database


def addInDb(plaintext, key):
    db.create_all()
    allUsers = text_key.query.all()
    flag = 0
    for x in allUsers:
        if x.plainText == plaintext and x.key == key:
            flag = 1
    if flag == 0:
        new_item = text_key(plaintext, key)
        db.session.add(new_item)
        db.session.commit()


def addintext(plaintext):
    text.create_all()
    allUsers = combos.query.all()
    new_item = combos(plaintext)
    text.session.add(new_item)
    text.session.commit()

# temporary function to view what is stored in the database
@app.route("/view")
def userFetch():
    quiz.create_all()
    allUsers = Questionclass.query.all()
    diction = {"Questions": []}
    for x in allUsers:
        diction["Questions"].append({"Question": x.Question,
                                     "Option1": x.Option1,
                                     "Option2": x.Option2,
                                     "Option3": x.Option3})
    return jsonify(diction)


@app.route("/view1")
def userFetch1():
    text.create_all()
    allUsers = combos.query.all()
    diction = {"text": []}
    for x in allUsers:
        diction["text"].append({"text": x.plainText})
    return jsonify(diction)


@app.route('/delete')
def delete():
    text.create_all()
    allUsers = combos.query.all()
    for x in allUsers:
        text.session.delete(x)
    text.session.commit()
    return "0"


# function to check whether the text passed as parameter consists of something other than the binary bits
# if it consists of something else then the function will return 0 else it
# will return 1
def check_valid_text(text):
    for x in text:
        if x != '1' and x != '0':
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


def And(a, b):
    if a == '0' and b == '0':
        return "0"
    if a == '0' and b == '1':
        return "0"
    if a == '1' and b == '0':
        return "0"
    if a == '1' and b == '1':
        return "1"


