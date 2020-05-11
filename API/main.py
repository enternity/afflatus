#!/usr/bin/env python3
import requests
import argparse
import os

class OpenWeather():

    
    def __init__(self, api_key='10531eec7d08826697eaa0211d932abb', latitude=0, longitude=0):
        self.api_key = api_key
        self.latitude = int(latitude)
        self.longitude = int(longitude)
    
    def load_from_url(self):
        print(f"Lat and lon: {self.latitude}, {self.longitude}")

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}'
        print(url)

        respone = requests.get(url)
        
        print(respone.json())

def parse_args():
    parser = argparse.ArgumentParser(description='Du bao thoi tiet')
    parser.add_argument('--lat', required=True)
    parser.add_argument('--lon', required=True)

    opts = parser.parse_args()
    return opts

if __name__ == "__main__":  
    opts = parse_args()
    print(opts.lat)
    print(opts.lon)
    weather = OpenWeather(latitude=opts.lat,longitude=opts.lon)
    
    weather.load_from_url()