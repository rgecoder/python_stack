from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def success():
  return render_template("index.html", times = 8)

@app.route('/<x>/<y>')
def checkerboard(x,y):
  return render_template("index2.html", x=int(x), y=int(y))







if __name__ =="__main__":
  app.run(debug=True)