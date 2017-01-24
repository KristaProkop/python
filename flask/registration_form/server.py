from flask import Flask, redirect, request, render_template, session, flash
import re
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'secretkey'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/validate', methods=['POST'])
def validation():
    first_name = str(request.form['first_name'])
    last_name = str(request.form['last_name'])
    email = str(request.form['email'])
    password1 = str(request.form['password1'])
    password2 = str(request.form['password2'])
    dob = str(request.form['dob'])
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        # TODO: add check for date in the past
    except:
        flash("Please enter date in exact format: yyyy-mm-dd")
        return redirect('/')
    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password1) < 1 or len(password2) < 1:
        flash("All fields are required. Please complete all fields and resubmit.")
    elif any(filter(str.isdigit, first_name)) or any(filter(str.isdigit, last_name)):
        flash("Names cannot contain numbers. Please try again.")
    elif len(password1) < 9:
        flash("Password must be 8 or more characters")
    elif password1 != password2:
        flash("Passwords must match")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success! Thanks for registering, {}".format(first_name))
    return redirect('/')
   
app.run(debug=True) 
