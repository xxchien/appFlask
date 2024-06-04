# app.py
from flask import Flask
from views.admin import admin_bp
from views.user import user_bp

app = Flask(__name__)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/')
def index():
    return "this is a index page"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
