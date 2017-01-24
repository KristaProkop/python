from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'secretkey' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_student():
    if len(request.form['name']) < 1 or len(request.form['location']) < 1: 
        flash("Please fill in all required answers!")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comment limit 120 characters")
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['language'] = request.form['language']
        session['location'] = request.form['location']
        session['comment'] = request.form['comment']
        return redirect('/show')

@app.route('/show')
def show_results():
    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
   
app.run(debug=True) 