from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
app.secret_key= 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
  print("Got Post Info")
  #notice key used to access info corresponds with the names
  #of the inputs from our html form
  
  # name = request.form['name']
  # email = request.form['email']
  
  #now we add 2 properties to session to store the name and email
  session['name']= request.form['name']
  session['email'] = request.form['email']
  
  return redirect('/show')

@app.route('/show')
def show_user():
  #previous in show_user function did not have access to name and email from
  #form submission, now using session can acess name and email store from 
  #one function to another
  # return render_template('user.html', name=session['name'], email=session['email'])
  return render_template('user.html')

if __name__ == "__main__":
  app.run(debug = True)