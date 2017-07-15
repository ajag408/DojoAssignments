from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'books')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/render_add')
def render_add():
  return render_template("add.html")

@app.route('/add', methods=['POST'])
def add():


app.run(debug=True)
