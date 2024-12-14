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
