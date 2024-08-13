import requests

# Make GET request
resp = requests.get('https://api.kraken.com/0/public/AssetPairs?pair=XXBTZUSD')

# Check if response was successful
if resp.status_code != 200:
    print("Failed to retrieve data:", resp.text)
else:
    # Parse JSON response
    data = resp.json()

    # Extract the current cost of Bitcoin in US Dollars
    try:
        price = float(data['result']['XXBTZUSD']['pair_24h_hl'][-1]['price'])
    except (KeyError, IndexError):
        print("Failed to retrieve price")
    else:
        print("The current cost of Bitcoin in US Dollars is:", price)