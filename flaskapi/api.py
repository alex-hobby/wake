from flask import Flask

app = Flask(__name__)

@app.route('/test')
def do_something():
    print('hello')