from flask import Flask, render_template, request, redirect, session, flash
import re
import time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
# ".+@.+"
@app.route('/')
def index():
  # if len(request.form['email']) < 1:
  #      flash("email cannot be empty!", 'category1')
  # else:
  #      Email = request.form['email']
  # if len(request.form['first_name']) < 1:
  #      flash("name cannot be empty!", 'category2')
  # else:
  #      fName = request.form['first_name']
  # if len(request.form['last_name']) < 1:
  #      flash("name cannot be empty!", 'category3')
  # else:
  #      lName = request.form['last_name']
  # if len(request.form['password']) < 1:
  #      flash("must create password", 'category4')
  # else:
  #      Password = request.form['password']
  # if len(request.form['confirm_password']) < 1:
  #      flash("confirm password", 'category5')
  # else:
  #      cPassword = request.form['confirm_password']

  return render_template("index.html")
@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
          Off1 = True
          flash("email cannot be empty!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
          Off1 = True
          flash('email must be valid email', 'email')
    else:
          Off1 = False

    if len(request.form['first_name']) < 1:
          Off2 = True
          flash("name cannot be empty!", 'fName')
    elif (request.form['first_name']).isalpha() is False:
          Off2 = True
          flash("only letters please", 'fName')
    else:
          Off2 = False

    if len(request.form['last_name']) < 1:
          Off3 = True
          flash("name cannot be empty!", 'lName')
    elif (request.form['last_name']).isalpha() is False:
          Off3 = True
          flash("only letters please", 'lName')
    else:
          Off3 = False

    if len(request.form['password']) <= 8:
          Off4 = True
          flash("password must be 8 characters", 'pword')
    elif request.form['password'].isalpha() is True or request.form['password'].islower() is True:
          Off4 = True
          flash('password must have at least one uppercase letter and at least one digit', 'pword')
    else:
          if len(request.form['confirm_password']) < 1:
              Off4 = True
              flash("confirm password", 'cword')
          elif request.form['password'] != request.form['confirm_password']:
             Off4 = True
             flash('password must match confirmation', 'cword')
          else:
              Off4 = False

    if len(request.form['birthdate']) <= 1:
          Off5 = True
          flash('birthdate must be valid entry', 'bday')
    else:
        birthdate = time.mktime(time.strptime(request.form['birthdate'], '%Y-%m-%d'))
        current_time = time.time()
        if birthdate>current_time:
            Off5 = True
            flash('birthdate must be in past', 'bday')
        else:
            Off5 = False

    if Off1 is False and Off2 is False and Off3 is False and Off4 is False and Off5 is False:
          flash('Thank you for submitting your information', 'success')

    return redirect('/')

app.run(debug=True)
