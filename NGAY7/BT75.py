# Bài tập 5: 
# Viết chương trình Python cho phép nhập vào một số nguyên và 
# hiển thị số đó là số chẵn hay số lẻ, nếu người dùng nhập vào số 0
#  thì kết thúc chương trình
a = int(input("Nhập số nguyên dương a: "))
while a!=0:
   sodu=a%2
   if sodu==0:
      print("số đã cho là số chẵn")
   else:
      print("số đã cho là số lẻ")
   a=0