item_name = "Laptop"
unit_price = 899.99
quantity = 2
subtotal = unit_price * quantity
tax_amount = subtotal * 0.5
final_total= subtotal + tax_amount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")
