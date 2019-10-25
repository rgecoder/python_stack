from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#index route will handle rendering the form
@app.route('/')
def index():
  return render_template("index.html")

#This route will handle form submission
#Note: define which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
  print("Got Post Info")
  name = request.form['name']
  email = request.form['email']
  print(name)
  print(email)
  #redirects back to the '/' route
  return render_template('success.html')


if __name__ =="__main__":
  #run the server
  app.run(debug=True)