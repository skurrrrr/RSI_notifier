import requests
from krakenex import KrakenAPI

# Initialize Kraken API connection
k  = KrakenAPI(api_key="FXR3huYN1av44xx5hOB9r0NuuFSztK7KwDk4XOg/ BVToH8Yy0Xly+mNw", api_secret='OCdTGRlHuWJ1kPaBw1+ApL99Hb3N1o6CTviqEjtL/ gNnTs8UGbT7ydYiwkppLB3BVgepyaxkLVo0xY3LYOG0Bw==')

# Set the URL for the API call
url  = f'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'

# Make GET request to the specified URL
response  = requests.get(url, headers={'Authorization': k.sign_request(f'public/Ticker?pair=XBTUSD')})

if response.status_code == 200:
    # Parse JSON response from API call
    data  = response.json()

    # Extract Bitcoin price from the parsed JSON data
    bitcoin_price  = float(data['result']['xbtusd']['price'])

    print(f'The current price of Bitcoin is: {bitcoin_price} USD')
else:

    print('Failed to retrieve data. Status code:', response.status_code)