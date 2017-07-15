from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
import datetime

app = Flask(__name__)
mysql = MySQLConnector(app,'books')

@app.route('/')
def index():
  query = "SELECT * FROM books"
  books = mysql.query_db(query)
  for book in books:
      book['created_at'] = book['created_at'].strftime('%b %dth %Y')
  return render_template("index.html", books = books)

@app.route('/render_add')
def render_add():
  return render_template("add.html")

@app.route('/add', methods=['POST'])
def add():
    query = "INSERT INTO books (title, author, created_at, updated_at)\
             VALUES (:title, :author, NOW(), NOW())"

    data = {
            'title': request.form['title'],
            'author': request.form['author'] }

    mysql.query_db(query, data)

    return redirect('/')

@app.route('/render_delete/<id>')
def render_delete(id):
    query = "SELECT * FROM books WHERE id = :id"
    data = {
            'id': id }
    book = mysql.query_db(query,data)
    print book
    return render_template('delete.html', book = book)

@app.route('/delete/<id>')
def delete(id):
    query = "DELETE FROM books WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
