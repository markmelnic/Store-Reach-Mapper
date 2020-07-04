
import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# linella markets link
link = "https://www.linella.md/markets"

page = requests.get(link, headers = headers, timeout=30)
soup = BeautifulSoup(page.content, 'html.parser')

markets = soup.find_all(class_ = 'mlm')

with open("linella_markets.csv", "w", newline = '') as lm_file:
    csv_writer = csv.writer(lm_file)

    for market in markets:
        index = market['data-index']
        lat = market['data-map-lat']
        lng = market['data-map-lng']
        title = market.find(class_ = "mlm-title").text
        address = market.find(class_ = "mlm-address").text
        timetable = market.find(class_ = "mlm-timetable").text
        
        csv_writer.writerow([index, str.encode(title), str.encode(address), timetable, lat, lng])