# 1SOLX100k

# 📊 Métrica de Evaluación de Tokens

Una métrica personalizada para evaluar la **legitimidad** y **calidad** de tokens en proyectos de criptomonedas. Esta herramienta combina factores clave relacionados con la seguridad, actividad del mercado, y fundamentos del proyecto.

---

## 🔑 **Factores Clave**

### 1️⃣ **Seguridad del Contrato** 🛡️  **Peso:** 40%.
- 🔍 **Fuente del código:** Verifica si el contrato inteligente está **verificado** en exploradores como Etherscan.
- ✅ **Auditorías:** Confirma si el contrato ha sido auditado por empresas confiables (CertiK, PeckShield, etc.).
- ⚠️ **Permisos peligrosos:** Revisa funciones sospechosas como:
  - `mint()`, `disableTrading()`, `setFees()`.
- 🚨 **Honeypots:** Usa herramientas como **Honeypot Checker** para detectar si no puedes vender el token después de comprarlo.

---

### 2️⃣ **Actividad en el Mercado** 📈 **Peso:** 25%.
- 💰 **Volumen de trading:** Tokens con un volumen diario **> $10,000** son más confiables.
- 🔒 **Liquidez bloqueada:** Verifica si la liquidez está bloqueada y el tiempo (usa Unicrypt o Team Finance).
- 📉 **Slippage:** Tokens con slippage mayor al **10%** son sospechosos.

---

### 3️⃣ **Presencia en Redes Sociales** 🌐**Peso:** 15%.
- 📢 **Comunidades activas:** Evalúa cuentas en **Twitter, Telegram o Discord**.
- 🤖 **Engagement real:** Asegúrate de que no están utilizando bots.
- 🛑 **Reclamos de estafa:** Busca menciones negativas en foros como **Reddit** o **Bitcointalk**.

---

### 4️⃣ **Equipo y Transparencia** 👥 **Peso:** 10%.
- 👤 **Equipo público:** Confirma si el equipo es visible y confiable en plataformas como LinkedIn.
- 🗺️ **Roadmap:** Evalúa si el proyecto tiene un roadmap realista.
- 🪙 **Tokenomics:** Analiza cómo se distribuyen los tokens (evita proyectos donde el equipo controla demasiado).

---

### 5️⃣ **Comportamiento On-Chain** 🔗 **Peso:** 10%.
- 🕵️‍♂️ **Movimientos sospechosos:** Usa herramientas como Etherscan para analizar wallets.
- 💼 **Concentración de wallets:** Tokens donde pocas wallets tienen más del **20%** son riesgosos.
- 📜 **Historial de transferencias:** Detecta patrones extraños, como muchas transferencias hacia una wallet específica.

---

## 🧮 **Fórmula para Calcular el Puntaje**

```
peso_seguridad = 0.4
peso_mercado = 0.25
peso_redes_sociales = 0.15
peso_equipo = 0.1
peso_comportamiento = 0.1
    
puntaje_total = (
    seguridad=80,         # Verificación del contrato y auditorías
    mercado=70,           # Volumen y liquidez
    redes_sociales=50,    # Actividad en redes
    equipo=90,            # Transparencia
    comportamiento=60     # Comportamiento on-chain
)

```
---

# 🔍 Identificación de Tokens Sospechosos o Rug-Pulls

Esta guía describe cómo detectar **tokens sospechosos** o **rug-pulls** (proyectos diseñados para estafar) analizando varios aspectos clave del contrato, el mercado y las actividades on-chain.

---

## 🛠️ **Aspectos a Evaluar**

### 1️⃣ **Análisis del Contrato** 🛡️
1. **Verificación del Contrato:**
   - Verifica si el contrato inteligente está **verificado** en Etherscan, BscScan u otros exploradores.
   - Busca contratos con permisos peligrosos como:
     - `mint()` (creación ilimitada de tokens).
     - `disableTrading()` (deshabilita las transacciones).
     - `setFees()` (modifica las tasas de transacción sin aviso).

2. **Auditorías:**
   - Revisa si el contrato ha sido auditado por empresas reconocidas como **CertiK** o **PeckShield**.
   - Los proyectos no auditados son más riesgosos.

3. **Backdoors (puertas traseras):**
   - Usa herramientas como **Token Sniffer** para detectar funciones ocultas que permitan a los desarrolladores retirar fondos.

---

### 2️⃣ **Análisis del Mercado** 📈
1. **Volumen de Trading:**
   - Tokens con un volumen diario inferior a **$10,000** son sospechosos por falta de interés genuino.

2. **Liquidez Bloqueada:**
   - Verifica si la liquidez está bloqueada en plataformas como **Unicrypt** o **Team Finance**.
   - La falta de liquidez bloqueada es una señal clara de rug-pull.

3. **Slippage (Deslizamiento):**
   - Tokens con un slippage mayor al **10%** suelen ser manipulados.

4. **Desbalance en Pares de Liquidez:**
   - Compara el saldo de tokens en el pool de liquidez:
     - Un desequilibrio (como **99% del par en token y 1% en stablecoin**) es sospechoso.

---

### 3️⃣ **Comportamiento On-Chain** 🔗
1. **Concentración de Wallets:**
   - Revisa si pocas wallets controlan más del **20%** de los tokens.
   - Los desarrolladores que poseen grandes cantidades pueden hacer **dumping** (venta masiva).

2. **Transferencias Anómalas:**
   - Analiza el historial de transacciones en **Etherscan** o **BscScan**:
     - Tokens enviados en grandes cantidades a wallets desconocidas pueden indicar fraude.

3. **Actividad de Contrato:**
   - Monitorea contratos para detectar actividades sospechosas:
     - Cambios frecuentes en tasas de transacción.
     - Transferencias hacia wallets no identificadas.

---

### 4️⃣ **Actividad en Redes Sociales** 🌐
1. **Engagement Real:**
   - Usa herramientas como **Social Blade** para evaluar si las cuentas de Twitter/Telegram tienen seguidores reales.
   - Comunidades muy grandes pero inactivas suelen ser bots.

2. **Reclamos de Estafa:**
   - Busca menciones negativas en:
     - **Reddit**.
     - **Bitcointalk**.
     - **Foros de inversores**.

---

## 🛑 **Indicadores Comunes de Rug-Pulls**
- 🚩 **Alta tasa de transacción:** Tokens que cobran un slippage >10% para comprar o vender.
- 🚩 **No puedes vender:** Usa herramientas como **Honeypot Checker** para verificar si puedes vender el token.
- 🚩 **Recompensas irreales:** Promesas de altos rendimientos (APY >1000%) son generalmente insostenibles.
- 🚩 **Lanzamientos rápidos:** Proyectos que se lanzan sin sitio web o documentación confiable.
- 🚩 **Cambios frecuentes en el contrato:** Revisa si el contrato ha sido modificado repetidamente.

---

## 🧮 **Automatización con Herramientas**
1. **Token Sniffer:**  
   Herramienta para analizar contratos, auditorías y actividad de tokens.
   - [https://tokensniffer.com](https://tokensniffer.com)

2. **Honeypot.is:**  
   Detecta si no puedes vender un token.  
   - [https://honeypot.is](https://honeypot.is)

3. **Etherscan/BscScan:**  
   Examina contratos y transacciones on-chain.

4. **DexTools/DexScreener:**  
   Analiza liquidez, volumen y precios de tokens.  
   - [https://www.dextools.io](https://www.dextools.io)  
   - [https://www.dexscreener.com](https://www.dexscreener.com)

---

# 🛠️ Token Analysis Toolkit

Este repositorio contiene herramientas y recursos útiles para analizar tokens, identificar posibles **rug-pulls** y mejorar la eficiencia en la evaluación de proyectos en el espacio de criptomonedas. 🚀

---

## 📌 **Recursos Clave**

### 1. 🔍 **Análisis de Contratos y Tokens**
- [**TokenFomo**](https://tokenfomo.io)  
  Analiza contratos recientes en múltiples cadenas y detecta rug-pulls emergentes.
  
- [**BSC Check**](https://bsccheck.com)  
  Revisión de contratos en Binance Smart Chain. Evalúa riesgos y funciones críticas.
  
- [**RugDoc**](https://rugdoc.io)  
  Especializado en contratos DeFi. Proporciona auditorías rápidas y consejos para evitar rug-pulls.

---

### 2. 📈 **Análisis de Liquidez y Trading**
- [**PooCoin**](https://poocoin.app)  
  Gráficos en tiempo real y movimientos de grandes ballenas en Binance Smart Chain.

- [**UniCrypt**](https://unicrypt.network)  
  Verifica el bloqueo de liquidez en proyectos emergentes.

- [**GeckoTerminal**](https://geckoterminal.com)  
  Datos avanzados de mercado y pares de liquidez para varias cadenas.

---

### 3. 🔗 **Exploración On-Chain**
- [**Etherscan**](https://etherscan.io) / [**BscScan**](https://bscscan.com) / [**PolygonScan**](https://polygonscan.com)  
  Explora contratos inteligentes, transacciones y wallets.

- [**DeBank**](https://debank.com)  
  Centraliza la gestión de activos DeFi y rastrea direcciones sospechosas.

- [**Arkham Intelligence**](https://arkhamintelligence.com)  
  Herramienta avanzada para rastrear entidades y movimientos significativos.

---

### 4. 📊 **Monitorización de Actividad de Ballenas**
- [**Whale Alert**](https://whale-alert.io)  
  Rastreos en tiempo real de grandes movimientos de criptomonedas.

- [**BubbleMaps**](https://bubblemaps.io)  
  Visualización interactiva de distribución de tokens en wallets.

---

### 5. 🚨 **Alertas en Tiempo Real**
- [**DexAlert**](https://dexalert.com)  
  Alertas en tiempo real sobre cambios de precio, volumen y liquidez.

- [**Moonarch**](https://moonarch.app)  
  Alertas personalizadas sobre slippage, volumen y posibles rug-pulls.

---

## 🛡️ **Cómo Identificar Tokens Sospechosos**
1. **Revisión del Contrato**  
   - Verifica si el contrato está auditado o es verificado.  
   - Revisa las funciones críticas como `mint()`, `pause()` o `setTax()`.

2. **Bloqueo de Liquidez**  
   - Confirma que la liquidez esté bloqueada por al menos 6 meses usando herramientas como [UniCrypt](https://unicrypt.network).

3. **Distribución de Tokens**  
   - Usa [BubbleMaps](https://bubblemaps.io) para analizar si un pequeño grupo de wallets tiene la mayor parte de los tokens.

4. **Comportamiento de Precios**  
   - Identifica subidas repentinas (pumps) o caídas drásticas. Herramientas como [DexTools](https://dextools.io) o [PooCoin](https://poocoin.app) son útiles.

5. **Actividad de los Desarrolladores**  
   - Busca actividad en GitHub o redes sociales. Proyectos legítimos suelen tener comunidades activas.

