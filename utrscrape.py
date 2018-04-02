import requests
from bs4 import BeautifulSoup


AKL = 'http://www.undertheradar.co.nz/utr/gigRegion/Auckland'
data = {"regionID": "1", "limit": "20"}

with requests.Session() as s:
    r = s.get(AKL)
    soup = BeautifulSoup(r.content, 'html.parser')

    events = 
    soup.find_all("script", class_"vevent")