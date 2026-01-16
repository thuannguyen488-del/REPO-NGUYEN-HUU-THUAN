# Bài 6 — Module kiểm tra mật khẩu
# Tạo module password_utils.py:
# is_long_enough(pw)        # >= 8 ký tự
# has_number(pw)
# has_uppercase(pw)
# is_strong_password(pw)    # thỏa cả 3 điều kiện trên
# Trong main.py:
# Nhập mật khẩu từ bàn phím
# Kiểm tra và in thông báo:
# ●	“Mật khẩu yếu”
# ●	hoặc “Mật khẩu mạnh”
import password_utils
pw=input("nhập vào đoạn password cần kiểm tra:")
if password_utils.is_strong_password(pw):
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")