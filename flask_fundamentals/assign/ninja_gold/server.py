from flask import Flask, redirect, request, render_template, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
  return render_template('index.html')



if __name__ == "__main__":
  app.run(debug = True)