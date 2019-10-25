from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def success():
  return ('success')

@app.route('/play')
def playground1():
  return render_template("index.html", phrase="Welcome!", times=3)

@app.route('/play/<times>')
def playground2(times):
  return render_template("index.html", phrase="Welcome!", times =int(times))

@app.route('/play/<times>/<color>')
def playground3(times,color):
  return render_template("index.html", phrase="Welcome!", times= int(times), color=color)




if __name__ == "__main__":
  app.run(debug=True)