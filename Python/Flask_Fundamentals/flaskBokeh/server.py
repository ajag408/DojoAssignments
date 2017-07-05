from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN


app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
# ".+@.+"
@app.route('/')
def index():
 return render_template('index.html')

@app.route('/success', methods=['POST'])
def plot():
    x = []
    xVals = request.form['xVals']
    for char in xVals:
        if char.isdigit():
            x.append(int(char))

    y = []
    yVals = request.form['yVals']
    for char in yVals:
        if char.isdigit():
            y.append(int(char))
        # elif char == ',':
        #     print char
    # x = [1, 2, 3, 4, 5]
    # y = [6, 7, 2, 4, 5]
    output_file("success.html")
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    p.line(x, y, line_width=2)
    
    show(p)

    return redirect('/')


app.run(debug=True)
