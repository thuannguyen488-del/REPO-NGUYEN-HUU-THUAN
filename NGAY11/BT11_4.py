# Bài tập 4: 
# Viết hàm kiểm tra xem ký tự nhập vào có phải là ký tự số không.
#  Nếu là ký tự số hàm trả về true, ngược lại trả về false.
def kiemtra(ch):
    if ch.isdigit():
        return "true"
    else:
        return "false"
kt=input("nhập vào ký tự:")
print("kết quả kiểm tra",kiemtra(kt))