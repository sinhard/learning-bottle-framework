#templating in bottle 
from bottle import run, route, template

@route('/')
def index():
    return template('index', name="Mohamed")
@route('/login')
def login():
    return template('login')

run(port=8080, host='localhost', debug=True, reloader=True)