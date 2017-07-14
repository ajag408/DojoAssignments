from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
import md5
import os, binascii
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
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
        return redirect('/')
    if len(request.form['last_name']) < 2 or request.form['last_name'].isalpha() is False:
        flash("letters only, at least 2 characters", 'category2')
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!", 'category3')
        return redirect('/')
    if len(request.form['password']) < 8:
        flash("at least 8 characters", 'category4')
        return redirect('/')
    if request.form['pconf'] != request.form['password']:
        flash('must match password', 'category5')
        return redirect('/')
    if len(request.form['first_name']) >= 2 and request.form['first_name'].isalpha() and len(request.form['last_name']) >= 2 and request.form['last_name'].isalpha() and EMAIL_REGEX.match(request.form['email']) and len(request.form['password']) >= 8 and request.form['password'] == request.form['pconf']:
        flash('success', 'category6')


        password = request.form['password']
        print password
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at)\
                 VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW())"
    # We'll then create a dictionary of data from the POST data received.
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'hashed_pw': hashed_pw,
                'salt': salt               }
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # return redirect('/')
        # query2 = "SELECT email, created_at FROM user_email"
        # email_list = mysql.query_db(query2)
        return redirect('/success')
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # bcrypt.check_password_hash(pw_hash, )
    user_query = "SELECT * FROM users WHERE email = :email"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
        if user[0]['password'] == encrypted_password:
            flash("You are logged in!", 'category7')
            return redirect('/success')
        else:
            flash('Login unsuccessful: invalid password!', 'category8')
            return redirect('/')
    else:
        flash('Login unsuccessful: invalid email', 'category8')
        return redirect('/')
  # set flash error message and redirect to login page
@app.route('/success')
def render_success():
    return render_template('success.html')
app.run(debug=True)
