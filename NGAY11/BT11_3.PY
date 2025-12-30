# Bài tập 3: 
# Viết hàm tính giai thừa của một số nguyên bất kỳ được đưa vào. 
# Gọi hàm vừa xây dựng được.
# ví dụ về giai thừa: 5! = 1 x 2 x 3 x 4 x 5 = 120
def Giai_thua(n):
    tich=1
    for i in range(1,n+1):
       tich*=i
    return tich
a= int(input("nhập vào số nguyên a="))
print("giá trị giai thừa của a:",Giai_thua(a))