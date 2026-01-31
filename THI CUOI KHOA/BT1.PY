# Câu 1: Nhập từ bàn phím list số nguyên a gồm n phần tử (n<=10). Hiển thị list vừa nhập. 
# Kiểm tra list vừa nhập có phải list dạng sóng hay không ? nếu là list dạng sóng hiển thị 
# kết quả là “true”, ngược lại hiển thị “false”.
# list dạng sóng là list mà mỗi phần tử thứ i nhỏ hơn cả 2 phần tử xung quanh liền kề, 
# hoặc lớn hơn cả 2 phần tử xung quanh liền kề:
# Ví dụ:
# list 1: [5, 2, 6, 3, 4] 🡺 true
# list 2: [5, 6, 7, 5, 8] 🡺 false
# list 3: [5, 1, 5, 5, 6] 🡺 false
list_a=[]
dem=0
n=int(input("nhập số phần tử của list a"))
for i in range(n):
    num=int(input("nhập vào số nguyên"))
    list_a.append(num)
print(list_a)
kiemtra=True
for i in range(1,n-1):
    if (list_a[i]>= list_a[i-1] and list_a[i] <=list_a[i+1])or(list_a[i]<= list_a[i-1] and list_a[i]>= list_a[i+1]):
        kiemtra=False
        break
if kiemtra:
    print("true")
else:
    print("false")