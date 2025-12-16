# Bài tập 5: 
# Viết chương trình Python cho phép người dùng nhập vào một số nguyên. 
# Hiển thị ra màn hình là : “Fizz” nếu số đó chia hết cho 3
# Hiển thị ra màn hình là : “Buzz” nếu số đó chia hết cho 5
# Hiển thị ra màn hình là : “Fizz-Buzz” nếu số đó chia hết cho 15
# Hiển thị ra màn hình chính số đó nếu nó không thuộc một trong 
# các trường hợp trên.
a=int(input("nhập vào số nguyên a cần xác định: "))
sodu3=a%3
sodu5=a%5
if sodu3==0 and sodu5!=0:
   print("“Fizz”")
elif sodu3!=0 and sodu5==0:
   print("“Buzz”")
elif sodu5==0 and sodu3==0:
   print("“Fizz-Buzz”")
else:
   print(a)