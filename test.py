from flask import Blueprint, Flask

app = Flask(__name__)
blog = Blueprint('blog', __name__)


# as a decorator
@blog.errorhandler(404)
def internal_server_error(e):
    return "render_template('500.html')", 404


@app.route('/')
def index():
    return "this is a index page"


# or with register_error_handler
app.register_error_handler(404, internal_server_error)

app.register_blueprint(blog)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
