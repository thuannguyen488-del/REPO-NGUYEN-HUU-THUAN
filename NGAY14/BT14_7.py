# Bài 7: Tuple lồng nhau
# Cho tuple:
# students = (
#     ("An", 8.5),
#     ("Bình", 7.0),
#     ("Chi", 9.2)
# )
# 1.	In tên và điểm của từng học sinh.

# 2.	Tìm học sinh có điểm cao nhất.
students = (("An", 8.5),("Bình", 7.0),("Chi", 9.2))
for ten,diem in students:
    print(f"{ten}: {diem}")
   # tim hoc sinh co diem cao nhat
hsgioi_nhat,diem_caonhat=students[0]
for ten,diem in students:
    if diem>diem_caonhat:
        hsgioi_nhat,diem_caonhat=ten,diem
print(hsgioi_nhat)