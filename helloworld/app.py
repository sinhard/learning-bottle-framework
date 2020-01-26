#hello world app written in bottle.py
from bottle import Bottle, run 

app = Bottle()
@app.route('/hello')
def hello():
    return "Hello World!"

#creates server
run(app, host='localhost', port=5000)