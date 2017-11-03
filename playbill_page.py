
from bs4 import BeautifulSoup

import requests, json

url = "http://ensemble.nypl.org/transcriptions/514a27240f7ca6258700014e"

playbills = requests.get(url)

if playbills.status_code != 200:
	print ("There was an error with", url)

page_html = playbills.text

soup = BeautifulSoup(page_html, "html.parser")

all_data = []

all_item_divs = soup.find("ul", attrs = {"class": "playbill-annotations"})

for a_div in all_item_divs:
    heading = a_div.find("div")
    #print(heading)
    print(heading['entity-name'])

#	this_data = { 'link_text':link_text.text, 'url':playbill_link['href'] }
#	all_data.append(this_data)

#json.dump(all_data,open('ensemble.json','w'),indent=4)
