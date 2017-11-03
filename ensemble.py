
from bs4 import BeautifulSoup

import requests, json, csv

url = "http://ensemble.nypl.org/programs?page="

playbills = requests.get(url)

if playbills.status_code != 200:
	print ("There was an error with", url)

page_html = playbills.text

soup = BeautifulSoup(page_html, "html.parser")

all_data = []

all_links = soup.find_all('a', string = 'View')

for a_link in all_links:
	print(a_link['href']

# counter = 0
# while counter < 9:
# 	counter = counter + 1
# 	print(url + counter)	
