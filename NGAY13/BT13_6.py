# Bài tập 6: 
# Tạo 2 List có tên là ‘’numbers1’’ và ‘’numbers2’’ trong Python 
# Hiển thị kết quả ra màn hình là 2 list này có giống nhau hay 
# không ( giống cả số lượng phần tử và giá trị mỗi phần tử)
numbers1=[]
numbers2=[]
n1=int(input("nhập vào số phần tử của list 1:"))
for i in range(n1):
    num=int(input("nhập vào số nguyên"))
    numbers1.append(num)
n2=int(input("nhập vào số phần tử của list 2:"))
for i in range(n1):
    num=int(input("nhập vào số nguyên"))
    numbers2.append(num)
print("list số đã nhập số 1:",numbers1)
print("list số đã nhập số 2:",numbers2)
if numbers1==numbers2:
    print("kết quả so sánh: giống cả số lượng phần tử và giá trị mỗi phần tử")
else:
    print("kết quả so sánh: hai list không giống nhau")
    