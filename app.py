from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! 1304 남가연"

@app.route('/about')
def about():
    return "about World!"

if __name__ == '__main__':
    app.run()
