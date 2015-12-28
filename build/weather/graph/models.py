from django.db import models
# from urllib.request import urlopen
# from urllib.parse import urlencode
# import json
# def weatherGraph(city):
# 	baseurl = "https://query.yahooapis.com/v1/public/yql?"
# 	yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""
# 	yql_query += city +",il\") "
# 	print(yql_query)
# 	yql_url = baseurl + urlencode({'q':yql_query}) + "&format=json"
# 	result = urlopen(yql_url).read().decode('utf-8')
# 	print(result)
# 	data = json.loads(result)
# 	return data
# def showWeather(data):
# 	if (data['query']['count']==1):
# 		print("Country: "+data['query']['results']['channel']['location']['city'])
# 		print("Humidity: "+data['query']['results']['channel']['atmosphere']['humidity'])	

# showWeather(weatherGraph("danang"))
# Create your models here.
