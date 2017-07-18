from flask import Flask, render_template, request, redirect, url_for
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
    for user in users:
        user['created_at'] = user['created_at'].strftime('%b %dth %Y')
    return render_template('index.html', users = users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/<id>/edit')
def edit(id):
    query = "SELECT * FROM users WHERE id = :id"

    data = {
            'id': id
    }

    user = mysql.query_db(query, data)
    user[0]['first_name'] = user[0]['full_name'].split(" ")[0]
    user[0]['last_name'] = user[0]['full_name'].split(" ")[1]

    user = user[0]

    return render_template('edit.html', user = user)

@app.route('/users/<id>')
def show(id):
    query = "SELECT * FROM users WHERE id = :id"

    data = {
            'id': id
    }

    user = mysql.query_db(query, data)
    user = user[0]
    user['created_at'] = user['created_at'].strftime('%b %dth %Y')

    return render_template('show.html', user = user)

@app.route('/users/create', methods = ['POST'])
def create():
    query = "INSERT INTO users (full_name, email, created_at, updated_at)\
            VALUES (:full_name, :email, NOW(), NOW())"

    data = {
            'full_name': request.form['first_name'] + " " + request.form['last_name'],
            'email': request.form['email']
    }

    mysql.query_db(query, data)

    query2 = "SELECT id FROM users WHERE email = :email"

    data2 = {
            'email': request.form['email']
    }

    user = mysql.query_db(query2, data2)
    id = user[0]['id']

    return redirect(url_for('.show', id = id))

@app.route('/users/<id>/destroy')
def destroy(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>', methods = ['POST'])
def update(id):
    query = "UPDATE users SET full_name = :full_name, email = :email WHERE id = :id"
    data = {
             'full_name': request.form['first_name'] + " " + request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect(url_for('.show', id = id))

app.run(debug=True)
