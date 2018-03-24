from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.Stock = GOOG
app.Type = Open

@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    app.Stock = request.form['Ticker']
    app.Type = request.form['Type']
    f = open('answers.txt')
    f.write('Stock: %s\n',%app.Stock)
    f.write('Type: %s\n',%app.Type)
    f.close()
    return redirect('/graph')

@app.route('/graph')
def graph():
  return render_template('about.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
