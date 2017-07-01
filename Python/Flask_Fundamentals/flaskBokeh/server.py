from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
# ".+@.+"
@app.route('/')
def index():
 return render_template('index.html')

@app.route('/success', methods=['POST'])
def plot():
    plot = figure()
    plot.circle([1,2], [3,4])

    html = file_html(plot, CDN, 'my plot')

    return render_template('success.html', html=html)


app.run(debug=True)
