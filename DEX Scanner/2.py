import requests

response = requests.get("https://api.dexscreener.com/token-boosts/latest/v1")
data = response.json()
print(data)
