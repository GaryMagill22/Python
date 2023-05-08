
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('index.html')


@app.route('/play/<int:num>')
def play(num):
    # times is variable using in for loop to create (x) boxes.
    return render_template('play.html', num=num)


@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template('color.html', num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
