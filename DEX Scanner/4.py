import requests

chain_id = "solana"
token_address = "A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv"

response = requests.get(f"https://api.dexscreener.com/orders/v1/{chain_id}/{token_address}")
data = response.json()
print(data)
