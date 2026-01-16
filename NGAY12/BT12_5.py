# Bài 5 — Module quy đổi đơn vị
# Tạo module converter.py chứa các hàm:
# ●	km_to_miles(km)
# ●	miles_to_km(miles)
# ●	celsius_to_fahrenheit(c)
# ●	fahrenheit_to_celsius(f)
# Trong main.py:
# ●	Cho sẵn:
# ○	10 km
# ○	40 độ C
# ●	Quy đổi và in kết quả
import converter
a=float(input("nhập vào số KM cần qui đổi"))
b=float(input("nhập vào số độ C cần qui đổi"))
mile=converter.km_to_miles(a)
FF=converter.celsius_to_fahrenheit(b)
print(f"{a} Km ={converter.km_to_miles(a)} m")
print(f"{b} đọ C ={converter.celsius_to_fahrenheit(b)} độ F")