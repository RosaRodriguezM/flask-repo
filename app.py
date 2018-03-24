from flask import Flask, render_template, request, redirect
from simplejson import loads
from pandas import DataFrame, to_datetime
from bokeh.embed import components 
from bokeh.models import ColumnDataSource, FactorRange, Title
from bokeh.plotting import figure
from bokeh.palettes import Spectral11

app = Flask(__name__)
app.Stock = 'GOOG'
app.Type = 'Open'

@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    app.Stock = request.form['Stock']
    app.Type = request.form['Select']
    return redirect('/graph')

@app.route('/graph')
def graph():
  api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' %app.Stock
  return render_template('graph.html',stock=api_url)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
