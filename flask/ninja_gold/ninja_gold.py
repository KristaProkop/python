from flask import Flask, render_template, request, redirect, session
import random 
import datetime


app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    if 'award' in session:
        return render_template('index.html', award=session['award'], messages=session['message_list'], subtotal=session['subtotal'])
    else: 
        session['subtotal'] = 0
        session['message_list'] = []
        return render_template('index.html', subtotal=session['subtotal'])


@app.route('/process_gold', methods=['POST'])
def calculate_gold():
    if 'reset' in request.form:
        reset()
    else:
        if 'farm' in request.form:
            award = random.randrange(10, 21) 
        if 'cave' in request.form:
            award = random.randrange(5, 11) 
        if 'house' in request.form:
            award = random.randrange(2, 6) 
        if 'casino' in request.form:
            award = random.randrange(-50, 51)
        if award < 0:
            message = "Entered a casino and lost "+str((award*-1))+ " golds...ouch (" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")) + ')'
        else: 
            message = "You have earned "+str(award)+ " golds from this play! (" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %p")) + ')'
        session['award'] = award
        session['message'] = message
        if 'message_list' not in session:
            session['message_list'] = []
        session['message_list'].append(message)
        sum_gold()
    return redirect('/')

def sum_gold():
    session['subtotal'] = session['subtotal'] + session['award']
  
def reset():
    session['subtotal'] = 0
    session['award'] = []
    session['message_list'] = []


app.run(debug=True)