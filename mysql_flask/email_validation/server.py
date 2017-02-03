
from flask import Flask, redirect, render_template, request, flash, session
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'emails')
app.secret_key = "secret_key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def validate():
    session['email'] = request.form['email']
    if len(session['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
             'email': session['email']
        }
        mysql.query_db(query, data)
        return redirect('/success')
        

@app.route('/success')
def query(): 
    query = "SELECT * FROM emails"# define your query
    emails = mysql.query_db(query)# run query with query_db()
    return render_template('success.html', email_dict=emails, email_submitted=session['email']) 

#     DELETE FROM emails 
# WHERE email = email;

app.run(debug=True)

