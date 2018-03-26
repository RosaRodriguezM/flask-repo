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
app.Type = ['Open']

@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
#  else:
#    app.Stock = request.form['Stock']
#    app.Type = request.form.getlist('selection')
#    return redirect('/graph')

@app.route('/graph',methods=['POST'])
def graph():
  Stock = request.form['Stock']
  lista  = request.form.getlist('selection')
  api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' %(Stock)
  session = requests.Session()
  session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
  raw_data = session.get(api_url)
  R=loads(raw_data.content)
  DATA=DataFrame(R['data'],columns=R['column_names'])
  p=figure()
  p.line([1,2,3],[1,2,3]) 
#  p = figure(title='Data from Quandle WIKI set', x_axis_label='Date', x_axis_type='datetime')
#  lista=app.Type
#  ll=len(lista)
#  for ii in range(ll):
#    p.line(to_datetime(DATA['Date'][0:52*5]),DATA[lista[ii][0:52*5]], color= Spectral11[ii],line_width=1,legend=lista[ii])
#  p.legend.location = "top_left"
  script, div = components(p)
  return render_template('graph.html', Ticker=Stock, script=script, div=div) 


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
