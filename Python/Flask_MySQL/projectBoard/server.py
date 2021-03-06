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

    if request.form['birthday'] != '':
        if datetime.datetime.now() < datetime.datetime.strptime(request.form['birthday'], '%Y-%m-%d'):
            birthday = False
            flash('dob must be from the past', 'birthday')
        else:
            birthday = True
    else:
        birthday = False

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
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/dashboard')
def render_dashboard():
    query1 = "SELECT * FROM projects WHERE status = 'incomplete'"
    current_projects = mysql.query_db(query1)
    for project in current_projects:
        project['deadline'] = project['deadline'].strftime('%m/%d/%Y')

    query2 = "SELECT * FROM projects WHERE status = 'complete'"
    completed_projects = mysql.query_db(query2)
    for project in completed_projects:
        project['deadline'] = project['deadline'].strftime('%m/%d/%Y')
        project['dateCompleted'] = project['dateCompleted'].strftime('%m/%d/%Y')

    return render_template('dashboard.html', current_projects = current_projects, completed_projects = completed_projects)

@app.route('/add_project')
def render_add_project():
    return render_template('add_project.html')

@app.route('/add_project', methods = ['POST'])
def add_project():
    if len(request.form['project_name']) < 1:
        project_name = False
    else:
        project_name = True

    if request.form['deadline'] != '':
        if datetime.datetime.now() > datetime.datetime.strptime(request.form['deadline'], '%Y-%m-%d'):
            deadline = False
        else:
            deadline = True
    else:
        deadline = False

    if project_name is True and deadline is True:
        query = "INSERT INTO projects (name, deadline, description, status, created_at, updated_at)\
                 VALUES (:name, :deadline, :description, :status, NOW(), NOW())"

        data = {
                'name': request.form['project_name'],
                'deadline': request.form['deadline'],
                'description': request.form['description'],
                'status': 'incomplete'
        }

        mysql.query_db(query, data)

        return redirect('/dashboard')

    else:
        return redirect('/add_project')

@app.route('/show/<id>')
def show(id):
    query = "SELECT * FROM projects WHERE id = :id"
    data = {'id': id}
    project = mysql.query_db(query, data)
    if project[0]['description'] == '':
        project[0]['description'] = 'N/A'
    project[0]['deadline'] = project[0]['deadline'].strftime('%m/%d/%Y')
    if project[0]['status'] == 'incomplete':
        project[0]['dateCompleted'] = 'N/A'
    project = project[0]
    return render_template('show.html', project = project)

@app.route('/delete/<id>')
def delete(id):
    query = "DELETE FROM projects WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/dashboard')

@app.route('/complete/<id>')
def complete(id):
    query = "UPDATE projects SET status = :status, dateCompleted = NOW() WHERE id = :id"
    data = {
             'status': 'complete',
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/dashboard')

app.run(debug=True)
