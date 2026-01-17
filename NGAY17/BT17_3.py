# Viết chương trình cho phép người dùng nhập các thông tin vào chương trình. 
# sau khi nhập xong dữ liệu hiển thị và người dùng nhấn nút submit thì hiển thị toàn bộ 
# thông tin đã nhập lên màn hình. Nếu người dùng bấm nút Clear thì xóa toàn bộ thông 
# tin đã nhập.
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Login_Program ")
window.geometry("300x350")
def clear():
     entry_ADDL1.delete(0, tk.END)
     entry_ADDL2.delete(0, tk.END)
     entry_FN.delete(0, tk.END)
     entry_LN.delete(0, tk.END)
     entry_city.delete(0, tk.END)
     entry_ctry.delete(0, tk.END)
     entry_pc.delete(0, tk.END)
     entry_sp.delete(0, tk.END)
def submit():
    data = {
        "First Name": entry_FN.get(),
        "Last Name": entry_LN.get(),
        "Address Line 1": entry_ADDL1.get(),
        "Address Line 2": entry_ADDL2.get(),
        "City": entry_city.get(),
        "State/Province": entry_sp.get(),
        "Postal Code": entry_pc.get(),
        "Country": entry_ctry.get()
    }
    info = "\n".join([f"{k}: {v}" for k, v in data.items()])
    messagebox.showinfo("Submitted Information", info)

# Tạo một frame (khung)
frame1 = tk.Frame(window, width=100, height=200, bg="lightgray", bd=5, relief="ridge")
frame1.pack(padx=5, pady=5, fill="both", expand=True)
frame2 = tk.Frame(window, width=50, bg="lightgray", bd=5, relief="ridge")
frame2.pack(padx=5, pady=5, fill="both", expand=True)
label_FN = tk.Label(frame1, text="First Name:", font=("Arial", 10))
label_FN.place(x=10,y=20)
entry_FN=tk.Entry(frame1)
entry_FN.place(x=150,y=20)
label_LN = tk.Label(frame1, text="Last Name:", font=("Arial", 10))
label_LN.place(x=10,y=50)
entry_LN=tk.Entry(frame1)
entry_LN.place(x=150,y=50)
label_ADDL1 = tk.Label(frame1, text="Address Line 1:", font=("Arial", 10))
label_ADDL1.place(x=10,y=80)
entry_ADDL1=tk.Entry(frame1)
entry_ADDL1.place(x=150,y=80)
label_ADDL2 = tk.Label(frame1, text="Address Line 2:", font=("Arial", 10))
label_ADDL2.place(x=10,y=110)
entry_ADDL2=tk.Entry(frame1)
entry_ADDL2.place(x=150,y=110)
label_city = tk.Label(frame1, text="City:", font=("Arial", 10))
label_city.place(x=10,y=140)
entry_city=tk.Entry(frame1)
entry_city.place(x=150,y=140)
label_sp = tk.Label(frame1, text="State/Province:", font=("Arial", 10))
label_sp.place(x=10,y=170)
entry_sp=tk.Entry(frame1)
entry_sp.place(x=150,y=170)
label_pc = tk.Label(frame1, text="Postal code:", font=("Arial", 10))
label_pc.place(x=10,y=200)
entry_pc=tk.Entry(frame1)
entry_pc.place(x=150,y=200)
label_ctry = tk.Label(frame1, text="country:", font=("Arial", 10))
label_ctry.place(x=10,y=230)
entry_ctry=tk.Entry(frame1)
entry_ctry.place(x=150,y=230)
btn_clear = tk.Button(window, text="Clear", bg="gray", fg="white",command=clear)
btn_clear.place(x=180,y=300)
btn_sub = tk.Button(window, text="Submit", bg="gray", fg="white",command=submit)
btn_sub.place(x=230,y=300)
window.mainloop()