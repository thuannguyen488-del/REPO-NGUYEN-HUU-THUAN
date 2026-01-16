# Bài 6: Chuyển đổi Tuple ↔ List
# Cho tuple:
# t = (10, 20, 30, 40)
# 1.	Chuyển tuple thành list.
# 2.	Thêm số 50 vào list.
# 3.	Chuyển list đó lại thành tuple và in ra kết quả.
t = (10, 20, 30, 40)
lis_t=list(t)
lis_t.append(50)
print(lis_t)
tup_t=tuple(lis_t)
print(tup_t)