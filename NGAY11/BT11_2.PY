# Bài tập 2: 
# Viết hàm tính diện tích, hàm tính chu vi hình tròn. Gọi hàm vừa xây 
# dựng được
import math
def dientich(r):
    return r**2*math.pi
def chuvi(r):
    return 2*math.pi*r
n=float(input("nhập vào bán kính:"))
print("diện tích đường tròn là",dientich(n))
print("chu vi đường tròn là",chuvi(n))