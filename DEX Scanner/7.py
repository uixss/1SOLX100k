import requests

token_addresses = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"

response = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{token_addresses}")
data = response.json()
print(data)
