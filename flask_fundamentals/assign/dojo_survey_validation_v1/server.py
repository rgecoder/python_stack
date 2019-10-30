from flask import Flask, render_template, request, redirect, flash, session

app=Flask(__name__)
app.secret_key = "secretkey"
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
  print("Got post info")

  return redirect('/')

@app.route('/result', methods=['POST'])
def result():
  name = request.form['name']
  selected_language = request.form['FavoriteLanguage']
  location = request.form['DojoLocation']
  comment = request.form['Description']
  print(comment)
  if len(request.form['name']) < 1:
    flash('Name can not be empty')
    return redirect('/')
  elif len(request.form['description']) < 1:
    flash('You need to add a comment')
    return redirect('/')
  elif len(request.form['des'])
