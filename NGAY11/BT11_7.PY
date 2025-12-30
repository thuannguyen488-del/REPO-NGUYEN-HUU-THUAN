# Bài tập 7: 
# Viết hàm nhận vào 1 số nguyên và hiển thị tổng tất cả các số chẵn
#  từ 0 đến chính nó
# ví dụ: người dùng nhập vào số 10 => hiển thị: tổng các số chẵn 
# từ 0 đến 10 là: 30 ( 2 + 4 + 6 + 8+10)
def tongchan(n):
    tong=0
    for i in range(n+1):
       if i%2==0:
           tong+=i
    return tong
a=int(input("nhập vào số nguyên a:"))
print(tongchan(a))