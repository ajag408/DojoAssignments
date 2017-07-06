from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'



@app.route('/')
def index():
 return render_template('index.html')

@app.route('/success', methods=['POST'])
def plot():
    # x = []
    # xVals = request.form['xVals']
    # for char in xVals:
    #     if char.isdigit():
    #         x.append(int(char))
    #
    # y = []
    # yVals = request.form['yVals']
    # for char in yVals:
    #     if char.isdigit():
    #         y.append(int(char))
    #     # elif char == ',':
    #     #     print char
    # # x = [1, 2, 3, 4, 5]
    # # y = [6, 7, 2, 4, 5]
    # output_file("success.html")
    # p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    #
    # p.line(x, y, line_width=2)
    #
    # show(p)

    map_options = GMapOptions(lat=int(request.form['lat']), lng=int(request.form['lon']), map_type="roadmap", zoom=11)

    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
    )
    plot.title.text = "Place"

    plot.api_key = "AIzaSyB3cdvDq6ndnv1OiZwYDJBWe270FR-Wg7c"

    # source = ColumnDataSource(
    # data=dict(
    #     lat=[30.29, 30.20, 30.29],
    #     lon=[-97.70, -97.74, -97.78],
    #     )
    # )
    #
    # circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
    # plot.add_glyph(source, circle)

    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    output_file("gmap_plot.html")
    show(plot)

    return redirect('/')


app.run(debug=True)
