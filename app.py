from flask import Flask, render_template, request, redirect
import requests
from simplejson import loads
from pandas import DataFrame, to_datetime
from bokeh.embed import components 
from bokeh.models import ColumnDataSource, FactorRange, Title
from bokeh.plotting import figure
from bokeh.palettes import Spectral11

app = Flask(__name__)
app.Stock = 'GOOG'
app.Type = 'Open'

#@app.route('/',methods=['GET','POST'])
#def index():
#  if request.method == 'GET':
#    return render_template('index.html')
#  else:
#    app.Stock = request.form['Stock']
#    app.Type = request.form['Select']
#    return redirect('/graph')

#@app.route('/graph')
@app.route('/')
def graph():
  api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' %app.Stock
  session = requests.Session()
  session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
  raw_data = session.get(api_url)
  R=loads(raw_data.content)
#  DATA=DataFrame(R['data'],columns=R['column_names'])  
  return render_template('graph.html',stock='%s'%R['data'][0][0])


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
