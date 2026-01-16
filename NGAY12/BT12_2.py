# Bài 2 — Đặt alias cho module
# Sử dụng lại module math_utils.py. (ở bài 1)
# Trong main.py, import module với tên ngắn hơn:
# import math_utils as mu
# Sau đó dùng:
# mu.add(3, 5)

import math_utils as mu
a= int(input("nhập vào số a"))
b= int(input("nhập vào số b"))
mu.add(a,b)
mu.sub(a,b)
mu.div(a,b)
mu.mul(a,b)