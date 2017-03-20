from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')

def index():
    if 'won' not in session:
        session['won'] = 1
    if 'lucky' not in session:
        lucky=random.randrange(0,101)
        session['lucky'] = lucky
    print session


    return render_template("index.html")


@app.route('/guess1', methods=['POST'])
def guess1():
    guess = request.form['guess']
    if int(guess) == session['lucky']:
        session['won'] = 2
    return redirect('/')

@app.route('/play1', methods = ['POST'])
def playagain():
    session['won']=1
    session.pop('lucky')
    return redirect('/')



app.run(debug=True)
