from order import create_order, orders
from cashier import calculate_total_sales


def test_total_is_price_times_quantity():
    orders.clear()
    create_order("darya", "tea", 2)
    assert orders[0]["total"] == 100


def test_quantity_zero_rejected():
    orders.clear()
    create_order("darya", "tea", 0)
    assert len(orders) == 0


def test_customer_empty_rejected():
    orders.clear()
    create_order("", "tea", 1)
    assert len(orders) == 0



def test_item_empty_rejected():
    orders.clear()
    create_order("darya", "", 1)
    assert len(orders) == 0


def test_total_sales_sums_all_orders():
    orders.clear()
    create_order("a", "tea", 1)
    create_order("b", "coffee", 1)
    assert calculate_total_sales() == 130
