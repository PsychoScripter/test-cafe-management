from order import get_orders
from cashier import calculate_total_sales, calculate_order_count


def show_orders():

    print("\n--- ORDERS ---")

    for index, order in enumerate(get_orders()):
        print(
            f"{index}. "
            f"{order['customer']} - "
            f"{order['item']} - "
            f"{order['quantity']} - "
            f"{order['total']}"
        )


def show_report():

    print("\n--- SALES REPORT ---")

    print("Total Orders:", calculate_order_count())
    print("Total Sales:", calculate_total_sales())