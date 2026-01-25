product = "Wireless Mouse"
price = 25.99
quantity = 2
discount_percentage = 10

price_before_discount = price * quantity
discount_amount = (discount_percentage / 100) * price_before_discount
final_price = price_before_discount - discount_amount

print(f"Price before discount: ${price_before_discount:.2f}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")

print(f"\nType of product: {type(product)}")
print(f"Type of price: {type(price)}")
print(f"Type of quantity: {type(quantity)}")