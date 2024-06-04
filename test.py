from flask import Flask, url_for, redirect
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the index page'


@app.route('/user/<username>')
def profile(username):
    return redirect(url_for('index'))

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return {
        "username": "344343",
        "theme": "3333"
    }
    else:
        return {
        "username": "33",
        "theme": "33"
    }
@app.post("/me")
def me_api():
    user = "get_current_user()"
    return {
        "username": user,
        "theme": user
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
