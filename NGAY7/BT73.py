# Bài tập 3: 
# Viết chương trình Python cho phép nhập vào một số nguyên 
# dương sau đó hiển thị ra tất cả ước của số đó. 
# ví dụ nhập vào 6 thì in ra màn hình 2, 3, 6
a = int(input("Nhập số nguyên a: "))
i=1
while i<=a:
   sodu=a%i
   if sodu==0 and i!=1:
       print(i)
   i=i+1