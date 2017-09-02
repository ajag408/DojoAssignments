from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'posts')

@app.route('/')
def index():
    query = "SELECT * FROM posts"
    notes = mysql.query_db(query)
    return render_template("index.html", notes = notes)

@app.route('/post_it', methods = ['POST'])
def post_it():
    query = "INSERT INTO posts (note, created_at, updated_at)\
         VALUES (:note, NOW(), NOW())"

    data = {
            'note': request.form['note'] }

    mysql.query_db(query, data)

    query2 = "SELECT * FROM posts WHERE note = :note"
    data2 = {
            'note': request.form['note'] }
    this_post = mysql.query_db(query2,data2)
    print this_post[0]

    return render_template('fresh_post.html', this_post = this_post[0]['note'])

app.run(debug=True)
