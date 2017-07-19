from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
import datetime

app = Flask(__name__)
mysql = MySQLConnector(app,'books_and_quotes')


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
    return render_template('delete.html', book = book)

@app.route('/delete/<id>')
def delete(id):
    query2 = "DELETE FROM quotes WHERE book_id = :book_id"
    data2 = {'book_id': id}
    mysql.query_db(query2, data2)

    query1 = "DELETE FROM books WHERE id = :id"
    data1 = {'id': id}
    mysql.query_db(query1, data1)

    return redirect('/')

@app.route('/add_quote/<id>')
def render_add_quote(id):
    query = "SELECT * FROM books WHERE id = :id"

    data = {
            'id': id
    }

    book = mysql.query_db(query, data)
    book = book[0]

    return render_template('add_quote.html', book = book)

@app.route('/add_quote/<id>', methods = ['POST'])
def add_quote(id):
    query = "INSERT INTO quotes (book_id, quote, created_at, updated_at)\
             VALUES (:book_id, :quote, NOW(), NOW())"

    data = {
            'book_id': id,
            'quote': request.form['quote']
    }

    mysql.query_db(query,data)

    return redirect('/')

@app.route('/quotes/<id>')
def view_quotes(id):
    query1 = "SELECT title FROM books WHERE id = :id"
    data1 = {
            'id': id
    }
    book = mysql.query_db(query1,data1)
    book = book[0]

    query2 = "SELECT quote FROM quotes WHERE book_id = :book_id"

    data2 = {
            'book_id': id
    }

    quotes = mysql.query_db(query2, data2)

    return render_template('quotes.html', book = book, quotes = quotes)

app.run(debug=True)
