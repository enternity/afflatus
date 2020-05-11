#!/usr/bin/env python3
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=700000,VN&appid=10531eec7d08826697eaa0211d932abb')
json_object = r.text
print(json_object)

