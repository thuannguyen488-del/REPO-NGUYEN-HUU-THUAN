# Bài tập 6: 
# Viết hàm nhận vào 1 số nguyên và hiển thị tất cả các số nguyên tố 
# từ 1 đến chính nó
# ví dụ: người dùng nhập vào số 10 => hiển thị: 
# các số nguyên tố từ 1 đến 10 là: 2,3,5,7
def timsont(n):
    soluong=0
    for i in range(2,n-1):
       if n%i==0:
           soluong+=1
    if soluong>=1:
        return n
    else:
        return 0
a=int(input("nhập vào số nguyên a:"))
for i in range(2,a):
   if timsont(i)==0:
       print(i,end=",")