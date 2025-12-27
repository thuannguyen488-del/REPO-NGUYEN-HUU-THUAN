# Bài tập 2: 
# Cho người dùng nhập vào 1 chuỗi và kiểm tra xem chuỗi đó có phải là 
# chuỗi Palindrome không.
# Chuỗi Palindrome là chuỗi đọc xuôi đọc ngược đều giống nhau. 
# ví dụ “abba”, “abcba”, “radar”...
chuoi=input("nhập vào chuỗi:")
# Chuẩn hóa chuỗi
chuoi = chuoi.replace(" ", "").lower()
is_palindrome = True  # giả định ban đầu là đúng
for i in range(len(chuoi)):
   if chuoi[i] != chuoi[len(chuoi) - 1 - i]:
        is_palindrome = False
        break  # thoát vòng lặp nếu phát hiện khác nhau
if is_palindrome:
    print("Chuỗi này là Palindrome.")
else:
    print("Chuỗi này không phải là Palindrome.")