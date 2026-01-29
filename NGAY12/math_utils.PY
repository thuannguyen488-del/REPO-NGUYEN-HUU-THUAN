# Bài 1 — Tạo module đơn giản
# Tạo file math_utils.py chứa các hàm:
# ●	add(a, b)

# ●	sub(a, b)

# ●	mul(a, b)

# ●	div(a, b) (nhớ xử lý chia 0)

# Sau đó tạo file main.py và import để sử dụng.
def add(a,b):
    tong=a+b
    print("tổng 2 số là:",tong)
def sub(a,b):
    tru=a-b
    print("hiệu 2 số là:",tru)
def mul(a,b):
    nhan=a*b
    print("tích 2 số là:",nhan)
def div(a,b):
    if b==0:
       print("không xác định")
    else:
       chia=a/b
       print("thương 2 số là",chia)