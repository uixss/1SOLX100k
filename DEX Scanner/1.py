import requests

response = requests.get("https://api.dexscreener.com/token-profiles/latest/v1")
data = response.json()
print(data)
