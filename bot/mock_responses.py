import random
import uuid
from datetime import datetime

def generate_mock_order(symbol, side, order_type, quantity, price=None):
    order_id = random.randint(100000, 999999)

    avg_price = price if price else round(random.uniform(20000, 70000), 2)

    response = {
        "symbol": symbol,
        "orderId": order_id,
        "clientOrderId": str(uuid.uuid4()),
        "side": side,
        "type": order_type,
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": avg_price,
        "transactTime": datetime.now().isoformat()
    }

    return response
