from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'email_validation_dB')
# our index route will handle rendering our form
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        flash("Success!")

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
        query = "INSERT INTO user_email (email, created_at)\
                 VALUES (:email, NOW())"
    # We'll then create a dictionary of data from the POST data received.
        data = {
                'email': request.form['email']
               }
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # return redirect('/')
        query2 = "SELECT email, created_at FROM user_email"
        email_list = mysql.query_db(query2)
        return render_template('success.html', show_el = email_list)
@app.route('/delete', methods=['POST'])
def delete():
    query = "DELETE FROM user_email WHERE email = :email"
    data = {'email': request.form['name']}
    mysql.query_db(query, data)
    query2 = "SELECT email, created_at FROM user_email"
    email_list = mysql.query_db(query2)
    return render_template("success.html", show_el = email_list)
app.run(debug=True)
