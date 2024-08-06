from markupsafe import escape
from flask import Flask

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)


app = Flask(__name__)
app.register_blueprint(simple_page)
# @app.route("/<name>")
# def hello(name):
#     # return f"Hello, {name}!"
#     return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
