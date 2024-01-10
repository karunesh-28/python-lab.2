# Write a Python program to create a class representing a shopping cart. Include
# methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity):
        if item in self.items:
            if quantity >= self.items[item]['quantity']:
                del self.items[item]
            else:
                self.items[item]['quantity'] -= quantity

    def calculate_total(self):
        total = sum(item_data['price'] * item_data['quantity'] for item_data in self.items.values())
        return total

# Example usage:
cart = ShoppingCart()

while True:
    print("\nShopping Cart Operations:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item name: ")
        price = float(input("Enter the price per item: "))
        quantity = int(input("Enter the quantity: "))
        cart.add_item(item, price, quantity)
        print(f"{quantity} {item}(s) added to the cart.")
    elif choice == '2':
        item = input("Enter the item name to remove: ")
        quantity = int(input("Enter the quantity to remove: "))
        cart.remove_item(item, quantity)
        print(f"{quantity} {item}(s) removed from the cart.")
    elif choice == '3':
        print("Current Cart:")
        for item, item_data in cart.items.items():
            print(f"{item}: {item_data['quantity']} x ${item_data['price']} each")
    elif choice == '4':
        total = cart.calculate_total()
        print(f"Total Price: ${total}")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
