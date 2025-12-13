# Bài tập 6: (*)
# Tính chỉ số cân nặng của cơ thể
# Chỉ số khối cơ thể (Body mass index-BMI) là một thước đo sức khỏe
#  dựa trên cân nặng và chiều cao. Nó được tính bằng cách lấy cân nặng
#  đơn vị tính kilogam chia cho bình phương của chiều cao đơn vị tính mét. Công thức:
# bmi = weight / ( height ^ 2 )
# Chỉ số BMI đối với người trên 20 tuổi được phân loại và diễn giải theo
#  bảng sau
cannang=float(input("nhập vào cân nặng:"))
chieucao=float(input("nhập vào chiều cao:"))
#chỉ số BMI
bmi=cannang/(chieucao**2)
if bmi>=30:
   print("người này xếp loại: Obese")
elif bmi>=25:
   print("người này xếp loại: Overweight")
elif bmi>=18.5:
   print("người này xếp loại: Normal")
else:
   print("người này xếp loại: Underweight")