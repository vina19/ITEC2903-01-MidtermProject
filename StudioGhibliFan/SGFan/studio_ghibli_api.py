import requests

url = 'https://ghibliapi.herokuapp.com/films'

def get_title(title):
	titles = requests.get(url, {'title' : title}).json()
	return titles['data']