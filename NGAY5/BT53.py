# Bài tập 3: 
# Viết chương trình Python cho phép người dùng nhập 3 số nguyên 
# và hiển thị giá trị lớn nhất của ba số nguyên đó
a=int(input("nhập vào số nguyên a:"))
b=int(input("nhập vào số nguyên b:"))
c=int(input("nhập vào số nguyên c:"))
if a>b:
   if a>c:
      print("số lớn nhất là:a")
   else:
      print("số lớn nhất là:c")
else:
   if b>c:
      print("số lớn nhất là:b")
   else:
      print("số lớn nhất là:c")