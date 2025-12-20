# Bài tập 3:: 
# Nhập vào số nguyên dương n.
# Dùng while để tính tổng các số từ 1 đến n.
n = int(input("Nhập số nguyên dương n: "))
i=1
tong=0
while i<=n:
   tong+=i
   i=i+1
print("tổng cần tính từ 1..+...",n,"=",tong)