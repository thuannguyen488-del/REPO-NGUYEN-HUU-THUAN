# Viết chương trình nhập vào:
# - Ngày, tháng, năm 
# - Tính số ngày từ đầu năm của năm đó đến ngày/tháng/năm nhập vào
#  ở trên (trong đó chú ý đến năm nhuận, tháng 2 của năm nhuận có 29 ngày
# , tháng 2 của năm không nhuận là 28 ngày)
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
if (y % 400 == 0) or (y % 4 == 0 and y% 100 != 0):
   thang2=29
else:
   thang2=28
thang=1
tong_day=0
while thang<m:
   if thang%2==0:
      tong_day+=30
   else:
      tong_day+=31
   thang+=1
tong_day=tong_day+d
if m>=2:
  tong_day=tong_day-30+thang2  
print("Số ngày tính từ đầu năm:", tong_day)