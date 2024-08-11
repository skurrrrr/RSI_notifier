import requests

webhook_url = 'https://discord.com/api/webhooks/1272102141690904586/4vqKTtmOVps4MfOEeGXidL4WcrrDYnaGMd9CPeQVblulzrAE9Go4r-qfCeqleQgYb_Xp'

data = {
    "username": "notify test",
    "content": "Hello, World!"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(webhook_url, json=data, headers=headers)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Error: {response.text}")