from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import md5
import os, binascii
import datetime
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'projectBoard')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/reg', methods=['POST'])
def register():

    if len(request.form['first_name']) < 1:
        first_name = False
        flash('field cannot be empty', 'first_name')
    elif request.form['first_name'].isalpha() is False:
        first_name = False
        flash('field must contain only alphabetic characters', 'first_name')
    else:
        first_name = True

    if len(request.form['last_name']) < 1:
          last_name = False
          flash("field cannot be empty", 'last_name')
    elif (request.form['last_name']).isalpha() is False:
          last_name = False
          flash("field must contain only alphabetic characters", 'last_name')
    else:
          last_name = True

    if len(request.form['email']) < 1:
          email1 = False
          flash("field cannot be empty", 'email1')
    elif not EMAIL_REGEX.match(request.form['email']):
          email1 = False
          flash('email must be valid email', 'email1')
    else:
          email1 = True

    regQuery = "SELECT email FROM users WHERE email = :email"
    regData = {'email': request.form['email']}
    regEmail = mysql.query_db(regQuery, regData)
    if len(regEmail) > 0:
        email2 = False
        flash('email must be unique', 'email2')
    else:
        email2 = True

    print request.form['birthday']
    if request.form['birthday'] != '':
        if datetime.datetime.now() < datetime.datetime.strptime(request.form['birthday'], '%Y-%m-%d'):
            birthday = False
            flash('dob must be from the past', 'birthday')
    else:
        birthday = True

    if len(request.form['password']) < 8:
          password = False
          flash("password must be at least 8 characters", 'password')
    else:
        password = True

    if first_name is True and last_name is True and email1 is True and email2 is True and birthday is True and password is True:

        password = request.form['password']
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, birthday, password, salt, created_at, updated_at)\
                 VALUES (:first_name, :last_name, :email, :birthday, :hashed_pw, :salt, NOW(), NOW())"

        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'birthday': request.form['birthday'],
                'hashed_pw': hashed_pw,
                'salt': salt               }

        mysql.query_db(query, data)

        return redirect('/dashboard')
    else:
        return redirect('/')

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

@app.route('/dashboard')
def render_dashboard():
    query1 = "SELECT * FROM projects WHERE status = 'incomplete'"
    current_projects = mysql.query_db(query1)

    query2 = "SELECT * FROM projects WHERE status = 'complete'"
    completed_projects = mysql.query_db(query2)

    return render_template('dashboard.html', current_projects = current_projects, completed_projects = completed_projects)


app.run(debug=True)
