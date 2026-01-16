import tkinter as tk
from tkinter import messagebox

def clear_fields():
    for entry in entries.values():
        entry.delete(0, tk.END)

def submit_form():
    data = {label: entry.get() for label, entry in entries.items()}
    messagebox.showinfo("Thông tin đã nhập", "\n".join(f"{k}: {v}" for k, v in data.items()))

root = tk.Tk()
root.title("Address Entry Form")
root.geometry("400x400")
root.configure(bg="lightgray")

# Danh sách các nhãn
labels = [
    "First Name", "Last Name", "Address Line 1", "Address Line 2",
    "City", "State/Province", "Postal Code", "Country"
]

entries = {}

# Tạo các nhãn và ô nhập
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text + ":", bg="lightgray", anchor="w")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label_text] = entry

# Nút Clear và Submit
btn_clear = tk.Button(root, text="Clear", command=clear_fields, bg="gray", fg="white")
btn_clear.grid(row=len(labels), column=0, padx=10, pady=20)

btn_submit = tk.Button(root, text="Submit", command=submit_form, bg="blue", fg="white")
btn_submit.grid(row=len(labels), column=1, padx=10, pady=20)

root.mainloop()