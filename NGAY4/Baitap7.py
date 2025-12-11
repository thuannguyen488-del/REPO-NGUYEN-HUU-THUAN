#Bài tập 7: Hoán đổi giá trị hai biến
#Nhập vào 2 số a và b. Hoán đổi giá trị
#Ví dụ người dùng nhập vào a = 5, b = 10
#Chương trình tiến hành hoán đổi giá trị.
#Sau khi hoán đổi xong, in ra màn hình kết quả: a = 10, b = 5
a=int(input("nhập vào số a:"))
b=int(input("nhập vào số b:"))
c=b#lưu giá trị b
b=a
a=c
print("Giá trị a sau hoán đổi là: ",a)
print("Giá trị b sau hoán đổi là: ",b)