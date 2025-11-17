def creat_item(name: str, qty: int, price: float) -> dict:
    new_item = {"name": name, "qty": qty, "price": price}
    return new_item


def calc_total(items: list[dict]) -> float:
    total = sum(list(map(lambda x: x["qty"] * x["price"], items)))
    return total


def format_invoice(customer: str, items: list[dict]):
    print(f"Customer: {customer}")
    print("-----------------------")

    print(f"{'Product':<10} {'Qty': <5} {'Price': <5} {'Subtotal':<5}")
    for item in items:
        print(f"{item["name"]:<10} {item["qty"]: <5} {item["price"]:<5} {item["qty"] * item["price"]:<5}")
    print("-----------------------")
    print(f"TOTAL: {calc_total(items)}")


items = [
    {"name": "Pen", "qty": 2, "price": 5.0},
    {"name": "Notebook", "qty": 1, "price": 15.0}
]

total = calc_total(items)
print(total)

format_invoice("Nguyen Van A", items)
