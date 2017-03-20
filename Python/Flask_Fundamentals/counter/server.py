from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    counter = 0
    if 'counter' not in session:
         session['counter']= 1
    else:
         session['counter'] = int(session['counter']) + 1

    print session

    return render_template("index.html")

@app.route('/ninja')
def ninja():
    session['counter'] = int(session['counter']) + 1
    return redirect('/')

@app.route('/hacker')
def hacker():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
