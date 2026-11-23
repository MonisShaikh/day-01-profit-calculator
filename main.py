# Day 1 - Trading Profit Calculator
# By Monis Shaikh

print("--- Trading Profit Calculator ---")

buy_price = float(input("Buy Price dalo: "))
sell_price = float(input("Sell Price dalo: "))
quantity = int(input("Kitne shares liye?: "))

profit = (sell_price - buy_price) * quantity

print(f"\nTotal Profit: {profit} Rs")

if profit > 0:
    print("Mubarak ho! Profit hua hai ✅")
elif profit < 0:
    print("Loss hua hai, koi baat nahi seekh rahe hain ❤️")
else:
    print("Na profit, na loss - Barabar!")
