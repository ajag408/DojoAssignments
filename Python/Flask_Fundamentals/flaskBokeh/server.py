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
    idxChk = None
    for char in xVals:
        print '***char****'
        print char
        if idxChk and xVals.index(char) < idxChk:
            print 'continued'
            continue
        else:
            if char.isdigit():
                doubleDigit = char
                # if xVals.index(char) < len(xVals) - 1:
                runner = xVals.index(char) + 1
                while runner < len(xVals):
                    if xVals[runner].isdigit():
                        doubleDigit = doubleDigit + xVals[runner]
                        runner = runner + 1
                        idxChk = runner
                    else:
                        break

                print doubleDigit
        # elif char == ',':
        #     print char
    # x = [1, 2, 3, 4, 5]
    # y = [6, 7, 2, 4, 5]
    # output_file("success.html")
    # p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    #
    # p.line(x, y, line_width=2)
    #
    # show(p)

    return redirect('/')


app.run(debug=True)
