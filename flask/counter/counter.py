from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secretkey' 

@app.route('/')

def index():
    session['variable'] = 1
    if 'counter' not in session: 
        session['counter'] = 1 
    else: 
        session['counter'] += 1 
    return render_template('index.html')

@app.route('/', methods=['POST'])
def buttons():
    if request.form['btn'] == 'Add 2':
        session['counter'] += 2
    elif request.form['btn'] == 'Reset Counter':
        session['counter'] = 1
    return render_template('index.html')

app.run(debug=True) 


