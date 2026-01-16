# Bài tập 2: 
# Tạo 1 List có tên là ‘’numbers’’ trong Python và cho người 
# dùng nhập vào 10 phần tử số nguyên sau đó hiển thị giá trị 
# lớn nhất trong list numbers và vị trí của phần tử đó trong mảng
numbers=[]
for i in range(10):
    num=int(input("nhập vào số nguyên"))
    numbers.append(num)
print("list số đã nhập:",numbers)
max_number = max(numbers)
vitri_max= numbers.index(max_number)
print("giá trị lớn nhất là:",max_number, "vị trí trong chuỗi thứ: ",vitri_max)