import krakenex

# Set up your API key
api_key = "FXR3huYN1av44xx5hOB9r0NuuFSztK7KwDk4XOg/BVToH8Yy0Xly+mNw"
api_secret = "OCdTGRlHuWJ1kPaBw1+ApL99Hb3N1o6CTviqEjtL/gNnTs8UGbT7ydYiwkppLB3BVgepyaxkLVo0xY3LYOG0Bw=="

# Create a new Kraken client instance
client = krakenex.Client(api_key=api_key, api_secret=api_secret)

# Set up the symbol for Bitcoin/USDT
symbol = 'XBTUSD'

# Fetch the current price of BTC in USD
response = client.query_public('Ticker', {'pair': symbol})

# Parse the response data
data = response['result'][symbol]

# Get the current price from the response data
current_price = float(data['a'])