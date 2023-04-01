import requests

url = 'https://marsh-flavor-e1c.notion.site/Modern-Concurrency-4d7aa5ae54994b3989119a5d4bdea87a'

response = requests.get(url)

print(response.content)
