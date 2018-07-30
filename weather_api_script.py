import os
import pyowm

# api key for openweathermap
owm_api_key = os.environ.get('OWM_API_KEY')
owm = pyowm.OWM(owm_api_key)

# api key google maps
google_api_key = os.environ.get('GOOGLE_API_KEY')
google_map_api_key = google_api_key

# resolving city name - input field can take
# different city names e.g: one word name,
# dashes / spaces separated words or and also mixed types
# function below takes parameter from input field and
# resolve names by passing city name to appropriate function


def resolve_city_name(city_name):
    if " " in city_name:
        return city_name_with_spaces(city_name)
    elif "-" in city_name:
        return city_name_with_dashes(city_name)
    return city_name_one_word(city_name)


def city_name_with_spaces(city_name):
    compound_city_name = list()
    city_name_string = ""
    city_name = city_name.split()
    for part_of_city_name in city_name:
        if part_of_city_name == "-":
            compound_city_name.append("-")
        city_name_string += part_of_city_name[0].upper() + part_of_city_name[1:].lower()
        compound_city_name.append(city_name_string)
        city_name_string = ""
    return compound_city_name


def city_name_with_dashes(city_name):
    city_name_dashes_list = list()
    city_name_word = ""
    for name in city_name:
        if name == "-":
            city_name_word = city_name_word[0].upper() + \
                             city_name_word[1:].lower()
            city_name_dashes_list.append(city_name_word)
            city_name_dashes_list.append(name)
            city_name_word = ""
            name = ""
        city_name_word += name
    city_name_word = city_name_word[0].upper() + city_name_word[1:].lower()
    city_name_dashes_list.append(city_name_word)
    return ''.join(city_name_dashes_list)


def city_name_one_word(city_name):
    city_name = city_name[0].upper() + city_name[1:].lower()
    return city_name


# searching resolved city name,
# return ID of the searched city
def get_city_by_id(city_name):
    city_name = resolve_city_name(city_name)
    if isinstance(city_name, list):
        searched_cities = list()
        with open('cities/city_list.txt', 'r') as get_city_name:
            if len(city_name) == 2:
                for city in get_city_name:
                    city_split = city.split()
                    if city_name[0].lower() == city_split[1].lower() and city_name[1].lower() == city_split[2].lower():
                        searched_cities.append(city_split)
            elif len(city_name) == 3:
                for city in get_city_name:
                    city_split = city.split()
                    if city_name[0].lower() == city_split[1].lower() and city_name[1].lower() == city_split[2].lower() \
                        and city_name[2].lower() == city_split[3].lower():
                        searched_cities.append(city_split)
        return searched_cities
    with open('cities/city_list.txt', 'r') as get_city_name:
        searched_cities = list()
        for city in get_city_name:
            city_split = city.split()
            if city_name.lower() == city_split[1].lower() and len(city_name.lower()) == len(city_split[1].lower()):
                searched_cities.append(city_split)
        return searched_cities


# function determines if there is more than one
# city with the same name. If there is only one
# city, function return city id and country iso code in list,
# if there are many cities, function return id, city name,
# latitude, longitude, and country iso code in list.
def more_cities_with_the_same_name(city_name):
    city_name = get_city_by_id(city_name)
    if len(city_name) == 1:
        return [city_name[0][0], city_name[0][-1], city_name[0][-2], city_name[0][-3]]
    elif len(city_name) > 1:
        id_city_list = list()
        for city in range(len(city_name)):
            id_city_list.append(city_name[city])
        return id_city_list
    return "No city on the list"


# return weather data of searched city
# return formatted name of the city
def get_current_weather(city_name):
    searched_city = more_cities_with_the_same_name(city_name)
    city_name_front = resolve_city_name(city_name)
    if isinstance(city_name_front, list):
        city_name_front = " ".join(city_name_front)
    # owm api for > 1 city starts here
    if isinstance(searched_city[0], list):
        # import function for taking id of the city
        # appending this id to list_of_cities
        ids_from_many_cities = get_city_by_id(city_name)
        list_of_cities = list()
        for city in range(len(searched_city)):
            city_int = searched_city[city][0]
            city_int = city_int.strip()
            # code changed from city_int = int(city_int)
            city_int = int(city_int)
            proxy_list_of_cities = list()
            id_of_city = ids_from_many_cities[city][0]
            city_data = owm.weather_at_id(city_int)
            current_weather = city_data.get_weather()
            # print current_weather
            temp = current_weather.get_temperature('celsius')
            wind = current_weather.get_wind()
            humidity = current_weather.get_humidity()
            city_weather_data = id_of_city, google_map_api_key, city_name_front, searched_city[city][-3], \
                                 searched_city[city][-2], temp['temp_max'],\
                                 temp['temp_min'], wind['speed'], humidity,  searched_city[city][-1],
            proxy_list_of_cities.append(city_weather_data)
            list_of_cities.append(proxy_list_of_cities[:])
            del proxy_list_of_cities
        return list_of_cities
    # owm api for 1 city starts here
    else:
        city_int = searched_city[0]
        city_int = city_int.strip()
        city_int = int(city_int)
        city = owm.weather_at_id(city_int)
        country_iso_code = searched_city[1]
        latitude = searched_city[-1]
        longitude = searched_city[-2]
        current_weather = city.get_weather()
        temp = current_weather.get_temperature('celsius')
        wind = current_weather.get_wind()
        humidity = current_weather.get_humidity()
        return (
                google_map_api_key,
                city_name_front,
                latitude,
                longitude,
                temp['temp_max'],
                temp['temp_min'],
                wind['speed'],
                humidity,
                country_iso_code,
        )


# select from many cities one city
def get_current_weather_by_id(city_name, city_id):
    current_weather = get_current_weather(city_name)
    for cities in current_weather:
        if city_id in cities[0]:
            return cities


def get_city_name_and_id_from_many_cities(city_id):
    city_name_correct_order = ""
    correct_city_name = ""
    number_string_get = len(city_id) - 2
    # print number_string_get
    for element in city_id:
        correct_city_name += city_id[number_string_get]
        number_string_get -= 1
        if city_id[number_string_get] == ",":
            break
    correct_city_name = correct_city_name.strip()
    correct_city_name = correct_city_name[1:-1]
    correct_order_number_string_get = len(correct_city_name) - 1
    for element in correct_city_name:
        city_name_correct_order += correct_city_name[correct_order_number_string_get]
        correct_order_number_string_get -= 1
    city_name = city_name_correct_order
    city_id_string = city_id[1:-1]
    city_id_string = city_id_string.split()
    city_number_id = city_id_string[0][1:-2]
    return [city_name, city_number_id]
