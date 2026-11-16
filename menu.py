MENU = {
    "coffee": 80,
    "latte": 120,
    "tea": 50,
    "cake": 90
}


def show_menu():
    print("\n--- CAFE MENU ---")

    for item, price in MENU.items():
        print(f"{item}: {price} Toman")


def get_price(item):
    return MENU.get(item)