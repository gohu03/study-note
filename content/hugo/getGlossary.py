import requests
from bs4 import BeautifulSoup
import json

url = 'https://gohugo.io/getting-started/glossary/'

res = requests.get(url)
keys = []
values = []

if res.status_code == 200:
  html = res.text
  soup = BeautifulSoup(html, 'html.parser')
  GlossaryWrapper = soup.find(id='prose')
  for key in GlossaryWrapper.find_all('h6'):
    keys.append(key.text.strip())
    value = key.find_next_sibling()
    for link in value.find_all('a'):
      href = link.get('href')
      if href and href.startswith('/'):
        link['href'] = 'https://gohugo.io' + href
    values.append(value.decode_contents())

obj = dict(zip(keys, values))
with open("./glossary.json", 'w') as f:
  json.dump(obj, f, indent=4)
