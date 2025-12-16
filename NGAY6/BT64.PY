# Bài tập 4 (*): 
# Viết chương trình Python để tính cước điện thoại bàn cho một 
# hộ gia đình với các thông số như sau:
# Phí thuê bao bắt buộc là 25 nghìn.
# 600 đồng cho mỗi phút gọi của 50 phút đầu tiên.
# 400 đồng cho mỗi phút gọi của 150 phút tiếp theo.
# 200 đồng cho bất kỳ phút gọi nào sau 200 phút đầu tiên.
time=float(input("nhập vào thời gian gọi (phút): "))
if time<=50:
   cuocdt=25000+600*time
   print("tiền cước điện thoại là:",cuocdt)
elif time<=200:
   cuocdt=25000+600*50+400*time
   print("tiền cước điện thoại là:",cuocdt)
else:
   cuocdt=25000+600*50+400*150+(time-200)*200
   print("tiền cước điện thoại là:",cuocdt)