# Bài tập cuối khóa
# Viết chương trình quản lý nhân viên
# Chương trình cho phép người dùng lưu trữ thông tin:tên ,ngày tháng năm sinh, trình độ, địa chỉ, số đt,trình độ, ... và thực hiện các 
# chức năng sau: 
# Hiển thị menu tùy chọn
# 1.Hiển thị danh sách : Hiển thị danh sách tất cả nhân viên đang lưu trữ
# 2.Cho phép thêm mới bạn bè: Thực hiện thêm mới bạn bè vào danh sách
# 3.Cho phép chỉnh sửa thông tin nhân viên:
# 3.Cho phép xóa thông tin nhân viên:
# 5.Lưu thông tin ra file
# 6.thoát chương trình: cho phép xóa bạn bè ra khỏi danh sách
# Chương trình quản lý bạn bè trên "Facebook"
nhanvien = []  # danh sách bạn bè
Profile_nhanvien = []  # danh sách bạn bè
    #mở file lên và đọc lại danh sách để chuyển thành list
with open("danh_sachnv.csv", mode="r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
    # loại bỏ ký tự xuống dòng và tách theo dấu phẩy
        Profile_nhanvien = line.strip().split(",")
        nhanvien.append(Profile_nhanvien)
def clear():
    TT1=entry_1.delete(0, tk.END)
    TT2=entry_2.delete(0, tk.END)
    TT3=entry_3.delete(0, tk.END)
    TT4=entry_4.delete(0, tk.END)
    TT5=entry_5.delete(0, tk.END)
    TT6=entry_6.delete(0, tk.END)
    TT7=entry_7.delete(0, tk.END)
    TT8=entry_8.delete(0, tk.END)
    TT9=entry_9.delete(0, tk.END)
    TT10=entry_10.delete(0, tk.END)
    TT11=entry_11.delete(0, tk.END)
def show_danhsach(ten_file="danh_sachnv.csv"):
    listbox.delete(0, tk.END)  # Xóa nội dung cũ
    with open(ten_file, mode="r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            # loại bỏ ký tự xuống dòng và tách theo dấu phẩy
            row = line.strip().split(",")
        # Hiển thị theo định dạng:
            listbox.insert(tk.END, f"{i}. Tên: {row[0]} | Ngày sinh: {row[1]}| Phòng ban: {row[2]} | Chức vụ: {row[3]} | Trình độ: {row[4]}| ĐT: {row[5]}| Đ/c: {row[6]}| Ngày BĐ: {row[8]}| Mã số NV: {row[10]}")
def add_nv(ten_file="danh_sachnv.csv"):
    TT1=entry_1.get().lower()
    TT2=entry_2.get().lower()
    TT3=entry_3.get().lower()
    TT4=entry_4.get().lower()
    TT5=entry_5.get().lower()
    TT6=entry_6.get().lower()
    TT7=entry_7.get().lower()
    TT8=entry_8.get().lower()
    TT9=entry_9.get().lower()
    TT10=entry_10.get().lower()
    TT11=entry_11.get().lower()
    Profile_nhanvien=[TT1,TT2,TT3,TT4,TT5,TT6,TT7,TT8,TT9,TT10,TT11]
    nhanvien.append(Profile_nhanvien)
    with open(ten_file, mode="a", encoding="utf-8") as f:
        f.write(",".join(Profile_nhanvien) + "\n")
    listbox.delete(0, tk.END)  # Xóa nội dung cũ
    listbox.insert(tk.END, f"Đã ghi dữ liệu {TT1} vào file {ten_file}")
    clear()
    TT12=entry_12.delete(0, tk.END)
def edit_nhanvien(ten_file="danh_sachnv.csv"):
    show_danhsach()
    if not nhanvien:
        return
    try:
        index=int(entry_12.get().lower())
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return
    if 1 <= index <= len(nhanvien):
        print("Để trống nếu muốn giữ nguyên giá trị hiện tại.")
        TT1=entry_1.get().lower()or nhanvien[index-1][0]
        TT2=entry_2.get().lower()or nhanvien[index-1][1]
        TT3=entry_3.get().lower()or nhanvien[index-1][2]
        TT4=entry_4.get().lower()or nhanvien[index-1][3]
        TT5=entry_5.get().lower()or nhanvien[index-1][4]
        TT6=entry_6.get().lower()or nhanvien[index-1][5]
        TT7=entry_7.get().lower()or nhanvien[index-1][6]
        TT8=entry_8.get().lower()or nhanvien[index-1][7]
        TT9=entry_9.get().lower()or nhanvien[index-1][8]
        TT10=entry_10.get().lower()or nhanvien[index-1][9]
        TT11=entry_11.get().lower()or nhanvien[index-1][10]
        nhanvien[index-1] = [TT1, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9, TT10,TT11]
        with open(ten_file, mode="w", encoding="utf-8") as f:
           for nv in nhanvien:
               f.write(",".join(nv) + "\n")
        # print(f"Đã đổi thông tin {TT1}.")
        listbox.delete(0, tk.END)  # Xóa nội dung cũ
        listbox.insert(tk.END, f"Đã chỉnh sửa dữ liệu {TT1} vào file {ten_file}")
        clear()
        TT12=entry_12.delete(0, tk.END)
    else:
         print("Số thứ tự không hợp lệ.")

def xoa_nv(ten_file="danh_sachnv.csv"):
    show_danhsach()
    clear()
 #mở file lên và đọc lại danh sách để chuyển thành list
    # with open(ten_file, mode="r", encoding="utf-8") as f:
    #     for i, line in enumerate(f, start=1):
    #         # loại bỏ ký tự xuống dòng và tách theo dấu phẩy
    #         Profile_nhanvien = line.strip().split(",")
    #         nhanvien.append(Profile_nhanvien)
    if not nhanvien:
        return
    try:
        index =int(entry_12.get().lower())
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return
    if 1 <= index <= len(nhanvien):
        removed = nhanvien.pop(index-1)
        print(f"Đã xóa {removed} khỏi danh sách.")
                # Ghi lại toàn bộ danh sách vào file
        with open(ten_file, mode="w", encoding="utf-8") as f:
            for nv in nhanvien:
                f.write(",".join(nv) + "\n")
        listbox.delete(0, tk.END)  # Xóa nội dung cũ
        listbox.insert(tk.END, f"Đã Xóa dữ liệu {removed} từ file {ten_file}")
        TT12=entry_12.delete(0, tk.END)
    else:
        print("Số thứ tự không hợp lệ.")
# Tạo bảng làm việc
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN ")
window.geometry("700x400")
# frame1 = tk.Frame(window, width=100, height=200, bg="lightgray", bd=5, relief="ridge")
# frame1.pack(padx=5, pady=5, fill="both", expand=True)
# frame2 = tk.Frame(window, width=50, bg="lightgray", bd=5, relief="ridge")
# frame2.pack(padx=5, pady=5, fill="both", expand=True)
label_1 = tk.Label(window, text="Tên:", font=("Arial", 10))
label_1.place(x=10,y=20)
entry_1=tk.Entry(window)
entry_1.place(x=150,y=20)
label_2 = tk.Label(window, text="Ngày sinh:", font=("Arial", 10))
label_2.place(x=10,y=50)
entry_2=tk.Entry(window)
entry_2.place(x=150,y=50)
label_3 = tk.Label(window, text="Phòng ban:", font=("Arial", 10))
label_3.place(x=10,y=80)
entry_3=tk.Entry(window)
entry_3.place(x=150,y=80)
label_4 = tk.Label(window, text="Chức vụ:", font=("Arial", 10))
label_4.place(x=10,y=110)
entry_4=tk.Entry(window)
entry_4.place(x=150,y=110)
label_5 = tk.Label(window, text="Trình độ:", font=("Arial", 10))
label_5.place(x=10,y=140)
entry_5=tk.Entry(window)
entry_5.place(x=150,y=140)
#cột 2
label_6 = tk.Label(window, text="số điện thoại:", font=("Arial", 10))
label_6.place(x=300,y=20)
entry_6=tk.Entry(window)
entry_6.place(x=450,y=20)
label_7 = tk.Label(window, text="Địa chỉ :", font=("Arial", 10))
label_7.place(x=300,y=50)
entry_7=tk.Entry(window)
entry_7.place(x=450,y=50)
label_8 = tk.Label(window, text="Địa chỉ mail:", font=("Arial", 10))
label_8.place(x=300,y=80)
entry_8=tk.Entry(window)
entry_8.place(x=450,y=80)
label_9 = tk.Label(window, text="Thời gian vào công ty:", font=("Arial", 10))
label_9.place(x=300,y=110)
entry_9=tk.Entry(window)
entry_9.place(x=450,y=110)
label_10 = tk.Label(window, text="Giới tính:", font=("Arial", 10))
label_10.place(x=300,y=140)
entry_10=tk.Entry(window)
entry_10.place(x=450,y=140)
label_11 = tk.Label(window, text="Mã nhân viên:", font=("Arial", 10))
label_11.place(x=300,y=170)
entry_11=tk.Entry(window)
entry_11.place(x=450,y=170)
label_12 = tk.Label(window, text="Số thứ tự theo DS:", font=("Arial", 10))
label_12.place(x=10,y=170)
entry_12=tk.Entry(window)
entry_12.place(x=150,y=170)
btn_update = tk.Button(window, text="Hiển thị danh sách", command=lambda: show_danhsach("danh_sachnv.csv"))
btn_update.place(x=10,y=200)
btn_them= tk.Button(window, text="Thêm vào danh sách", bg="gray", fg="white",command=add_nv)
btn_them.place(x=150,y=200)
btn_xoa = tk.Button(window, text="Xóa nhân viên", bg="gray", fg="white",command=xoa_nv)
btn_xoa.place(x=300,y=200)
btn_update = tk.Button(window, text="Cập nhật thông tin", bg="gray", fg="white",command=edit_nhanvien)
btn_update.place(x=440,y=200)
listbox = tk.Listbox(window, width=100, height=10)
listbox.place(x=10, y=230)
window.mainloop()