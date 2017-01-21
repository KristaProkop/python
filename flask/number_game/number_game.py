from flask import Flask, render_template,request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    session['counter'] = 0
    session['num'] = random.randrange(1, 101) 
    session['color'] = 'hide'
    session['formsubmit'] = 'show'
    session['playagain'] = 'hide'
    return render_template('index.html')


@app.route('/', methods=['POST'])
def guesses():
    if request.form['btn'] == 'Play Again':
        return index()
    if request.form['btn'] == 'Submit':
        session['counter'] += 1
        guess = request.form['guess']
        if session['num'] == int(guess):
            session['result'] = "Correct!"
            session['color'] = 'green'
            session['playagain'] = 'show'
            session['formsubmit'] = 'hide'
        else: 
            if session['counter'] < 10:
                if session['num'] > int(guess):
                    session['result'] = "too low!"
                else:
                    session['result'] = "too high!"
            if session['counter'] == 10:
                session['result'] = "Sorry! The number was " + str(session['num'])
                session['playagain'] = 'show'
                session['formsubmit'] = 'hide'
            session['color'] = 'red'
        return render_template('index.html')


app.run(debug=True) 



# # Set session like so:
# session['someKey'] = 50
# # Remove something from session like so:
# session.pop('someKey')