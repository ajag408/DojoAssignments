from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def create_user():
   print "Submitted Info"
   # we'll talk about the following two lines after we learn a little more
   # about form
   if len(request.form['name']) < 1:
       nameOff = True
       flash("name cannot be empty!", 'category1')
    #    return redirect('/')
   else:
       nameOff = False
       Name = request.form['name']
       Location = request.form['location']
       Language = request.form['language']

   if len(request.form['comment'])<1:
       commentOff = True
       flash("comment box cannot be empty!", 'category2')
   elif len(request.form['comment'])>120:
       commentOff = True
       flash("comment should not be longer than 120 characters", 'category2')
   else:
       commentOff = False
       Comment = request.form['comment']

   if nameOff or commentOff:
       return redirect('/')
   else:
       return render_template("result.html", name = Name, location = Location, language = Language, comment = Comment )

app.run(debug=True) # run our server
