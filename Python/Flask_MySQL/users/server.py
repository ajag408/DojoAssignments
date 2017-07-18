from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'users')

@app.route('/')
def render_index():
    return redirect('/users')

@app.route('/users')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users = users)

app.run(debug=True)
