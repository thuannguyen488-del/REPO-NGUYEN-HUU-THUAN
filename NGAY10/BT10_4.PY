# Bài tập 4: 
# Cho người dùng nhập vào 2 số nguyên dương. Kiểm tra 2 số đó
#  có phải là cặp số thân thiết hay không.
# Một cặp số được gọi là thân thiết nếu số này bằng tổng tất 
# cả các ước của số kia (trừ chính số đó) và ngược lại.
# Ví dụ: số 220 ngoài bản thân nó ra, nó còn có 11 ước số 
# là 1, 2, 4, 5, 10, 11, 20, 44, 55 và 110. 
# Tổng của 11 ước số này vừa đúng bằng 284.
#  Ngược lại, số 284 ngoài bản thân nó, nó còn 5 ước số khác là: 
# 1, 2, 4, 71, 142, tổng của chúng cũng vừa đúng bằng 220.
so_a=int(input("nhập vào số nguyên a:"))
so_b=int(input("nhập vào số nguyên b:"))
tonga=0
tongb=0
for i in range(1,so_a//2+1):
   if so_a%i==0:
      tonga+=i
for j in range(1,so_b//2+1):
   if so_b%j==0:
      tongb+=j
if tonga==so_b and tongb==so_a:
    print("cặp số đã cho là cặp sô thân thiết")
else:
    print("không phải là cặp số thân thiết")