# Bài tập 1: 
# Tạo 1 List có tên là ‘’numbers’’ trong Python và 
# cho người dùng nhập vào 10 phần tử số nguyên sau đó hiển thị List 
# này ra màn hình
numbers=[]
for i in range(10):
    num=int(input("nhập vào số nguyên"))
    numbers.append(num)
print("list số đã nhập:",numbers)