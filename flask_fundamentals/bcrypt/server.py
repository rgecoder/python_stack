from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/createUser', methods=['POST'])
def create():
  pw_hash = bcrypt.generate_password_hash(request.form['password'])
  print(pw_hash)

  mysql = connectToMySQL('mydb')
  query = 'INSERT INTO users (username, password) VALUES (%(username)s, %(password_hash)s);'
  # put the pw_hash in our data dictionary, NOT the password the user provided
  data = {"username":request.form['username'],
          "password_hash": pw_hash}

mysql.query_db(query,data)
return redirect("/")

@app.route('login', methods=['POST'])
def login():
  #see if username provided exists in the database
  mysql = connectToMySQL("mydb")
  query = "SELECT * FROM users WHERE username = %(username)s;"
  data = {"username": request.form["username"]}
  result = mysql.query_db(query,data)
  if result:
    # assuming we only have one user with this username, the user would be first in the list we get back
    #of course, we should have some logic to prevent duplicates of usernames when we create users
    #use bcrypt's check_password_hash method, passthign the hash from our db and the password from the form
    if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
      #if we get True after checking the pw, we may put the user id in session
      session['userid'] = result[0]['id']
      #never render on a post, always redirect
      return redirect('/success')
    #if we didn't find anything in the db by searching the username or if the pw don't match
    #flash an error msg and redirect back to the safe route
    flash("You could not be logged in")
    return redirect('/')