import requests
import re

url = 'https://wanshanziwo.eu.org/'
response = requests.get(url)
html=response.text
lines = html.split('\n')
search_str = 'https://wanshanziwo.eu.org/airport/'

for line in lines:
    if search_str in line:
        tags = re.findall(r'<.*?>',line)
        for tag in tags:
            line = line.replace(tag, '')

        url2 = line.strip()

        resp = requests.get(url2)
       
        print(resp.text)
        break
