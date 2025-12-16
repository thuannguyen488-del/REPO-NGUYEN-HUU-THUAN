# Bài tập 3: 
# Cửa hàng của bạn nhận gửi bán sản phẩm cho một công ty khác và
#  hưởng hoa hồng, với mức hoa hồng theo doanh số bán như sau:
# 5% nếu tổng doanh số nhỏ hơn hoặc bằng 100 triệu.
# 10% nếu tổng doanh số nhỏ hơn hoặc bằng 300 triệu.
# 20 % nếu tổng doanh số là lớn hơn 300 triệu.
# Hãy viết chương trình Python để tính hoa hồng bạn sẽ nhận được dựa
#  trên doanh số bán hàng.
doanhso=float(input("nhập vào doanh số bán hàng của nhân viên: "))
if doanhso<=100000000:
   hoahong=0.05*doanhso
   print("Hoa hồng nhân viên nhận được là:",hoahong)
elif doanhso<=300000000:
   hoahong=0.1*doanhso
   print("Hoa hồng nhân viên nhận được là:",hoahong)
else:
   hoahong=0.2*doanhso
   print("Hoa hồng nhân viên nhận được là:",hoahong)