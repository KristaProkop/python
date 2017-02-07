
from flask import Flask, redirect, render_template, request, flash, session
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'registration')
app.secret_key = "secret_key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    password = request.form['password']
    if (len(session['email']) < 1) or (len(password) < 1): 
        flash('please enter a valid email address and password')
        return redirect('/')
    else:
        try: 
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            query_data = { 'email': session['email'] }
            user = mysql.query_db(user_query, query_data) 
            if bcrypt.check_password_hash(user[0]['password'], password):
                session['id'] = user[0]['id']
                #save id to session to validate login status later
                return redirect('/success')
            else:
                flash('check your credentials and try again')
                return redirect('/')
        except: 
            flash("Please check your credentials and try again")
            return redirect('/')

@app.route('/registration', methods=['GET'])
def register():
    return render_template('registration.html')


@app.route('/register', methods=['POST'])
##Need to refactor to DRY structure
def validate():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['password_conf'] = request.form['password_conf']
    if len(session['email']) < 1:
        flash("All fields required.")
        return redirect('/registration')
    if not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/registration')
    if (len(session['first_name']) < 2) or (len(session['last_name']) < 2) or not session['first_name'].isalpha() or not session['last_name'].isalpha():
        flash("Name must be at least 2 characters and cannot contain numbers")
        return redirect('/registration')
    if (len(session['password']) < 8):
        flash("Password must be 8 or more characters")
        return redirect('/registration')
    if (session['password'] != session['password_conf']):
        flash("Passwords do not match")
        return redirect('/registration')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
             'first_name': session['first_name'],
             'last_name': session['last_name'],
             'email': session['email'],
             'password': pw_hash
        }
        mysql.query_db(query, data)
        return redirect('/success')
        

@app.route('/success')
def query(): 
    return render_template('success.html', user_email=session['email'], user_id=session['id']) 



app.run(debug=True)

