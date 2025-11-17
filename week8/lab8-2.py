import tkinter as tk
from tkinter import ttk
exchange_rate = {
    "TWD": 1,
    "USD": 31,
    "JPY": 0.22,
    "EUR": 34
}
def on_combobox_select0(event):
    value = event.widget.get()

def on_combobox_select1(event):
    value = event.widget.get()

def over():
    money = name_entry.get()
    money = int(money)
    use_m = money
    value1 = origin_combo.get()
    value2 = change_combo.get()
    if(value1 == "TWD"):
        use_m = use_m / exchange_rate[value2]
    else:
        use_m = use_m * exchange_rate[value1]
    result_label.config(text=f"結果: {money:.2f}{value1}={use_m:.2f}{value2}\n")

root = tk.Tk()
root.title("金錢兌換小工具")
root.geometry("600x400")


tk.Label(root, text="金額:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
name_entry = tk.Entry(root, font=("Arial", 11), width=20)
name_entry.grid(row=0, column=1, sticky="w")


tk.Label(root, text="原始貨幣:", font=("Arial", 11, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=10)
origin_combo = ttk.Combobox(
    root,
    values=["USD", "EUR", "JPY", "TWD"],
    font=("Arial", 10),
    width=20,
    state="readonly"
)
origin_combo.grid(row=1, column=1, sticky="w")
origin_combo.set("選擇貨幣")
origin_combo.bind("<<ComboboxSelected>>", on_combobox_select0)

# -------- 兌換貨幣 --------
tk.Label(root, text="目標貨幣:", font=("Arial", 11, "bold")).grid(row=2, column=0, sticky="w", padx=10, pady=10)
change_combo = ttk.Combobox(
    root,
    values=["USD", "EUR", "JPY", "TWD"],
    font=("Arial", 10),
    width=20,
    state="readonly"
)
change_combo.grid(row=2, column=1, sticky="w")
change_combo.set("選擇貨幣")
change_combo.bind("<<ComboboxSelected>>", on_combobox_select1)


label2 = tk.Label(root, text="", font=("Arial", 10), fg="blue")
label2.grid(row=3, column=0, columnspan=2, sticky="w", padx=10)


over_btn = tk.Button(root, text="開始換算", command=over, font=("Arial", 12))
over_btn.grid(row=4, column=0, columnspan=2, pady=15, padx=10)


result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=10)

root.mainloop()
