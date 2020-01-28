#creating custom error pages
from bottle import run, route, error

@error(404)
def error404(error):
    return '<h1>Page not found</h1>'

@error(405)
def error405(error):
    return '<h1>This method is not allowed</h1>'

@error(500)
def error505(error):
    return '<h1>Something went wrong</h1>'

@route('/', method='POST')
def index():
    return '<h1>Index page.</h1>'

@route('/login')
def login():
    return '<h1>Login page.</h1>'

@route('/zero')
def zero():
    return 1 / 0

run(port=8080, host='localhost', debug=True, reloader=True)