# Binance Futures Testnet Trading Bot

A simple Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet.

Features:

- MARKET Orders
- LIMIT Orders
- BUY and SELL support
- CLI Input using argparse
- Input Validation
- Logging
- Error Handling

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd TradingBot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

## Place Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Place Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Example Validation Error

```bash
python cli.py --symbol BTCUSDT --side ABC --type MARKET --quantity 0.001
```

Output:

```text
FAILED TO PLACE ORDER
Reason: Side must be BUY or SELL
```

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading.log
```

## Project Structure

TradingBot/

├── bot/
│   ├── client.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env


## Dependencies

Main libraries used:

- python-binance
- python-dotenv
- requests

All dependencies are listed in requirements.txt.


## Project Description

> Note: This project uses Binance Futures Testnet and does not place real-money trades.


## Sample Logs

Example MARKET and LIMIT order logs are available in the sample_logs folder.


## Assumptions

- User has Binance Futures Testnet account.
- API keys are valid.
- Internet connection is available.
- Quantity and price must follow Binance Futures rules.