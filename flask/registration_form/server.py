from flask import Flask, redirect, request, render_template, session, flash

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_student():
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password1']) < 1 or len(request.form['password2']) < 1:
        flash("All fields are required. Please complete all fields and resubmit.")
    else:
        flash("Success! your name is {}".format(request.form['name']))
    return redirect('/')
   
app.run(debug=True) 

# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match