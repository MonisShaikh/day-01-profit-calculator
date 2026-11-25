import tkinter as tk

window = tk.Tk()
window.title("Trading Calculator Pro - By Monis")
window.geometry("420x600")
window.configure(bg="#1e1e1e")

tk.Label(window, text="📈 Trading Calculator PRO", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=15)

def make_label(text):
    tk.Label(window, text=text, font=("Arial", 11), bg="#1e1e1e", fg="white").pack()

def make_entry():
    e = tk.Entry(window, font=("Arial", 13), justify="center", width=22)
    e.pack(pady=4)
    return e

make_label("Buy Price:")
buy_entry = make_entry()

make_label("Sell Price:")
sell_entry = make_entry()

make_label("Kitne Shares?:")
qty_entry = make_entry()

make_label("Brokerage % (Ex: 0.1):")
brokerage_entry = make_entry()
brokerage_entry.insert(0, "0.1")

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#1e1e1e", fg="#00ff88", justify="left")
result_label.pack(pady=15)

def calculate():
    try:
        buy = float(buy_entry.get())
        sell = float(sell_entry.get())
        qty = int(qty_entry.get())
        brok_per = float(brokerage_entry.get())

        total_buy = buy * qty
        total_sell = sell * qty
        gross = total_sell - total_buy
        brokerage = (total_buy + total_sell) * brok_per / 100
        net = gross - brokerage
        profit_per = ((sell - buy) / buy) * 100

        if net > 0:
            color = "#00ff88"
            msg = "PROFIT HUA! ✅"
        elif net < 0:
            color = "red"
            msg = "LOSS HUA! ❌"
        else:
            color = "white"
            msg = "BARABAR!"

        result_label.config(
            text=f"{msg}\n\nGross Profit: {gross:.2f} Rs\nBrokerage: -{brokerage:.2f} Rs\n----------------\nNet Profit: {net:.2f} Rs\nProfit %: {profit_per:.2f}%",
            fg=color
        )
    except:
        result_label.config(text="Sahi Number Dalo!", fg="yellow")

tk.Button(window, text="CALCULATE KARO", font=("Arial", 13, "bold"), bg="#00ff88", fg="black", command=calculate, width=22).pack(pady=10)

window.mainloop()
