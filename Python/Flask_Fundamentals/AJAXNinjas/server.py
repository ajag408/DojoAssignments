from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)

@app.route('/')
def load_index():
    return render_template("index.html")

@app.route('/red')
def red():
    return jsonify(img = 'imgs/raphael.jpg', text = 'You chose Raphael!')

app.run(debug=True)
