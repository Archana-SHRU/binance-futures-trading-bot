import typer
from rich import print
from bot.orders import place_order

app = typer.Typer()


@app.command()
def trade():
    try:
        print("[bold cyan]=== Trading Bot (Mock Mode) ===[/bold cyan]\n")

        symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
        side = input("Enter Side (BUY/SELL): ").upper()
        order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()
        quantity = float(input("Enter Quantity: "))

        price = None
        if order_type == "LIMIT":
            price = float(input("Enter Price: "))

        print("\n[yellow]Placing order...[/yellow]\n")

        response = place_order(symbol, side, order_type, quantity, price)

        print("[green]Order Placed Successfully![/green]\n")

        print("[bold]Order Summary:[/bold]")
        print(f"Symbol: {response['symbol']}")
        print(f"Order ID: {response['orderId']}")
        print(f"Side: {response['side']}")
        print(f"Type: {response['type']}")
        print(f"Status: {response['status']}")
        print(f"Executed Quantity: {response['executedQty']}")
        print(f"Average Price: {response['avgPrice']}")
        print(f"Time: {response['transactTime']}")

    except Exception as e:
        print(f"[red]Error: {str(e)}[/red]")


if __name__ == "__main__":
    app()
