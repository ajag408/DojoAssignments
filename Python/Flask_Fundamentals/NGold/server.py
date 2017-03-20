from flask import Flask, render_template, request, redirect, session
import random, time, datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')

def index():
    if 'activity' not in session:
        session['activity'] = ""
    if 'earning' not in session:
        session['earning'] = 0

    print session
    return render_template("index.html")

@app.route('/process_money', methods = ['POST'])
def process_money():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    if request.form['building'] == 'farm':
        temp_earn = random.randrange(10, 21)
        session['earning']+=temp_earn
        session['activity'] += "Earned " +str(temp_earn)+ " golds from the farm! ("+ st + ")\n"
    elif request.form['building'] == 'cave':
        temp_earn = random.randrange(5, 11)
        session['earning']+=temp_earn
        session['activity'] += "Earned " +str(temp_earn)+ " golds from the cave! ("+ st +")\n"
    elif request.form['building'] == 'house':
        temp_earn = random.randrange(2, 6)
        session['earning']+=temp_earn
        session['activity'] += "Earned " +str(temp_earn)+ " golds from the house! ("+st+")\n"
    elif request.form['building'] == 'casino':
        temp_earn = random.randrange(-50, 51)
        session['earning']+=temp_earn
        if temp_earn<0:
            session['activity'] += "Lost " +str(temp_earn)+ " golds! ("+st+")\n"
        else:
            session['activity'] += "Earned " +str(temp_earn)+ " golds from the casino! ("+st+")\n"
    return redirect('/')
app.run(debug=True)
