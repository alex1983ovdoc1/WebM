from flask import current_app
import requests


# for https://openweathermap.org/api/one-call-3 (bondpy20221)
# Погода бот на python -> change city
def weather_by_city(city_name):	
	lat=37.983810
	lon=23.727539
	params1 = {
		'lat': lat,
		'lon': lon,
		'units': 'metric',
		'appid': '05966ac74347d94fb6dcd48d722b66eb'			
	}	
	weather_url = 'https://api.openweathermap.org/data/2.5/weather?'
	try:
		result = requests.get(weather_url, params=params1)
		result.raise_for_status()                 # status answer server (error 4xx, 5xx)
		weather = result.json()
		if "main" in weather:
			if "temp" in weather["main"]:
				try:
					current_condition = {
									'temp_C': round(weather["main"]["temp"], 1),
									'FeelsLikeC': round(weather["main"]["feels_like"], 1)}
					return current_condition
				except(IndexError, TypeError): # (server -> give wrong data)
					return False
	except(requests.RequestException, ValueError): # Network Error (requests-> not Internet, ValueError-> html address wrong)
		print("--/Newwork Error/ (webapp/weather_html.py)--")
		return False
	return False



if __name__=='__main__':
	w = weather_by_city('Kyiv,Ukraine')
	print(w)