import tkinter as tk

# Window banao
window = tk.Tk()
window.title("Trading Profit Calculator - By Monis")
window.geometry("400x450")
window.configure(bg="#1e1e1e")

# Title
title = tk.Label(window, text="📈 Trading Calculator", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=20)

# Buy Price
tk.Label(window, text="Buy Price:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack()
buy_entry = tk.Entry(window, font=("Arial", 14), justify="center", width=20)
buy_entry.pack(pady=5)

# Sell Price
tk.Label(window, text="Sell Price:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack()
sell_entry = tk.Entry(window, font=("Arial", 14), justify="center", width=20)
sell_entry.pack(pady=5)

# Quantity
tk.Label(window, text="Kitne Shares?:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack()
qty_entry = tk.Entry(window, font=("Arial", 14), justify="center", width=20)
qty_entry.pack(pady=5)

# Result dikhane ke liye
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="#00ff88")
result_label.pack(pady=20)

# Button dabane pe kya hoga
def calculate():
    try:
        buy = float(buy_entry.get())
        sell = float(sell_entry.get())
        qty = int(qty_entry.get())
        profit = (sell - buy) * qty

        if profit > 0:
            result_label.config(text=f"Profit: {profit} Rs ✅", fg="#00ff88")
        elif profit < 0:
            result_label.config(text=f"Loss: {profit} Rs ❌", fg="red")
        else:
            result_label.config(text="Na Profit, Na Loss", fg="white")
    except:
        result_label.config(text="Sahi Number Dalo!", fg="yellow")

# Calculate Button
btn = tk.Button(window, text="CALCULATE KARO", font=("Arial", 14, "bold"), bg="#00ff88", fg="black", command=calculate, width=20)
btn.pack(pady=10)

window.mainloop()
