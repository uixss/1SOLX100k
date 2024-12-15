# 🔍 Identificación de Tokens Sospechosos o Rug-Pulls

Esta guía describe cómo detectar **tokens sospechosos** o **rug-pulls** (proyectos diseñados para estafar) analizando varios aspectos clave del contrato, el mercado y las actividades on-chain.


<img src="../img/id.jpg" alt="ig" style="display: block; margin: 0 auto;">

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

