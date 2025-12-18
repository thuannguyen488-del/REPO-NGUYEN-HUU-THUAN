# Bài 5: Tìm bội chung nhỏ nhất của 2 số nguyên m và n được nhập vào 
# từ bàn phím.
# Nhập hai số nguyên m và n từ bàn phím.
# Sử dụng thuật toán Euclid để tìm ước chung lớn nhất (UCLN) của m và n.
# Tính bội chung nhỏ nhất (BCNN) bằng công thức:
#  BCNN(m, n) = (m × n) / UCLN(m, n).
# In ra giá trị của BCNN.
def ucln(a, b):
    while b:#vòng lặp đến khi b=0 thì thoát,thuật toán Euclid
        a, b = b, a % b
        '''gán đồng thời, a nhận giá trị b và b nhận 
        giá trị là số dư của a chia b'''
    return a
m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
bcnn = (m * n) // ucln(m, n)
print(f"Bội chung nhỏ nhất của {m} và {n} là: {bcnn}")
