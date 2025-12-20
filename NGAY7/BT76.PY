# Bài tập 6: 
# Sử dụng vòng lặp while trong  Python để viết chương trình sau: 
# Cho người dùng nhập vào 1 số. Hiển thị ra màn hình tổng từ 1 đến chính số đó.
# ví dụ : 
# Người dùng nhập vào : 5
# Kết quả hiển thị: 15 
# vì 1 + 2 + 3 + 4 + 5 = 15
# Người dùng nhập vào : 10
# Kết quả hiển thị: 55
# vì 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
n = int(input("Nhập số nguyên dương n: "))
i=1
tong=0
while i<=n:
   tong+=i
   i=i+1
print("tổng cần tính từ 1..+...",n,"=",tong)