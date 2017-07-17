from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
import md5
import os, binascii
import datetime
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

    query2 = "SELECT messages.id AS message_primary_id, messages.user_id AS message_user_id, messages.message AS message_content, messages.created_at AS message_created_at, usersA.id AS message_user, usersA.first_name AS message_user_fn, usersA.last_name AS message_user_ln, COUNT(comments.comment) AS comment_count, GROUP_CONCAT(comments.comment) AS comment_content, GROUP_CONCAT(comments.created_at) AS comment_created_at, GROUP_CONCAT(usersB.first_name) AS comment_user_fn, GROUP_CONCAT(usersB.last_name) AS comment_user_ln\
    FROM messages JOIN users AS usersA ON usersA.id = messages.user_id LEFT JOIN comments ON messages.id = comments.message_id LEFT JOIN users AS usersB ON comments.user_id = usersB.id GROUP BY messages.id"


    messages = mysql.query_db(query2)
    for message in messages:
        if message['comment_count'] > 0:
            message['comment_content_py'] = []
            for count in range(0, message['comment_count']):
                message['comment_content_py'].append(message['comment_content'].split(',')[count])
            print message




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

@app.route('/post_comment/<message_id>', methods = ['POST'])
def post_comment(message_id):
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at)\
             VALUES (:message_id, :user_id, :comment, NOW(), NOW())"

    data = {
            'message_id': message_id,
            'user_id': session['user_id'],
            'comment': request.form['comment']
    }

    mysql.query_db(query, data)

    return redirect('/wall')

app.run(debug=True)
