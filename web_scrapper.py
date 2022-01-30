from bs4 import BeautifulSoup
import requests
import re

req = requests.get('http://www.saranathan.ac.in')

soup = BeautifulSoup(req.text, features="lxml")

for link in soup.find_all('a'):
    print(link.get('href'))



