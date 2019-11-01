from flask import Flask, redirect, render_template, request, flash, session
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretkey"
mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
  if len(request.form['email']) < 1:
    flash('Email cannot be blank!')
  elif not EMAIL_REGEX.match(request.form['email']):
    flash('Email is invalid!')
  else:
    query("INSERT INTO emails (email, created_at, updated_at)" + "VALUES(:email, NOW(), NOW())" )
    data = {
      'email': request.form['email']
    }
    mysql.query_db(query,data)
    session['email'] = request.form['email']
    return redirect('/success')
  return redirect('/')