from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def load_form():
    return render_template("form.html")

@app.route('/rgb', methods = ['POST'])
def changeColor():
    r = request.form['redVal']
    g = request.form['greenVal']
    b = request.form['blueVal']
    return render_template('form.html', r = r, g = g, b = b)

app.run(debug=True)
