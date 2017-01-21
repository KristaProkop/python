from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secretkey' 

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def show_results():
  return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

def create_student():
   session['name'] = request.form['name']
   session['language'] = request.form['language']
   session['location'] = request.form['location']
   session['comment'] = request.form['comment']
   return redirect('/result')
   
app.run(debug=True) 