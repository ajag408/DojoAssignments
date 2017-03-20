from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
".+@.+"
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
           flash("email cannot be empty!", 'category1')
      else:
           Email = request.form['email']
      if len(request.form['first_name']) < 1:
           flash("name cannot be empty!", 'category2')
      elif (request.form['first_name']).isalpha() is False:
           flash("only letters please", 'category6')
      else:
           fName = request.form['first_name']
      if len(request.form['last_name']) < 1:
           flash("name cannot be empty!", 'category3')
      elif (request.form['last_name']).isalpha() is False:
           flash("only letters please", 'category6')
      else:
           lName = request.form['last_name']
      if len(request.form['password']) <= 8:
           flash("password must be 8 characters", 'category4')
      else:
           Password = request.form['password']
      if len(request.form['confirm_password']) < 1:
           flash("confirm password", 'category5')
      else:
           cPassword = request.form['confirm_password']

      return render_template("process.html")
app.run(debug=True)
