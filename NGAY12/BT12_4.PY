# Bài 4 — Module tính diện tích hình học
# Tạo module geometry.py gồm:
# ●	area_circle(r)
# ●	area_rectangle(w, h)
# ●	area_triangle(a, h)   # tam giác có đáy a chiều cao h
# Trong main.py:
# ●	Tính diện tích:
# ●	hình tròn bán kính 5
# ●	hình chữ nhật 4×7
# ●	tam giác đáy 6, chiều cao 8
import geometry
print("diện tích hình tròn bán: ",geometry.area_circle(5))
print("diện tích hình chữ nhật: ",geometry.area_rectangle(4,7))
print("diện tích hình tam giác: ",geometry.area_triangle(6,8))