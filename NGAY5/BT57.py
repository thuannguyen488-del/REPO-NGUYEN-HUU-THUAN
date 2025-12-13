# Bài tập 7: (*) 
# Viết chương trình Python cho phép nhập vào một năm bất kỳ và hiển thị
#  xem năm đó có phải là năm nhuận không
# Cách xác định năm nhuận: Những năm chia hết cho 4 là năm nhuận,
#  ngoại trừ những năm chia hết cho 100 mà không chia hết cho 400.
# Từ đó, có thể rút gọn thành các quy tắc xác định năm nhuận:
# Những năm chia hết cho 4 mà không chia hết cho 100 là năm nhuận
# Những năm chia hết cho 100 mà không chia hết cho 400 thì KHÔNG PHẢI 
# là năm nhuận
# Những năm chia hết đồng thời cho 100 và 400 là năm nhuận
nam=int(input("Nhập vào năm cần xác định:"))
a=nam%4
chia100=nam%100
chia400=nam%400
if chia400==0:
   if chia100==0:
      print("Năm này là năm nhuần")
   else:
      print("Năm này không phải là năm nhuần")
else:
    if a==0 and chia100>0:
      print("Năm này là năm nhuần")
    else:
       print("Năm này không phải là năm nhuần")