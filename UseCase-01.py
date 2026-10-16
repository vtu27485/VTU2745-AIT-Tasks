previous_price = float(input("Enter previous stock price: "))
current_price = float(input("Enter current stock price: "))

price_difference = current_price - previous_price

if price_difference > 0:
    print("Predicted stock trend: Increase")
elif price_difference < 0:
    print("Predicted stock trend: Decrease")
else:
    print("Predicted stock trend: Stable")
"""
Enter previous stock price: 100
Enter current stock price: 120
Predicted stock trend: Increase
"""
