# Bài tập 4: 
# Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập 
# vào 10 phần tử số nguyên sau đó hiển thị có bao nhiêu phần tử > 5
numbers=[]
dem=0
for i in range(10):
    num=int(input("nhập vào số nguyên"))
    numbers.append(num)
for j in range(10):
   if numbers[j]>5:
      dem+=1
print("chuỗi:",numbers)
print("số lượng các phần tử lớn hơn 5 trong chuỗi là:",dem)