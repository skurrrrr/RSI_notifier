import requests

# Set the query parameters
params = {
    'pair': 'XBTUSD',
    'since': 1616663618,
    'count': 2
}

resp = requests.get('https://api.kraken.com/0/public/Trades', params=params)

print(resp.json())

