
import bottle
from bottle import route, error
import weather_api_script
app = bottle.app()

# main page
@route('/', method='GET')
def index():
    city = bottle.request.GET.get("my_city")
    if city is None or city == "":
        return bottle.template('index_page')
    return bottle.redirect('/%s' % city)

# page with only one city
@route('/<city_name>')
def weather_page(city_name):
    weather_api = weather_api_script.get_current_weather(city_name)
    if isinstance(weather_api, list):
        my_weather_many_cities = list()
        for city in weather_api:
            my_weather_many_cities.append(city[0])
        return bottle.template(
                             'current_weather_more_cities',
                             many_cities=my_weather_many_cities,
                             )
    else:
        my_weather = [weather_api[0], weather_api[1], weather_api[2], weather_api[3], weather_api[4], weather_api[5],
                      weather_api[6],  weather_api[7],  weather_api[8]]
        return bottle.template(
                            'current_weather',
                            google_map_api_key=weather_api[0],
                            city_name=weather_api[1],
                            latitude=weather_api[2],
                            longitude=my_weather[3],
                            weather_max_temp=my_weather[4],
                            weather_min_temp=my_weather[5],
                            weather_wind=my_weather[6],
                            humidity=my_weather[7],
                            country_iso_code=weather_api[8],
                            )

# page with more than one city
@route('/selected')
def selected_city():
    city_id = bottle.request.GET.get("id")
    city_name_city_id = weather_api_script.get_city_name_and_id_from_many_cities(city_id)
    testing_variable = weather_api_script.get_current_weather_by_id(city_name_city_id[0], city_name_city_id[1])
    return bottle.template('current_weather',
                           google_map_api_key=testing_variable[0][1],
                           city_name=testing_variable[0][2],
                           latitude=testing_variable[0][3],
                           longitude=testing_variable[0][4],
                           weather_max_temp=testing_variable[0][5],
                           weather_min_temp=testing_variable[0][6],
                           weather_wind=testing_variable[0][7],
                           humidity=testing_variable[0][8],
                           country_iso_code=testing_variable[0][9],
                           )

# page error
@error(404)
@error(500)
def error500(error):
    return bottle.template('error_page')

if __name__ == '__main__':
    bottle.run(app=app, host='localhost', port=8080, debug=True)
