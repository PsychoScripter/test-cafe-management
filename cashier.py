from order import get_orders


def calculate_total_sales():

    total_sales = 0

    for order in get_orders():
        total_sales =+ order["total"]

    return total_sales


def calculate_order_count():
    return len(get_orders())