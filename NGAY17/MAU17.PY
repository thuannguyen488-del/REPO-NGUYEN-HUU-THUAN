import tkinter as tk
from tkinter import messagebox
dictionary = {
    "hello": "xin chào",
    "red" : "màu đỏ",
    "code": "mã nguồn"
}
def delete_word(event):
    word = entry_word.get().lower()
    if word == "":
        messagebox.showwarning("Lỗi", "Vui lòng nhập từ cần xoá")
        return
    if word not in dictionary:
        messagebox.showwarning("Không tồn tại", "Từ này chưa có trong từ điẻn")
        return
    if messagebox.askyesno("Xác nhận", f"Xoá từ '{word}"):
        del dictionary[word]
        messagebox.showinfo("Thành công", f"Đã xoá từ: '{word}")
def search_word():
    word = entry_word.get().lower()
    text_result.delete("1.0", tk.END)
    if word == "":
        messagebox.showwarning("Lỗi", "Vui lòng nhập từ cần tìm")
        return
    if word in dictionary:
        text_result.insert(tk.END, dictionary[word])
    else:
        text_result.insert(tk.END, "Không tìm tháy")
def add_word():
    word = entry_word.get().lower()
    meaning = text_result.get("1.0", tk.END)
    if word == "" or meaning == "":
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return
    dictionary[word] = meaning
    messagebox.showinfo("Thêm từ thành công", f"Đã thêm từ: '{word}")
    entry_word.delete(0, tk.END)
    text_result.delete("1.0", tk.END)
#Xây dựng giao diện ứng dụng
root = tk.Tk()
root.title("Ứng dụng từ điển Anh-Việt")
root.geometry("500x350")
label_input = tk.Label(root, text = "Nhập từ", font = ("Arial", 17)).pack(pady = 5)
entry_word = tk.Entry(root, font = ("Arial", 13), width=30)
entry_word.pack()
btn_frame = tk.Frame(root)
btn_frame.pack(pady = 10)
btn_search = tk.Button(btn_frame, text = "Tra từ", width=12, command=search_word).grid(row = 0, column= 0, padx = 5)
btn_addWord = tk.Button(btn_frame, text = "Thêm từ", width=12, command=add_word).grid(row = 0, column= 1, padx = 5)
btn_delete = tk.Button(btn_frame, text = "Xoá từ", width=12)
btn_delete.grid(row = 0, column= 2, padx = 5)
btn_delete.bind("<Button-1>", delete_word)
tk.Label(root, text="Nghĩa của từ: ", font= ("Arial", 12)).pack()
text_result = tk.Text(root, height=7, width= 50, font=("Arial", 11))
text_result.pack()
root.mainloop()
