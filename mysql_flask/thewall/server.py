
from flask import Flask, redirect, render_template, request, flash, session
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
app.secret_key = "secret_key"


@app.route('/')
def index():
    if 'logged_in' in session:
        flash('You are already logged in')
    return render_template('index.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash("You have logged out")
    return redirect('/')

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
                session['first_name'] = user[0]['first_name']
                session['last_name'] = user[0]['last_name']
                session['logged_in'] = True
                return redirect('/wall')
            else:
                flash('check your credentials and try again')
                return redirect('/')
        except: 
            flash("Please check your credentials and try again")
            return redirect('/')

@app.route('/registration', methods=['GET'])
def register():
    return render_template('registration.html')

@app.route('/register')
def display_registration():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
##Need to refactor to DRY structure
def validate():
    if len(request.form['email']) < 1:
        flash("All fields required.")
        return redirect('/register')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/register')
    elif (len(request.form['first_name']) < 2) or (len(request.form['last_name']) < 2) or not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash("Name must be at least 2 characters and cannot contain numbers")
        return redirect('/register')
    elif (len(request.form['password']) < 8):
        flash("Password must be 8 or more characters")
        return redirect('/register')
    elif (request.form['password'] != request.form['password_conf']):
        flash("Passwords do not match")
        return redirect('/register')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'email': request.form['email'],
             'password': pw_hash
        }
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/wall')
##TODO: if no messages in DB do not show messages
def load_wall():
    query = "SELECT users.id, users.first_name, users.last_name, messages.message, messages.created_at FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at"
    messages = mysql.query_db(query)
    return render_template('wall.html', messages=messages) 

@app.route('/post_message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
             'user_id': session['id'],
             'message': request.form['message'],
        }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)

