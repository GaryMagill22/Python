

from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello world!'  # Return the string 'Hello World!' as a response


@app.route('/Contact')
def contact():
    return 'Hello!'


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    # Run the app in debug mode.
    app.run(debug=True, host="localhost", port=8000)
