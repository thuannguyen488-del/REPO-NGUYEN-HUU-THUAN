# Bài tập 5:
# Mô phỏng tìm kiếm mật khẩu vét cạn (Brute Force) đơn giản:
#  Bằng cách giả lập việc bẻ khóa một mật khẩu gồm 3 chữ số. 
# Ví dụ:
# Mật khẩu đúng là "381".(học viên tự đặt mật khẩu bất kỳ hoặc sử dụng
#  hàm random())
# Sử dụng ba vòng lặp for lồng nhau (mỗi vòng từ 0 đến 9) 
# để thử tất cả các kết hợp có thể. In ra mỗi lần thử. 
# Khi tìm thấy mật khẩu chính xác, in ra "Password found: 381" 
import random
matkhau=random.randint(100,999)
for i in range(10):
   for j in range(10):
      for k in range(10):
         mk=i*100+j*10+k
         print("mật khẩu thử",mk,end=";")
         if mk==matkhau:
            matkhaumay=mk
print("mật khẩu là:",matkhaumay)