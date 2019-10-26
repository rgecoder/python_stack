import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"


@app.route('/')
def index():
    if 'randNum' not in session:
        session['randNum'] = random.randrange(0, 101)
    if 'message' not in session:
        session['message'] = ""
    if 'button' not in session:
        session['button'] = "Submit"
    print(session['randNum'])

    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['number']) > session['randNum']:
        session['message'] = "too high"
    elif int(request.form['number']) == session['randNum']:
        session['message'] = str(session['randNum']) + " was the number!"
        session['button'] = "Play again"

    else:
        session['message'] = "too low"

    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    # session.pop('randNum')
    # session.pop('message')
    session.clear()
    return redirect('/')
    #or session.clear()


if __name__ == "__main__":
    app.run(debug=True)
