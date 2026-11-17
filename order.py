from menu import MENU, get_price


orders = []


def create_order(customer_name, item, quantity):

    price = get_price(item)

    if price is None:
        print("Item not found!")
        return
    
    try:
        quantity = int(quantity)
        
        if quantity <= 0:
                print("quantity not valid!")
                return
            
        total = price * quantity
        
    except ValueError :
        print ("error TypeError")
        return
        
    except TypeError:
        print("Quantity must be a number!")
        return
        
    order = {
        "customer": customer_name,
        "item": item,
        "quantity": quantity,
        "total": total,
        "status": "pending"
    }

    orders.append(order)

    print("Order registered successfully!")


def get_orders():
    return orders


def cancel_order(index):

    if index < 0 or index > len(orders):
        print("Invalid order number!")
        return

    orders.pop(index)
    print("Order canceled!")