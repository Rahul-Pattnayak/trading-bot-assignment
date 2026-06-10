import logging
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(
    API_KEY,
    API_SECRET,
    testnet=True
)


def place_market_order(symbol, side, quantity):

    try:

        logging.info(
            f"Market Order Request | "
            f"Symbol={symbol} "
            f"Side={side} "
            f"Quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(
            f"Market Order Response | "
            f"OrderId={response.get('orderId')} "
            f"Status={response.get('status')} "
            f"ExecutedQty={response.get('executedQty')}"
        )

        return response

    except Exception as e:

        logging.error(
            f"Market Order Failed | "
            f"Symbol={symbol} "
            f"Side={side} "
            f"Quantity={quantity} "
            f"Error={e}"
        )

        raise


def place_limit_order(
    symbol,
    side,
    quantity,
    price
):

    try:

        logging.info(
            f"Limit Order Request | "
            f"Symbol={symbol} "
            f"Side={side} "
            f"Quantity={quantity} "
            f"Price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(
            f"Limit Order Response | "
            f"OrderId={response.get('orderId')} "
            f"Status={response.get('status')} "
            f"ExecutedQty={response.get('executedQty')}"
        )

        return response

    except Exception as e:

        logging.error(
            f"Limit Order Failed | "
            f"Symbol={symbol} "
            f"Side={side} "
            f"Quantity={quantity} "
            f"Price={price} "
            f"Error={e}"
        )

        raise