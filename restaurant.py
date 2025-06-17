# Define the menu
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

# Greet the user
print("Welcome to Python Restaurant!")
print("\nMenu:")
for item, price in menu.items():
    print(f" {item.capitalize()}: Rs {price}")

order_total = 0
ordered_items = []

while True:
    item = input("\nEnter the item you want to order: ").lower()

    if item in menu:
        order_total += menu[item]
        ordered_items.append(item.capitalize())
        print(f"'{item.capitalize()}' has been added to your order.")
    else:
        print(f"Sorry, we don't have '{item}'.")

    another = input(
        "Do you want to add another item? (Yes/No): ").strip().lower()
    if another != "yes":
        break

print("\n--- Order Summary ---")
for i in ordered_items:
    print(f"- {i}")
print(f"Total Amount to Pay: Rs {order_total}")
