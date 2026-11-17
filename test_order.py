import pytest
from order import create_order, get_orders

# @pytest.mark.parametrize("quantity", [0, -1, -5])
# def test_invalid_quantity(quantity):
#     create_order ("hesam","tea",quantity)
    
#     assert len(get_orders()) == 0
    
@pytest.mark.parametrize("quantity", ["sx", "0"])
def test_invalid_type_quantity(quantity):
    create_order ("hesam","tea",quantity)
    
    assert len(get_orders()) == 0