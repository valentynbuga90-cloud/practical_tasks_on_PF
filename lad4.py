def format_price(price):
    return f"ціна: {price:.2f} грн"


def check_availability(*items):
    store = {
        "хліб": True,
        "молоко": True,
        "яйця": False,
        "цукор": True,
        "чай": False,
        "кава": True
    }

    return {item: store.get(item.lower(), False) for item in items}


def process_order(order_items):
    prices = {
        "хліб": 25.50,
        "молоко": 32.00,
        "яйця": 60.00,
        "цукор": 28.40,
        "чай": 70.00,
        "кава": 95.00
    }

    availability = check_availability(*order_items)

    if not all(availability.values()):
        print("❌ Замовлення неможливе! Деяких товарів нема в наявності.")
        for item, is_available in availability.items():
            if not is_available:
                print(f" - {item}: Немає в наявності")
        return

    total = sum(prices[item] for item in order_items)

    print("\nВаше замовлення:")
    for item in order_items:
        print(f"{item} — {format_price(prices[item])}")

    print("\nЗагальна сума:", format_price(total))


while True:
    print("\n--- МАГАЗИН ---")
    print("1 — Купити товари")
    print("2 — Переглянути ціну товарів")
    print("3 — Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        order = input("Введіть товари через кому: ").lower().split(",")
        order = [item.strip() for item in order]
        process_order(order)

    elif choice == "2":
        items = input("Введіть товари для перевірки: ").lower().split(",")
        items = [i.strip() for i in items]

        availability = check_availability(*items)
        for item, state in availability.items():
            print(f"{item}: {'є в наявності' if state else 'немає'}")

    elif choice == "3":
        print("До побачення!")
        break

    else:
        print("Невідома команда.")
