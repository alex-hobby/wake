from flask import Flask
app = Flask(__name__)

@app.route('/sleeping/<int:asleep>')
def asleep_check(asleep):
   s = "Asleep!"
   if not asleep:
   	s = "Awake!"
   return s

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = False)