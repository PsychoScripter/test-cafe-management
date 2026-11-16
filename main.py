from menu import show_menu
from order import create_order, orders
from report import show_orders, show_report
import menu

def main():

    while True:

        print("\n===== CAFE MANAGEMENT =====")
        print("1. Show Menu")
        print("2. Create Order")
        print("3. Show Orders")
        print("4. Sales Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            try:
                customer = input("Customer name: ")
                item = input("Item name: ")
                if item not in menu.MENU:
                    print('your item not exist')
                    continue
                quantity = int(input("Quantity: "))
            except ValueError:
                print('please enter correct value')

            create_order(customer, item, quantity)

        elif choice == "3":
            show_orders()

        elif choice == "4":
            show_report()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()