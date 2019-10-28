from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # add some validations!
    if len(request.form['name']) < 1:
        # display validation errors
        # just pass a string to the flash function
        flash("Name cannot be empty!")
    else:
        # display success message
        # just pass a string to flash function
        flash(f"success! Your name is {request.form['name']}.")

    # either way the app should return to index and display the message
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
