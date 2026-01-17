# Viết chương trình kiểm tra thông tin đăng nhập của người dùng. Nếu thông tin đăng nhập với 
# Username là “admin” và password là “123456” thì thông báo là “đăng nhập thành công”, 
# nếu thông tin đăng nhập không khớp với thông tin trên thì thông báo là “đăng nhập thất bại”

import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Login_Program ")
window.geometry("300x400")
def kiemtra():
    usname_kt=entry_username.get().lower()
    passW_KT=entry_PW.get().lower()
    if usname_kt=="admin" and passW_KT=="123456":
         messagebox.showwarning("Thông báo","Đăng nhập thành công")
    else:
         messagebox.showwarning("thông báo","Đăng nhập thất bại")
        
label_login= tk.Label(window, text = "Login")
label_login.place(x=20,y=20)
label_USN= tk.Label(window, text = "Username")
label_USN.place(x=20,y=50)
entry_username= tk.Entry(window)
entry_username.place(x=20,y=80)
label_PW = tk.Label(window, text = "Password")
label_PW.place(x=20,y=110)
entry_PW= tk.Entry(window)
entry_PW.place(x=20,y=140)
button_login= tk.Button(window, text= "   Login   ",command=kiemtra).place(x=20,y=170)
window.mainloop()