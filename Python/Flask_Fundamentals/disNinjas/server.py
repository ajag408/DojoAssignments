from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template("home.html")

@app.route('/ninja')
def show_all4():
    return render_template('all.html')

@app.route('/ninja/<color>')
def show_ninja(color):
    if color == 'blue':
        return render_template('leonardo.html')
    elif color == 'orange':
        return render_template('michelangelo.html')
    elif color == 'red':
        return render_template('raphael.html')
    elif color == 'purple':
        return render_template('donatello.html')
    else:
        return render_template('mfox.html')

app.run(debug=True)
