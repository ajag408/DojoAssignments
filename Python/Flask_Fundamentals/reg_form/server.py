from flask import Flask, render_template, request, redirect, session, flash
import re
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
          Off = True
          flash("email cannot be empty!", 'email')
      elif not EMAIL_REGEX.match(request.form['email']):
          Off = True
          flash('email must be valid email', 'email')
      else:
          Off = False

      if len(request.form['first_name']) < 1:
          Off = True
          flash("name cannot be empty!", 'fName')
      elif (request.form['first_name']).isalpha() is False:
          Off = True
          flash("only letters please", 'fName')
      else:
          Off = False

      if len(request.form['last_name']) < 1:
          Off = True
          flash("name cannot be empty!", 'lName')
      elif (request.form['last_name']).isalpha() is False:
          Off = True
          flash("only letters please", 'lName')
      else:
          Off = False

      if len(request.form['password']) <= 8:
          Off = True
          flash("password must be 8 characters", 'pword')
      else:
          if len(request.form['confirm_password']) < 1:
              Off = True
              flash("confirm password", 'cword')
          elif request.form['password'] != request.form['confirm_password']:
             Off = True
             flash('password must match confirmation', 'cword')
          else:
              Off = False



      if Off is False:
          flash('Thank you for submitting your information', 'success')

      return redirect('/')

app.run(debug=True)
