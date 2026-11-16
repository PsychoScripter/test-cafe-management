from order import create_order, orders
from cashier import calculate_total_sales


def test_total_sales_sums_all_orders():
    orders.clear()
    create_order("a", "tea", 1)
    create_order("b", "coffee", 1)
    assert calculate_total_sales() == 130