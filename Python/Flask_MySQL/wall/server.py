from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_reg')
# our index route will handle rendering our form
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/reg', methods=['POST'])
def register():
    if len(request.form['first_name']) < 2 or request.form['first_name'].isalpha() is False:
        flash("letters only, at least 2 characters", 'category1')
        # return redirect('/')
    if len(request.form['last_name']) < 2 or request.form['last_name'].isalpha() is False:
        flash("letters only, at least 2 characters", 'category2')
        # return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!", 'category3')
        # return redirect('/')
    if len(request.form['password']) < 8:
        flash("at least 8 characters", 'category4')
        # return redirect('/')
    if request.form['pconf'] != request.form['password']:
        flash('must match password', 'category5')
        # return redirect('/')
    if len(request.form['first_name']) >= 2 and request.form['first_name'].isalpha() and len(request.form['last_name']) >= 2 and request.form['last_name'].isalpha() and EMAIL_REGEX.match(request.form['email']) and len(request.form['password']) >= 8 and request.form['password'] == request.form['pconf']:
        flash('success', 'category6')


        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)

        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at)\
                 VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
    # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'pw_hash': pw_hash               }
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # return redirect('/')
        # query2 = "SELECT email, created_at FROM user_email"
        # email_list = mysql.query_db(query2)
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']
    # bcrypt.check_password_hash(pw_hash, )
    user_query = "SELECT * FROM users WHERE email = :email"
    query_data = { 'email': email }
    session['user'] = mysql.query_db(user_query, query_data)
    print session['user'] # user will be returned in a list
    if bcrypt.check_password_hash(session['user'][0]['pw_hash'], password):
        flash("You are logged in!", 'category7')
    else:
        flash('Login unsuccessful!', 'category8')
    return render_template('wall.html', this_user = session['user'])
  # set flash error message and redirect to login page
@app.route('/post_message', methods=['POST'])
def post_message():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
             VALUES (:user_id, :message, NOW(), NOW())"
        # We'll then cr eate a dictionary of data from the POST data received.
    data = {
             'user_id': session['user'][0]['id'],
             'message': request.form['message']
           }
        # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)


    query2 = "SELECT users.first_name, users.last_name, messages.id, messages.created_at, messages.message\
              FROM users\
              JOIN messages ON users.id = messages.user_id"
    session['messages'] = mysql.query_db(query2)
    return render_template('wall.html', this_user = session['user'], message_array = session['messages'])
@app.route('/post_comment', methods=['POST'])
def post_comment():
    # query2 = "SELECT users.first_name, users.last_name, messages.created_at, messages.message\
    #           FROM users\
    #           JOIN messages ON users.id = messages.user_id"
    # messages = mysql.query_db(query2)

    this_message = request.form['messagenum']

    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at)\
             VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    #     # We'll then create a dictionary of data from the POST data received.
    data = {
            'user_id': session['user'][0]['id'],
            'message_id': request.form['messagenum'],
            'comment': request.form['comment']
           }
    # #     # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    #

    query2 = "SELECT users.first_name, users.last_name, messages.id, comments.created_at, comments.comment, comments.user_id\
             FROM users\
             JOIN messages ON users.id = messages.user_id\
             JOIN comments ON users.id = comments.user_id\
             WHERE comments.message_id = :message_id"

    data2 = {
             'message_id': this_message
            }
    session['comments'] = mysql.query_db(query2, data2)
    print session['comments']

    # querydc = "SELECT users.first_name, users.last_name\
    #             FROM users\
    #             WHERE users.id = :user_id"
    # datadc = {
    #           'user_id': comments['user_id']
    #          }
    # # name = mysql.query_db(querydc, datadc)
    # print name


    #return render_template('wall.html', this_user = session['user'], comment_array = messages)
    return render_template('wall.html', this_user = session['user'], message_array = session['messages'], comment_array = session['comments'])
app.run(debug=True)
