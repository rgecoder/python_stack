from flask import Flask, render_template, request, redirect, session, flash

# re module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9,+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z+$]')
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def submit():
    # if len(request.form['email']) < 1:
    #     flash("Email cannot be blank!")

    # elif not EMAIL_REGEX.match(request.form['email']):
    #   flash("Invalid Email Address!")

    # else:
    #     flash("Success!")

    # return redirect('/')

    #'categorize' flash error message into different label/buckets
    if len(request.form['email']) < 1:
      flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!", "email")
    if len(request.form['name']) < 1:
      flash("Name cannot be blank!", "name")
    elif len(request.form['name']) <=3:
      flash("Name must be 3+ characters", "name")
    
    if len(request.form['comment']) < 1:
      flash("Comment cannot be blank!", "comment")
    elif len(request.form['comment']) > 100:
      flash("Comment must be less than 100 characters", "comment")
    
    if '_flashes' in session.key():
      return redirect("/")

    else:
      return redirect("/success")

#str.isalpha() returns a boolean that shows if string contains only alphabetic characters
# time.strptime(string,format) -- changes a string to a time using the given format

if __name__ == "__main__":
    app.run(debug=True)
