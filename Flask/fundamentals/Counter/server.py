from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "keep it secret"


@app.route('/')
def home():
    if 'counter' in session:
        print('key exists!')
        session['counter'] += 1
    else:
        print("key 'counter' does NOT exist")
        session['counter'] = 1

    return render_template('index.html')

# post route


@app.route('/increase', methods=['POST'])
def increase():

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    # Run the app in debug mode.
    app.run(debug=True, host="localhost", port=8000)
