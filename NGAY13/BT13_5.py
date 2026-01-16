# Bài tập 5: 
# Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người dùng nhập 
# vào 10 phần tử số nguyên. 
# Tiếp tục cho người dùng nhập 1 số n 
# Nếu n tồn tại trong list numbers thì tiến hành xóa giá trị n ra khỏi 
# list number
#  sau đó hiển thị có bao nhiêu phần tử > 5
numbers=[]
dem=0
for i in range(10):
    num=int(input("nhập vào số nguyên"))
    numbers.append(num)
so_moi=int(input("nhập vào số cần so sánh:"))
while so_moi in numbers:
    numbers.remove(so_moi)
for k in range(len(numbers)):
   if numbers[k]>5:
      dem+=1
print("chuỗi:",numbers)
print("số lượng các phần tử lớn hơn 5 trong chuỗi là:",dem)