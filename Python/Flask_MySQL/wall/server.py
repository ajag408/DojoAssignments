from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import md5
import os, binascii
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'wall')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/reg', methods=['POST'])
def register():
    password = request.form['password']
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()

    query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at)\
             VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"

    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'hashed_pw': hashed_pw,
            'salt': salt               }

    mysql.query_db(query, data)

    query2 = "SELECT id FROM users WHERE first_name = :first_name AND email = :email"

    data2 = {
            'first_name': request.form['first_name'],
            'email': request.form['email']
    }

    user = mysql.query_db(query2, data2)
    session['user_id'] = user[0]['id']

    return redirect('/wall')

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_query = "SELECT * FROM users WHERE email = :email"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data)

    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
        if user[0]['password'] == encrypted_password:
            session['user_id'] = user[0]['id']
            return redirect('/wall')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/wall')
def render_wall():
    query = "SELECT * FROM users WHERE id = :id"

    data = {
            'id': session['user_id']
    }

    user = mysql.query_db(query, data)

    query2 = "SELECT * FROM messages"

    messages = mysql.query_db(query2)

    return render_template('wall.html', user = user, messages = messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/post_message', methods = ['POST'])
def post_message():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
             VALUES (:user_id, :message, NOW(), NOW())"

    data = {
            'user_id': session['user_id'],
            'message': request.form['message'],
          }

    mysql.query_db(query, data)

    return redirect('/wall')

app.run(debug=True)
