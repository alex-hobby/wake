from flask import Flask

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/test')
def do_something():
    print('hello')

@app.route('/')
def index():
    return app.send_static_file('index.html')