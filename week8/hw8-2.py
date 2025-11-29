import tkinter as tk

root = tk.Tk()
root.title("記帳小工具")
root.geometry("450x400")
records = []

def update_total():
    total = sum(amount for _, amount in records)
    total_label.config(text=f"總金額：{total:.2f} 元")

def add_record():
    item = item_entry.get()
    try:
        amount = float(amount_entry.get())
    except:
        return
    if item.strip() == "":
        return
    records.append((item, amount))
    listbox.insert(tk.END, f"{item} - {amount:.2f} 元")
    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    update_total()

def delete_selected():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    listbox.delete(index)
    del records[index]
    update_total()

def clear_all():
    listbox.delete(0, tk.END)
    records.clear()
    update_total()

item_frame = tk.Frame(root)
item_frame.pack(pady=5)
tk.Label(item_frame, text="品項：").grid(row=0, column=0)
item_entry = tk.Entry(item_frame, width=20)
item_entry.grid(row=0, column=1, padx=20)
tk.Button(item_frame, text="新增", width=10, command=add_record).grid(row=0, column=2, padx=5)

amount_frame = tk.Frame(root)
amount_frame.pack(pady=5)
tk.Label(amount_frame, text="金額：").grid(row=0, column=0)
amount_entry = tk.Entry(amount_frame, width=20)
amount_entry.grid(row=0, column=1, padx=20)
tk.Button(amount_frame, text="刪除選取", width=10, command=delete_selected).grid(row=0, column=2, padx=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=10,padx=10, anchor="w")
listbox = tk.Listbox(list_frame, width=40, height=10)
listbox.grid(row=0, column=0, sticky="w")
tk.Button(list_frame, text="清空", width=8, command=clear_all).grid(row=0, column=1, padx=10)

total_label = tk.Label(root, text="總金額：0.00 元", font=("Arial", 12))
total_label.pack(pady=5,padx=10, anchor="w")
root.mainloop()