s = input("Nhập vào một chuỗi: ")
# Chuẩn hóa chuỗi (loại bỏ khoảng trắng, viết thường)
s = s.replace(" ", "").lower()

# Kiểm tra Palindrome
if s == s[::-1]:
    print("Chuỗi này là Palindrome.")
else:
    print("Chuỗi này không phải là Palindrome.")
