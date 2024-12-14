import requests

chain_id = "solana"
pair_id = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"

response = requests.get(f"https://api.dexscreener.com/latest/dex/pairs/{chain_id}/{pair_id}")
data = response.json()
print(data)
