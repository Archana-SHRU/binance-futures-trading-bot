# Simplified Trading Bot (Binance Futures Testnet - USDT-M)

## 1. Problem Statement

Manual crypto trading on futures markets can be repetitive and error-prone.
Developers and traders often need a lightweight system to:

- Programmatically place BUY/SELL orders
- Support different order types (Market, Limit)
- Validate trading inputs
- Log order activity
- Handle errors gracefully

Additionally, accessing Binance Futures Testnet may be restricted in some regions,
making development and testing challenging.

This project addresses these challenges by providing a modular,
CLI-based trading bot with structured logging and mock execution support.

---

## 2. Proposed Solution

This project implements a structured Python-based trading bot that:

- Accepts user input via CLI
- Supports MARKET and LIMIT orders
- Supports both BUY and SELL sides
- Validates symbol, quantity, and price
- Logs all order requests and responses
- Handles invalid input and runtime errors
- Provides mock execution mode for restricted environments

The architecture separates:
- Client/API Layer
- Order Logic
- Input Validation
- Logging Configuration
- CLI Interface

This makes the project clean, reusable, and production-ready.

---

## 3. Who Can Benefit From This?

This system can benefit:

- Beginner algorithmic traders
- Developers learning API integrations
- Students learning clean project architecture
- Engineers building automated trading tools
- Anyone testing futures strategies safely using test environments

---

## 4. Key Features

✔ Modular project structure  
✔ CLI-based user interaction  
✔ Market & Limit order support  
✔ BUY / SELL side support  
✔ Input validation  
✔ Structured logging  
✔ Error handling  
✔ Mock execution mode  
✔ Real API-ready design  

---

## 5. Project Architecture

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── logging_config.py
│   ├── mock_responses.py
│   ├── orders.py
│   ├── validators.py
│
├── logs/
│
├── cli.py
├── README.md
├── requirements.txt

---

## 6. Setup Instructions

1. Clone the repository
2. Create virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

---

## 7. How to Run

python cli.py

Follow the CLI prompts.

Example:
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.01

---

## 8. Logging

All API requests and responses are logged inside:

logs/trading.log

The log file contains:
- Order request details
- Order response details
- Error messages (if any)

---

## 9. Mock Mode Explanation

Due to regional identity verification enforcement on Binance Futures Testnet,
this project runs in mock execution mode.

The client layer is fully compatible with Binance Futures API
and can be activated by adding valid API credentials in client.py.

---

## 10. Assumptions

- USDT-M futures pairs are used
- Symbols must end with USDT
- Quantity and price must be positive values

---

## 11. Future Improvements

- Real Binance API integration toggle
- Stop-Limit order support
- OCO support
- Strategy-based automation
- Web UI integration
- Risk management module

---

## Author

Developed as part of Python Developer Internship Assignment.
