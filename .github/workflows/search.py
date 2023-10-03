import requests

url = 'https://wanshanziwo.eu.org/'
response = requests.get(url) 
html = response.text

lines = html.split('\n')
print(lines)
search_str = 'https://wanshanziwo.eu.org/airport/'

for line in lines:
    if search_str in line:
        print(line)
        break
