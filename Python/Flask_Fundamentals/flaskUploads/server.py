import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'KeepItSecretKeepItSafe'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.files
        # check if the post request has the file part
        if 'file' not in request.files:
            session['success'] = 'no'
            return redirect('/result')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            session['success'] = 'no'
            return redirect('/result')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['success'] = 'yes'
            return redirect('/result')
    else:
        return render_template('index.html')

@app.route('/result')
def result():
    if session['success'] == 'yes':
        message = 'Your file has been successfully uploaded.'
    elif session['success'] == 'no':
        message = 'Your file upload failed. Please try again.'
    return render_template('result.html', message=message)


app.run(debug=True)
