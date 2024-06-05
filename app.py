# app.py
import logging

from flask import Flask

import views.admin
from views.admin import admin_bp
from views.user import user_bp

app = Flask(__name__)


@app.route('/')
def index():
    return "this is a index page"


app.register_blueprint(admin_bp, url_prefix='/test')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print("map" + str(app.url_map))
    app.run(host='0.0.0.0', debug=True)
