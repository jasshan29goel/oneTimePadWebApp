from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, validators
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'

class EmployeeInfo(FlaskForm):
    """
    EmployeeInfo class will have Name,Dept
    """
    fullName = StringField('Full Name',[validators.InputRequired()])
    dept = StringField('Department',[validators.InputRequired()])

class CompanyDetails(FlaskForm):
    """
    CompanyDetails will have yearOfExp. 
    """
    yearsOfExp = IntegerField('Year of Experiece',[validators.InputRequired()]) 


@app.route('/', methods = ['GET','POST'] )
def index():
    """
    View will render index.html page.
    If form is validated then showData.html will load the employee or company data.
    """
    companydetails = CompanyDetails()
    employeeInfo = EmployeeInfo()

    if companydetails.validate_on_submit():
        return render_template('index.html', form = companydetails,form1 = employeeInfo)

    if employeeInfo.validate_on_submit():
        return render_template('index.html', form1 = employeeInfo,form = companydetails)   

    return render_template('index.html',form1 = employeeInfo, form = companydetails)

if __name__ == '__main__':
    app.run(debug= True, port =8092)