#Bài tập 2: 
#Viết chương trình Python cho phép nhập vào bán kính của 
# hình tròn và tính toán, hiển thị ra màn hình chu vi,
#  diện tích của hình tròn
import math
R=int(input("nhập vào bán kính đường tròn R:"))
chuvi=2*R*math.pi
dientich=R**2*math.pi
print(chuvi)
print(dientich)
