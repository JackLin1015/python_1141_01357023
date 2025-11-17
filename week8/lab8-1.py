import tkinter as tk
from tkinter import ttk

def count():
    height = height_entry.get()
    weight = weight_entry.get()
    height_bmi = ((int(height)/100)**2)
    bmi = int(weight) / height_bmi
    health_weight1 = 18.5 * height_bmi
    health_weight2 = 24 * height_bmi
    result_label.config(text=f"您的BMI : {bmi:.2f}\n健康體重範圍 : {health_weight1:.1f}kg ~ {health_weight2:.1f}kg")

root = tk.Tk()
root.title("BMI 計算機")
root.geometry("400x400")

height_frame = tk.Frame(root)
height_frame.pack(anchor="w", pady=5, padx=10)

tk.Label(height_frame, text="身高 (公分) :", font=("Arial", 11)).pack(side="left")
height_entry = tk.Entry(height_frame, font=("Arial", 11), width=20)
height_entry.pack(side="left")

weight_frame = tk.Frame(root)
weight_frame.pack(anchor="w", pady=5, padx=10)

tk.Label(weight_frame, text="體重 (公斤) :", font=("Arial", 11)).pack(side="left")
weight_entry = tk.Entry(weight_frame, font=("Arial", 11), width=20)
weight_entry.pack(side="left")

BMI_btn = tk.Button(root, text="計算BMI", command=count, font=("Arial", 10))
BMI_btn.pack(anchor="w", padx=90)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    width=40,
    anchor="w",
    justify="left"
)
result_label.pack(anchor="w", padx=10)

root.mainloop()
