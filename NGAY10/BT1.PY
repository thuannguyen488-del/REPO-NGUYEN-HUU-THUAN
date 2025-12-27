# Bài tập 1: 
# Cho người dùng nhập vào 1 số nguyên dương. 
# Tính giai thừa của số đó
so=int(input("nhập vào số nguyên:"))
giaithua=1
for i in range(1,so+1):
   giaithua*=i
print("giai thừa của số đã cho:",so,"!=",giaithua)