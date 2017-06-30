from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
# ".+@.+"
@app.route('/')
def index():
 return render_template('index.html')

app.run(debug=True)
