


cafe_name = "Python Café"

print(f"Welcome to {cafe_name}!")


def greet_user(name):
    """Return a greeting message for the user with their name."""
    return f"Welcome to {cafe_name}, {name}!"


user_name = input("Enter name: ")
message = greet_user(user_name)
print(message)

is_reward_user= input("Are you a rewards member?(y/n): ")
if is_reward_user.lower() == "Y": 
    discount = 0.1  # 10% discount
else:
    discount = 0.1

    print(f"what would like to oder today, {user_name}?")
print("Menu")
Menu= {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}
print("Menu:")
for item, price in Menu.items():
    print(f"- {item}: ${price:.2f}")
order = [] 

# --- NEW: Order Collection Loop ---
order = []
print("\nEnter the items you want to order one by one. Type 'done' when you are finished.")

while True:
    selection = input("Add item: ").strip().lower()
    if selection == "done":
        break
    elif selection in Menu:
        order.append(selection)
        print(f"Added {selection} to your order.")
    else:
        print("Sorry, that item is not on the menu. Please try again.")

# --- NEW: Total and Receipt Calculation ---
if order:
    print("\n--- Your Receipt ---")
    subtotal = 0.0

    # Print each selected item and add up the subtotal
    for item in order:
        price = menu[item]
        subtotal += price
        print(f"{item.capitalize()}: ${price:.2f}")

    # Calculations
    discount_amount = subtotal * discount
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * tax_rate
    total = taxable_amount + tax_amount

    # Final breakdown
    print("-" * 20)
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"10% Rewards Discount: -${discount_amount:.2f}")
    print(f"Tax (8%): ${tax_amount:.2f}")
    print(f"Total Amount Due: ${total:.2f}")
    print("-" * 20)
else:
    print("\nYou didn't order anything today. See you next time!")
tax_rate = 0.08

if is_reward_user.lower() == "N":
    discount = 0.0
else:
    discount = 0

Menu= {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}
print("Menu:")
for item, price in Menu.items():
    print(f"- {item}: ${price:.2f}")
order = [] 

   