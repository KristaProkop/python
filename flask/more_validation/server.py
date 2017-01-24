from flask import Flask, render_template, redirect, request, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)

app.secret_key = "secret_key"

@app.route('/', methods=['GET'])

def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)

# str.isalpha() -- Returns a boolean that shows whether a string contains only alphabetic characters. Documentation here.


#time.strptime(string, format) -- Changes a string to a time using the given format. Documentation here.