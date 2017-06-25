from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)

@app.route('/')
def load_index():
    return render_template("index.html")

@app.route('/red')
def red():
    return jsonify(img = 'imgs/raphael.jpg', text = 'You chose Raphael!')

@app.route('/blue')
def blue():
    return jsonify(img = 'imgs/leonardo.jpg', text = 'You chose Leonardo!')

@app.route('/orange')
def orange():
    return jsonify(img = 'imgs/michelangelo.jpg', text = 'You chose Michelangelo!')

@app.route('/purple')
def purple():
    return jsonify(img = 'imgs/donatello.jpg', text = 'You chose Donatello!')

@app.route('/form', methods = ['POST'])
def delineate():
    if request.form['customColor'] == 'red' or request.form['customColor'] == 'Red':
        return render_template('index.html', text = 'You chose Raphael!', img = '/static/imgs/raphael.jpg')
    elif request.form['customColor'] == 'blue' or request.form['customColor'] == 'Blue':
        return render_template('index.html', text = 'You chose Leonardo!', img = '/static/imgs/leonardo.jpg')
    elif request.form['customColor'] == 'orange' or request.form['customColor'] == 'Orange':
        return render_template('index.html', text = 'You chose Michelangelo!', img = '/static/imgs/michelangelo.jpg')
    elif request.form['customColor'] == 'purple' or request.form['customColor'] == 'Purple':
        return render_template('index.html', text = 'You chose Donatello!', img = '/static/imgs/donatello.jpg')
    else:
        return render_template('index.html', text = "There's no ninja in that color", img = '/static/imgs/tmnt.png' )


app.run(debug=True)
