from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<flask>')
def say(flask):
    return f'Hi {flask}!'


@app.route('/repeat/<int:num>/<string:hello>')
def str_int(num, hello):
    return f'{hello * num}'


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    # Run the app in debug mode.
    app.run(debug=True, host="localhost", port=8000)
