from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greetings():
  return render_template('root.html')

@app.route('/projects')
def project_view():
    return render_template('projects.html')

@app.route('/about')
def about_me():
    return render_template('about.html')

app.run(debug=True)
