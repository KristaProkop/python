from flask import Flask
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')

print mysql.query_db('SELECT * FROM friends')

app.run(debug=True)




# from flask import Flask, render_template, redirect, request
# from mysqlconnection import MySQLConnector

# app = Flask(__name__)
# app.secret_key = 'secretwords'

# mysql = MySQLConnector(app, 'mydb')

# @app.route('/')

# def index():
#     result = mysql.query_db('SELECT * FROM users')
#     print result
#     return render_template('index.html', result=result)




# app.run(debug=True)