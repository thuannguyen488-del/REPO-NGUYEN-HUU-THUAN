import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("First_Program ")
window.geometry("500x300")
def dangnhap(event):
    word = entry_username.get().lower()
    if word=="":
        messagebox.showwarning("Lỗi", "chưa nhập tên đăng nhập")
        return
    else:
        label_tb= tk.Label(window, text = f"Bạn đã nhập tên đăng nhập là: {word}",font=("Arial", 10))
        label_tb.place(x=10,y=30)
# def dangnhap(event):
#     word = entry_username.get().lower()
#     if word=="":
#         messagebox.showwarning("Lỗi", "chưa nhập tên đăng nhập")
#         return
#     else:
#         text_result.insert(tk.END,f"Bạn đã nhập tên đăng nhập là: {word}" )
label_USN= tk.Label(window, text = "Tên của bạn",font=("Arial", 10))
label_USN.place(x=10,y=60)
entry_username= tk.Entry(window)
entry_username.place(x=100,y=60)
button_login= tk.Button(window, text= "   Đăng nhập   ",font=("Arial", 10))
button_login.place(x=100,y=90)
# text_result = tk.Text(window, height=1, width= 50, font=("Arial", 10))
# text_result.place(x=10,y=30)
button_login.bind("<Button-1>", dangnhap)
# label_tb= tk.Label(window, text = f"Bạn đã nhập tên đăng nhập là: {word}",font=("Arial", 10))
# label_tb.place(x=10,y=30)
window.mainloop()
