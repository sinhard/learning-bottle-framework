#bottle rest api
from bottle import run, get, route, post

provinces = [
    {'id' : '1', 'province_name' : 'Western Area'}, 
    {'id' : '2', 'province_name' : 'Southern Province'}, 
    {'id' : '3', 'province_name' : 'Northern Province'}, 
    {'id' : '4', 'province_name' : 'Eastern Province'}, 
]

cities = [
    {'uid' : '1', 'city_name' : 'Freetown', 'province' : 'Western Area'}, 
    {'uid' : '2', 'city_name' : 'Bo', 'province' : 'Southern Province'}, 
    {'uid' : '3', 'city_name' : 'Makeni', 'province' : 'Northern Province'}, 
    {'uid' : '4', 'city_name' : 'Kenema', 'province' : 'Eastern Province'}, 
]

@get('/provinces')
def getAll():
    return {'provinces' : provinces}

@get('/cities')
def getAll():
    return {'cities' : cities}

@get('/province/<uid>')
def getOne(uid):
    get_uid = [province for province in provinces if province['uid'] == uid]
    return {'province' : get_uid[0]}

@get('/province/<province_name>')
def getOne(province_name):
    get_province = [province for province in provinces if province['province_name'] == province_name]
    return {'province' : get_province[0]}

@post('/city')
def addOne():
    new_city = {'city_name' : request.json.get('city_name'), 'city' : request.json.get('city')}
    cities.append(new_city)
    return {'cities' : cities}

@get('/city/<city_name>')
def getOne(city_name):
    get_city = [city for city in cities if city['city_name'] == city_name]
    return {'city' : get_city[0]}

run(port=5000, host='localhost', debug=True, reloader=True)