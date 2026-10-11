


cafe_name = "Python Café"

print(f"Welcome to {cafe_name}!")

def greet_user(name):
    """Return a greeting message for the user with their name."""
    return f"Welcome to {cafe_name}, {name}!" 

user_name = input("Enter name: ")
message = greet_user(user_name)
print(message) 

# --- Fixed: Combined Rewards and Discount Logic ---
is_reward_user = input("Are you a rewards member? (y/n): ").strip().lower()
if is_reward_user == "y": 
    discount = 0.1  # 10% discount
else:
    discount = 0.0

tax_rate = 0.08 

print(f"\nWhat would you like to order today, {user_name}?")
print("--- Menu ---")
Menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

for item, price in Menu.items():
    print(f"{item.capitalize()}: ${price:.2f}")

# --- Fixed: Order Collection Loop ---
order = []
print("\nEnter the items you want to order one by one.")
print("Type 'remove' to delete an item, or 'done' when you are finished.") 

while True:
    selection = input("\nAdd item (or 'remove'/'done'): ").strip().lower()
    
    if selection == "done":
        break
        
    elif selection == "remove":
        if not order:
            print("Your order is currently empty. Nothing to remove.")
        else:
            item_to_remove = input("What item would you like to remove? ").strip().lower()
            if item_to_remove in order:
                order.remove(item_to_remove) 
                print(f"Removed '{item_to_remove}' from your order.")
            else:
                print(f"Sorry, '{item_to_remove}' is not in your current order.") 
                
    elif selection in Menu:
        order.append(selection)
        print(f"Added '{selection}' to your order. Current items: {len(order)}")
        
    else:
        print("Sorry, that item is not on our menu. Please try again.")

# --- Total and Receipt Calculation ---
if order:
    print("\n--- Your Receipt ---")
    subtotal = 0.0

    for item in order:
        price = Menu[item]
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
