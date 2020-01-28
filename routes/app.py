#routing in bottle
from bottle import run, route

#static routes
@route('/')
def index():
    return '<h1>Routes in Bottle</h1><nav><ul><li><a href="/static/routes">Static Routes</a></li><li><a href="/dynamic/routes">Dynamic Routes</a></li></ul></nav>'

@route('/static/routes')
def static():
    return '<h1>Static Routes</h1><nav><ul><li><a href="/home">Home</a></li><li><a href="/login">Login</a></li></li><li><a href="/">Return</a></li></ul></nav>'

@route('/home')
def home():
    return '<h1>On the home page.</h1><a href="/static/routes">Return</a>'

@route('/login')
def name():
    return '<h1>On the login page.</h1><a href="/static/routes">Return</a>'

#dynamic routes
@route('/dynamic/routes')
def dynamic():
    return '<h1>Please paste either of the following route link into your web browser url bar and see the magic!</h1><br><code>localhost:8080/article/1 <br>localhost:8080/user/replace with your name</code><br><a href="/">Return</a>'

@route('/article/<id>')
def article(id):
    return '<h1>You are the viewing article ' + id + '</h1>'

@route('/user/<name>')
def user(name):
    return '<h1>Your name is ' + name + '</h1>'

#methods 
@route('/posted', method="GET")
def posted():
    return '<h1>Date is being posted</h1>'

#fires server
run(port=8080, host='localhost', reloader=True)