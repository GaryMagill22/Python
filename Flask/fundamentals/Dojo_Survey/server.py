# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# Create a new instance of the Flask class called "app"
app.secret_key = "keep it secret"


# Home page (First route that gets visited)

@app.route('/')
def home():
    # Rendering HTML files and displaying it
    return render_template('index.html')

# We get here when user hits submit and form gets packaged and passed along.


@app.route('/process', methods=['POST'])
def process():
    # request.form ---> used for getting values inputed in the form
    # session['INSERT KEY HERE'] ---> use this to create a copy and keep track of data
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')
# redirects you to specified url


@app.route('/result')
def result():
    # Hard-coding a location to be sent to the front-end
    name = ['name']
    location = ['location']
    language = ['language']
    comment = ['comment']

    # data location is assigned to the variable "loc" and this is what we'll refer to in the front end.
    return render_template('result.html', loc=location, language=language, comment=comment)
#  renders html file and displays


# This route handles the logging out by clearing everything thats saved in session.

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    # Run the app in debug mode.
    app.run(debug=True, host="localhost", port=8000)
