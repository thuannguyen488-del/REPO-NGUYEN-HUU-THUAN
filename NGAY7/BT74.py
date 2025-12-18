# Bài tập 4: 
# Viết chương trình Python cho phép nhập vào một số nguyên dương và 
# in ra các số chia hết cho 3 từ 0 đến chính nó. 
# ví dụ nhập vào số 10 sẽ in ra các số chia hết cho 3 từ 0 đến 10 
# là : 0,3,6,9
a = int(input("Nhập số nguyên dương a: "))
i=0
while i<=a:
   sodu=i%3
   if sodu==0:
       print(i)
   i=i+1