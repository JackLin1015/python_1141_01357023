import tkinter as tk

def calculate_score():
    score = 0
    score += q1_var.get()
    score += q2_var.get()
    score += q3_var.get()
    score += q4_var.get()
    if score >= 3:
        result = "健康狀況：健康狀況良好"
    else:
        result = "健康狀況：健康狀況不好"
    result_label.config(text=f"您的總分：{score}\n{result}")
root = tk.Tk()
root.title("生活健康狀況問卷")
root.geometry("500x300")  

tk.Label(root, text="生活健康狀況問卷",font=("Arial", 12)).grid(row=0, column=0, columnspan=3, pady=10)

q1_var = tk.IntVar()
tk.Label(root, text="1.請問是否有抽菸習慣？").grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="是", variable=q1_var, value=0).grid(row=1, column=1)
tk.Radiobutton(root, text="否", variable=q1_var, value=1).grid(row=1, column=2)

q2_var = tk.IntVar()
tk.Label(root, text="2.請問是否有飲酒習慣？").grid(row=2, column=0, sticky="w")
tk.Radiobutton(root, text="是", variable=q2_var, value=0).grid(row=2, column=1)
tk.Radiobutton(root, text="否", variable=q2_var, value=1).grid(row=2, column=2)

q3_var = tk.IntVar()
tk.Label(root, text="3.每天睡眠時間是否超過六小時？").grid(row=3, column=0, sticky="w")
tk.Radiobutton(root, text="是", variable=q3_var, value=1).grid(row=3, column=1)
tk.Radiobutton(root, text="否", variable=q3_var, value=0).grid(row=3, column=2)

q4_var = tk.IntVar()
tk.Label(root, text="4.是否有均衡飲食？").grid(row=4, column=0, sticky="w")
tk.Radiobutton(root, text="是", variable=q4_var, value=1).grid(row=4, column=1)
tk.Radiobutton(root, text="否", variable=q4_var, value=0).grid(row=4, column=2)

submit_button = tk.Button(root, text="送出問卷並顯示結果", command=calculate_score)
submit_button.grid(row=5, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=3, pady=10)
root.mainloop()