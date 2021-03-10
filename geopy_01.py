from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent='geoapiExercises')
#print(geolocator.geocode(input('Введите индес: ')))

add_1 = geolocator.geocode(input('Введите первый адрес: '))
add_2 = geolocator.geocode(input('Введите второй адрес: '))
city_1 = (add_1.latitude, add_1.longitude)
city_2 = (add_2.latitude, add_2.longitude)
print(f'Расстояние между {add_1} и {add_2}:')
print(distance.distance(city_1, city_2).km,'км')