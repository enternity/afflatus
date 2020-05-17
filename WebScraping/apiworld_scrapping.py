#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

response = requests.get("https://apiworld.co/awards/api-300-top-industry-innovations/?ref=hackernoon.com").text

soup = BeautifulSoup(response,'html.parser')

apis = soup.find_all("tr")
is_success = True
if apis is None:
    is_success = False
info = {'CompanyName':[],'APIName':[], 'TechnologyCategory':[]}
for api in apis:
    try:
        td_tags = api.find_all("td")
    except:
        api = None
    try:
        info['CompanyName'].append(td_tags[0].text.replace("\n",""))
    except:
        info['CompanyName'].append("None")
    try:
        info['APIName'].append(td_tags[1].text.replace("\n",""))
    except:
        info['APIName'].append("None")
    try:
        info['TechnologyCategory'].append(td_tags[2].text.replace("\n",""))
    except:
        info['TechnologyCategory'].append("None")            

# write to json_file
with open("api_info.json", 'w') as json_file:
    json.dump(info,json_file)

print(f"Crawl data.....{is_success}")
