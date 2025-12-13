#Bài tập 1: 
# Viết một chương trình Python:
# Nhập vào hai số a và b, và kiểm tra xem a có chia hết cho b
#  hay không và hiển thị kết quả ra màn hình
a=int(input("nhập vào số nguyên a:"))
b=int(input("nhập vào số nguyên b:"))
c=a%b
if (a%b==0):
   print("a chia hết cho b")
else:
   print("a không hết cho b")
