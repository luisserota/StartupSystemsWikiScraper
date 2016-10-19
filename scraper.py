from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

# print(r.text)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.table)

table = soup.table.find_all("tr")

count = 0
temp_count = 0

CB = ""
AreaKm = ""
PopC = ""
PopKm = ""
Neighborhoods = ""
for i in table:
	if temp_count < 12:
		temp_count = temp_count + 1
		continue
	if count == 1:
		CB = i.get_text()
	if count == 2:
		AreaKm = i.get_text()
	if count == 3:
		PopC = i.get_text()
	if count == 4:
		PopKm = i.get_text()
	if count == 5:
		Neighborhoods = i.get_text()

	if count == 6:
		insert

	if count == 7:
		count = 0

	if count != 7:
		count = count + 1
	else:
		count = 0
