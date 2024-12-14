# 📊 DexScreener API Integration

## 🔄 Endpoints Implementados

### ✨ Obtener los últimos perfiles de tokens

**Endpoint:** `GET https://api.dexscreener.com/token-profiles/latest/v1`

- **Límite de tasa:** 60 solicitudes por minuto.
- **Respuesta:**
  - URL, chainId, dirección del token, iconos, descripción y enlaces asociados.

```python
import requests
response = requests.get("https://api.dexscreener.com/token-profiles/latest/v1")
data = response.json()
print(data)
```

---

### 🎡 Obtener los últimos tokens "boosted"

**Endpoint:** `GET https://api.dexscreener.com/token-boosts/latest/v1`

- **Límite de tasa:** 60 solicitudes por minuto.
- **Respuesta:**
  - Tokens que recibieron boosts, incluyendo el monto total.

```python
import requests
response = requests.get("https://api.dexscreener.com/token-boosts/latest/v1")
data = response.json()
print(data)
```

---

### 🏆 Obtener los tokens "boosted" más populares

**Endpoint:** `GET https://api.dexscreener.com/token-boosts/top/v1`

- **Límite de tasa:** 60 solicitudes por minuto.
- **Respuesta:**
  - Tokens destacados por popularidad o volumen.

```python
import requests
response = requests.get("https://api.dexscreener.com/token-boosts/top/v1")
data = response.json()
print(data)
```

---

### 🔍 Verificar pedidos asociados a un token

**Endpoint:** `GET https://api.dexscreener.com/orders/v1/{chainId}/{tokenAddress}`

- **Parámetros de ruta:**
  - `chainId`: Ejemplo `solana`.
  - `tokenAddress`: Dirección del token.
- **Límite de tasa:** 60 solicitudes por minuto.
- **Respuesta:**
  - Estado del pedido: `processing`, `approved`, `rejected`, etc.

```python
import requests
chain_id = "solana"
token_address = "A55XjvzRU4KtR3Lrys8PpLZQvPojPqvnv5bJVHMYy3Jv"
response = requests.get(f"https://api.dexscreener.com/orders/v1/{chain_id}/{token_address}")
data = response.json()
print(data)
```

---

### 📊 Obtener pares por dirección de token

**Endpoint:** `GET https://api.dexscreener.com/latest/dex/tokens/{tokenAddresses}`

- **Parámetros de ruta:**
  - `tokenAddresses`: Direcciones de tokens, separadas por comas (hasta 30).
- **Límite de tasa:** 300 solicitudes por minuto.
- **Respuesta:**
  - Lista de pares asociados con el token, precios, liquidez, etc.

```python
import requests
token_addresses = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"
response = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{token_addresses}")
data = response.json()
print(data)
```

---

### 🔍 Buscar pares coincidentes con una consulta

**Endpoint:** `GET https://api.dexscreener.com/latest/dex/search`

- **Parámetros de consulta:**
  - `q`: Texto de búsqueda.
- **Límite de tasa:** 300 solicitudes por minuto.
- **Respuesta:**
  - Lista de pares que coinciden con el texto proporcionado.

---

## 🛠️ Tecnologías Utilizadas

- Python – Para las solicitudes a la API y manejo de datos.
- [Requests](https://pypi.org/project/requests/) – Cliente HTTP para integrar la API de DexScreener.

---

## 📖 Documentación Oficial

Visita la documentación oficial de la API de DexScreener para obtener más detalles: [DexScreener API Docs](https://dexscreener.com/docs)

---
