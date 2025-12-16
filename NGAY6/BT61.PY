# Bài tập 1: 
# Viết một chương trình Python:
# cho phép Nhập lương nhân viên và tính thuế thu nhập sau đó hiển 
# thị lương ròng (số tiền lương thực sự mà nhân viên đó nhận được). 
# Với các thông số giả sử như sau:
# 30% thuế thu nhập nếu lương là 15 triệu.
# 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# 10% thuế thu nhập nếu lương dưới 7 triệu
luong=float(input("nhập vào lương của nhân viên cần tính: "))
if luong>=15000000:
   luongnet=0.7*luong
   print("Lương thực lãnh của nhân viên này là",luongnet)
elif luong>=7000000:
   luongnet=0.8*luong
   print("Lương thực lãnh của nhân viên này là",luongnet)
else:
   luongnet=0.9*luong
   print("Lương thực lãnh của nhân viên này là",luongnet)