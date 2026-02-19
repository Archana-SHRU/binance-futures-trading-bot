from bot.mock_responses import generate_mock_order
from bot.logging_config import setup_logger
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

logger = setup_logger()


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # Validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            validate_price(price)

        logger.info(f"Order Request → {symbol}, {side}, {order_type}, {quantity}, {price}")

        # MOCK MODE EXECUTION
        response = generate_mock_order(symbol, side, order_type, quantity, price)

        logger.info(f"Order Response → {response}")

        return response

    except Exception as e:
        logger.error(f"Order Failed → {str(e)}")
        raise
