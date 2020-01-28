from bottle import run, route

@route('/')
def index():
    return '<h1>Hello, World!</h1>'

run(port=8080, host='localhost')
