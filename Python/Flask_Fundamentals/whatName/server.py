from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def render_landingPage():
    return render_template("landingPage.html")

@app.route('/process', methods = ['POST'])
def print_name():
    print request.form['nameField']
    return redirect('/')

app.run(debug=True)
