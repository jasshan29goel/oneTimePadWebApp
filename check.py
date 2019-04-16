# from flask import Flask,request,render_template,jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)


class Spam(object):
    def __init__(self, description, value):
        self.description = description
        self.value = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, d):
        if not d:
            raise Exception("description cannot be empty")
        self._description = d

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if not (v > 0):
            raise Exception("value must be greater than zero")
        self._value = v


mans = Spam(134, -2)

# if __name__ == '__main__':
#     app.run(debug=True)
