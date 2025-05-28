# Laboratorio 5 - QKD

Un proyecto en Python que simula el protocolo BB84 para distribución cuántica de claves (QKD), demostrando cómo Alice y Bob pueden generar una clave secreta segura incluso ante intentos de espionaje.


## 📌 Descripción
Este código simula:

✅ Generación de bits y bases aleatorias para Alice y Bob.

✅ Transmisión de qubits (fotones polarizados).

✅ Medición de Bob y construcción de la clave secreta.

⚠️ Ataque de Eve, que introduce errores en la comunicación.

📊 Visualización de resultados para entender cómo se forma la clave.


## ⚙️ Requisitos
Python 3.x

Librerías estándar (random)

## 🚀 Instalación y Ejecución

1. Clona o descarga el repositorio.
2. Ejecuta el script

```python
python Lab5.py
```
3. Resultados obtenidos
```python
=== Simulación BB84 ===
Bits de Alice:       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
Bases de Alice:      ['↗', '↕', '↕', '↗', '↕', '↗', '↗', '↗', '↕', '↕', '↕', '↗', '↕', '↕', '↕', '↗', '↗', '↗', '↕', '↗']
Bases de Bob:        ['↕', '↕', '↕', '↕', '↗', '↗', '↗', '↗', '↕', '↗', '↕', '↕', '↕', '↗', '↕', '↕', '↗', '↗', '↕', '↗']
Resultados de Bob:   [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]

--- Clave Secreta ---
Índices coincidentes: [1, 2, 5, 6, 7, 8, 10, 12, 14, 16, 17, 18, 19]
Clave compartida:     [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]
Longitud de la clave: 13 bits

--- Con Eve (ataque) ---
Clave con Eve:       [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1]
Errores introducidos: 3
```

## 🔍 ¿Cómo Funciona?
1. Alice genera bits aleatorios y los codifica en bases (↕ o ↗).
2. Bob mide los qubits con bases aleatorias.
3. Alice y Bob comparan bases y solo conservan los bits donde coinciden (clave secreta).
4. Si Eve espía, introduce errores en la clave, lo que permite detectarla.

5. Ver Infografía [https://github.com/FabianJuarez182/Lab5_QKD/blob/main/infografia_qkd.pdf]

## 🎯 Objetivos del Proyecto
✔️ Entender BB84 de manera práctica.

✔️ Simular seguridad cuántica con lógica clásica.

✔️ Explorar cómo el azar protege información.

✔️ Visualizar el impacto de la criptografía cuántica en el futuro.


## 📁 Estructura del Código
```python
python Lab5.py
README.md  
```

