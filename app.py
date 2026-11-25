import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Trading Calculator PRO - By Monis")
window.geometry("420x700")
window.configure(bg="#1e1e1e")

tk.Label(window, text="📈 Trading Calculator PRO", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=12)

def make_label(text):
    tk.Label(window, text=text, font=("Arial", 11), bg="#1e1e1e", fg="white").pack()

def make_entry():
    e = tk.Entry(window, font=("Arial", 13), justify="center", width=22)
    e.pack(pady=3)
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
result_label.pack(pady=10)

# --- HISTORY WALA HISSA ---
tk.Label(window, text="📜 History - Pichle Hisaab:", font=("Arial", 12, "bold"), bg="#1e1e1e", fg="white").pack(pady=5)

history_list = tk.Listbox(window, width=55, height=6, font=("Arial", 10), bg="#2d2d2d", fg="white")
history_list.pack(pady=5)

# Purani History file se load karo
try:
    with open("history.txt", "r") as f:
        for line in f:
            history_list.insert(tk.END, line.strip())
except:
    pass

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
            text=f"{msg}\nNet Profit: {net:.2f} Rs | Profit %: {profit_per:.2f}%",
            fg=color
        )

        # History me save karo
        time_now = datetime.now().strftime("%d/%m %H:%M")
        history_text = f"{time_now} | Buy {buy} Sell {sell} Qty {qty} = Net {net:.0f} Rs"
        history_list.insert(tk.END, history_text)
        history_list.yview(tk.END)

        # File me bhi save karo taaki band karne ke baad bhi rahe
        with open("history.txt", "a") as f:
            f.write(history_text + "\n")

    except:
        result_label.config(text="Sahi Number Dalo!", fg="yellow")

tk.Button(window, text="CALCULATE KARO", font=("Arial", 13, "bold"), bg="#00ff88", fg="black", command=calculate, width=22).pack(pady=8)

window.mainloop()
