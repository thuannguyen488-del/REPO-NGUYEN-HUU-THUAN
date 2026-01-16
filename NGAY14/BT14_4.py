# Bài 4: Tính toán trên Tuple
# Cho tuple:
# numbers = (2, 4, 6, 8, 10)
# 1.	Tính tổng các phần tử.
# 2.	Tìm giá trị lớn nhất và nhỏ nhất.
numbers = (2, 4, 6, 8, 10)
tong=0
max=0
for i in numbers:
    tong+=i
    if max<=i:
       max=i
print("tổng các phần tử", tong)
print("giá trị lớn nhất", max)

      