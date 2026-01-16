# Bài tập 3: 
# Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập
#  vào 10 phần tử số nguyên sau đó hiển thị tổng tất cả phần tử có 
# giá trị > 10
numbers=[]
tong=0
for i in range(10):
    num=int(input("nhập vào số nguyên"))
    numbers.append(num)
for j in range(10):
   if numbers[j]>10:
      tong+=numbers[j]
print("chuỗi:",numbers)
print("tổng các số lớn hơn 10 trong chuỗi là:",tong)