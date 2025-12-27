# Bài tập 3: 
# Cho người dùng nhập vào 1 số và kiểm tra số đó có phải là số hoàn hảo
#  hay không.
# Số hoàn hảo là một số nguyên dương bằng tổng các ước số dương thực sự 
# của nó (tức là các ước số ngoại trừ chính nó).
# Các số hoàn hảo đầu tiên là 6 (1+2+3=6), 28 (1+2+4+7+14=28)
so=int(input("nhập vào số nguyên:"))
tong=0
for i in range(1,so//2+1):
   if so%i==0:
      tong+=i
if tong==so:
    print("số đã cho là số hoàn hảo",tong)
else:
    print("số đã cho không phải là số hoàn hảo",tong)