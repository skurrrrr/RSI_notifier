import requests

resp = requests.get('https://api.kraken.com/0/public/AssetPairs?pair=XXBTZUSD')

print(resp.json())
