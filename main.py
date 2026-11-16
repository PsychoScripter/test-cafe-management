from menu import show_menu
from order import create_order, orders
from report import show_orders, show_report


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

            customer = input("Customer name: ").strip()
            if customer == "":
                print("Customer name cannot be empty!")
                continue

            item = input("Item name: ").strip().lower()
            if item == "":
                print("Item name cannot be empty!")
                continue
            try:
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Quantity must be a number")
                continue

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