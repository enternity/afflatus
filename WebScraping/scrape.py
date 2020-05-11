#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://coreyms.com/').text


soup = BeautifulSoup(source, 'lxml')

info = {'link':[], 'summary':[]}


for article in soup.find_all('article'):

    summary = article.find('div', class_='entry-content')
    #print(summary.p.text)
    try:
        vid_src = article.find('iframe', class_='youtube-player')
        vid_id = vid_src['src'].split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"

    except Exception as e:
        yt_link = None
    
    info['link'].append(yt_link)
    info['summary'].append(summary.p.text.replace("In this Python Programming Tutorial, we will be","") \
                                            .replace("In this Python Programming video, we will be learning","") \
                                            .replace("In this video, we will be learning how",""))

with open('info.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(info.keys())
    writer.writerows(zip(*info.values()))


print("Get link.... Success")
#headline = article.a.text
#print(headline)
