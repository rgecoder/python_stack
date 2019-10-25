from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
  
  return render_template("result.html")

@app.route('/danger')
def danger():
  print("a user tried to visit /danger")
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
