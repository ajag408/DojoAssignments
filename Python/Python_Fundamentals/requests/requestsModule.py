import requests

r = requests.get('https://suttacentral.net/data?suttas=dn1,dn2')

# print r.json()
print r.text
