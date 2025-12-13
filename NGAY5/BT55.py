# Bài tập 5: 
# Viết chương trình Python cho phép người dùng nhập vào điểm thi của 
# một bạn học sinh và hiển thị xếp loại cho học sinh đấy. 
# – Nếu điểm >=9 => hiển thị ra màn hình: xếp loại A
# – Nếu điểm >= 7 và <9 => hiển thị ra màn hình: xếp loại B
# – Nếu điểm>=5 and <7 =>hiển thị ra màn hình: xếp loại C
# – Nếu điểm<5 =>hiển thị ra màn hình: xếp loại D
diem=float(input("Nhập vào điểm của học sinh cần xếp loại:"))
if diem>=9:
     print("Bạn học sinh này xếp loại: A")
elif diem>=7:
   print("Bạn học sinh này xếp loại: B")
elif diem>=5:
   print("Bạn học sinh này xếp loại: C")
else:
   print("Bạn học sinh này xếp loại: D")