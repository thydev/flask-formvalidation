from flask import Flask, render_template, request, session, flash, redirect
import re, datetime
app = Flask(__name__)
app.secret_key = "fs@#dSdsf132SF$#$@#()9dx"
# create a regular expression object that we can use run operations on
email_reg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
pwd_reg = re.compile('^(?=\S{3,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def result():
    # print request.form
    isValid = True
    firstname = request.form['firstname'].strip()
    lastname = request.form['lastname'].strip()
    fullname =  firstname + " " + lastname
    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    birth_date = request.form['birthdate']

    if not (len(firstname) > 0):
        flash("First name can not be blank!", "error")
        isValid = False
    if not (len(lastname) > 0):
        flash("Last name can not be blak!", "error")
        isValid = False
    if not email_reg.match(email):
        flash("Invalid Email Address!", "error")
        isValid = False
    if (len(password) < 0):
        flash("Please input your password", "error")
        isValid = False
    elif not pwd_reg.match(password):
        flash("Password must contain at least 1 uppercase, 1 lowercase, 1 number and 1 symbol", "error")
        isValid = False
    elif password != password_confirm:
        flash("Password does not match!", "error")
        isValid = False

    if not birth_date:
        flash("Please input your birth date!", "error")
        isValid = False
    else:
        # birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
        present = datetime.datetime.now().strftime("%Y-%m-%d")
        print birth_date, present, birth_date > present
        if birth_date >= present:
            flash("Birth date can not be in the future!", "error")
            isValid = False
    
    if isValid:
        flash("Thank you for submitting information!", "sucess")
        # return render_template('result.html', fullname = fullname, location = location, language = language, comment = comment )
        return redirect('/')
    else:
        return redirect('/')

app.run(debug = True)
