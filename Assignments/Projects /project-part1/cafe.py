import math

print("*** Python Café ***")
user_name = input("What's your name? ").strip()
print(f"Welcome to {user_name}!")

# --- Rewards and Discount Logic ---
is_reward_user = input("Are you a rewards member? (yes/no) ").strip().lower()
if is_reward_user in ["yes", "y"]:
    discount_rate = 0.10  # 10% discount
else:
    discount_rate = 0.0

tax_rate = 0.08

# --- Menu Dictionary ---
Menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []

# --- Main Program Loop ---
while True:
    print("\n1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")
    
    choice = input("Choose an option (1-5): ").strip()
    
    # 1. VIEW MENU
    if choice == "1":
        print("\n--- Menu ---")
        for item, price in Menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")
            
    # 2. ADD AN ITEM
    elif choice == "2":
        item_to_add = input("What would you like? ").strip().lower()
        if item_to_add in Menu:
            try:
                quantity = int(input("How many? "))
                if quantity > 0:
                    for _ in range(quantity):
                        order.append(item_to_add)
                    print(f"Added {quantity} {item_to_add} to your order.")
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        else:
            print("Sorry, that item is not on the menu.")
            
    # 3. REMOVE AN ITEM
    elif choice == "3":
        if not order:
            print("Your order is currently empty. Nothing to remove.")
        else:
            item_to_remove = input("Which item should I remove? ").strip().lower()
            if item_to_remove in order:
                order.remove(item_to_remove)  # Removes exactly one instance
                print(f"Removed one {item_to_remove}.")
            else:
                print(f"Sorry, '{item_to_remove}' is not in your current order.")
                
    # 4. VIEW MY ORDER
    elif choice == "4":
        print("--- YOUR ORDER ---")
        if not order:
            print("(Your order is empty)")
            print("Items: 0")
        else:
            for item in order:
                print(f"{item}: ${Menu[item]:.2f}")
            print(f"Items: {len(order)}")
            
    # 5. CHECKOUT
    elif choice == "5":
        if not order:
            print("\nYou didn't order anything today. See you next time!")
            break
            
        print("\n===== Python Café RECEIPT =====")
        print(f"Customer: {user_name}")
        
        subtotal = 0.0
        for item in order:
            price = Menu[item]
            subtotal += price
            print(f"{item}: ${price:.2f}")
            
        # Calculations
        discount_amount = subtotal * discount_rate
        taxable_amount = subtotal - discount_amount
        tax_amount = taxable_amount * tax_rate
        total = taxable_amount + tax_amount
        
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: -${discount_amount:.2f}")
        print(f"Tax: ${tax_amount:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Thanks for visiting, {user_name}!")
        break
        
    # ERROR HANDLING FOR INVALID MENU NUMBERS
    else:
        print("Please choose a number from 1 to 5.")



