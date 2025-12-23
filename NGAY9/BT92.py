# Bài tập 2: 
# Sử dụng vòng lặp trong Python để viết chương trình kiểm tra số
#  nguyên tố. 
# Chương trình cho phép người dùng nhập vào 1 số nguyên dương và hiển thị
#  kết quả số đấy có phải là số nguyên tố hay không
# Lưu ý: Số nguyên tố là số nguyên lớn hơn 1 và chỉ chia hết cho 1 
# và chính nó. ví dụ: 2, 3, 5, 7, 11, 13…
so=int(input("nhập vào số nguyên:"))
t=0
for i in range(2,so):
   if so%i==0:
      print("số đã cho không phải là số nguyên tố")
      t+=1
      break
if t==0:
   print("số đã cho là số nguyên tố")