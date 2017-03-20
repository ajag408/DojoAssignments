from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
   # about forms
   Name = request.form['name']
   Location = request.form['location']
   Language = request.form['language']
   Comment = request.form['comment']
   return render_template("result.html", name = Name, location = Location, language = Language, comment = Comment )

   return redirect('/')
app.run(debug=True) # run our server
