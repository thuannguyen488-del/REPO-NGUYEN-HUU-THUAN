# Bài tập 5: 
# Viết hàm nhận vào 3 số nguyên bất kỳ, trả về số nguyên có giá trị 
# nhỏ nhất.
def min_3(a,b,c):
    if a>=b:
        if b>=c:
            min=c
        else:
            min=b
    else:
        if a>=c:
            min=c
        else:
            min=a
    return min
x= int(input("nhập vào số x="))
y= int(input("nhập vào số y="))
z= int(input("nhập vào số z="))
print("giá trị nhỏ nhất", min_3(x,y,z))