# Bài 3 — Module kiểm tra số
# Tạo module number_utils.py chứa các hàm:
# ●	is_even(n)        # trả về True nếu n chẵn
# ●	is_odd(n)		# trả về True nếu n lẻ
# ●	is_prime(n)       # trả về True nếu n là số nguyên tố
# Trong main.py:
# Nhập 1 số từ bàn phím
# In ra:
# ●	số đó có phải số chẵn không
# ●	số lẻ không
# ●	số nguyên tố không
import number_utils
a= int(input("nhập vào số a: "))
if number_utils.is_even(a):
   print(f"số {a} là số chẵn")
else:
   print(f"số {a} là số lẻ")
   if number_utils.is_prime(a):
      print(f"số {a} là số nguyên tố")
   else:
      print(f"số {a} không phải là số nguyên tố")