import argparse
import logging

from bot.logging_config import setup_logging
from bot.client import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    elif args.type == "LIMIT":

        if args.price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )
        validate_price(args.price)
        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\n================================")
    print("ORDER REQUEST SUMMARY")
    print("================================")

    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")

    if args.type == "LIMIT":
        print(f"Price    : {args.price}")

    print("\n================================")
    print("ORDER RESPONSE")
    print("================================")

    print(f"Order ID      : {response['orderId']}")
    print(f"Status        : {response['status']}")
    print(f"Executed Qty  : {response['executedQty']}")

    if "avgPrice" in response:
        print(f"Average Price : {response['avgPrice']}")

    print("\nSUCCESS: Order submitted successfully.")

except Exception as e:

    logging.error(
        f"Failed Order | "
        f"Symbol={args.symbol} "
        f"Side={args.side} "
        f"Type={args.type} "
        f"Quantity={args.quantity} "
        f"Error={e}"
    )

    print("\nFAILED TO PLACE ORDER")
    print(f"Reason: {e}")