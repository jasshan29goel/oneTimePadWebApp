from exp3 import db, text, quiz

# function to check whether the text passed as parameter consists of something other than the binary bits
# if it consists of something else then the function will return 0 else it
# will return 1
def check_valid_text(text):
    for x in text:
        if x != '1' and x != '0':
            return 0
    return 1
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


# database element class
class text_key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plainText = db.Column(db.String)
    key = db.Column(db.String)

    def __init__(self, plainText, key):
        self.plainText = plainText
        self.key = key

    def __repr__(self):
        return '<User %r>' % self.plainText


class combos(text.Model):
    id = text.Column(text.Integer, primary_key=True)
    plainText = text.Column(text.String)

    def __init__(self, plainText):
        self.plainText = plainText

    def __repr__(self):
        return '<User %r>' % self.plainText


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