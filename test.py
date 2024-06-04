from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api')
def api():

    return 'api页面'
@app.route('/api/test1')
def test1():
    return "test1"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
