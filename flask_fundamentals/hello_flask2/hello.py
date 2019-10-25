from flask import Flask # import flask to allow us to create our app
app = Flask(__name__) # global variable __name__ tells Flask whether or not we are running the file directly or importing as module

print(__name__)
@app.route('/') # @ symbol is a decorator which attaches following function to the '/' route

def success():
  return "success"

@app.route('/hello/<name>')
def hello(name):
  print(name)
  return "hello " + name

@app.route('/users/<username>/<id>')

def show_user_profile(username,id):
  print(username)
  print(id)
  return "username: "+ username + ", id: " +id

def hello_world():
  return 'Hello World!'

if __name__ =="__main__": # if __name__ is "__main__" we know we are runnign this file directly and not importing it from a different module

  app.run(debug=True) # run the app in debug mode