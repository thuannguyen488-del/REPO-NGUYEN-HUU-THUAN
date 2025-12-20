# Bài tập 2:: 
# Nhập liệu an toàn: Viết chương trình yêu cầu người dùng nhập điểm 
# môn học (từ 0 đến 10). Nếu người dùng nhập sai (ví dụ 15 hoặc -2), 
# yêu cầu họ nhập lại cho đến khi đúng thì thôi.
diem = float(input("Nhập số điểm: "))
while diem<0 or diem>10:
   diem = float(input("Nhập số điểm: "))
print("số điểm học sinh đúng là:",diem)