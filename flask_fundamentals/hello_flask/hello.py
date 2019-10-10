from flask import Flask
app = Flask(__name__) #__name__ tells flask whether running file direct or importing as a module

print(__name__)

@app.route('/') #@ symbol designates a decorator which attaches function to the '/' route

def hello_world():
  return 'Hello World!' # return hello world as a response

if __name__ ==  "__main__": # if __name__ is "__main__" we know we are running file directly
                          # and not importing from a different module

    app.run(debug=True) #run app in debug mode

