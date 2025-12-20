# Viết chương trình nhập vào:
# - Ngày, tháng, năm 
# - Tính số ngày từ đầu năm của năm đó đến ngày/tháng/năm nhập vào
#  ở trên (trong đó chú ý đến năm nhuận, tháng 2 của năm nhuận có 29 ngày
# , tháng 2 của năm không nhuận là 28 ngày)
def is_leap_year(year):
    # Năm nhuận: chia hết cho 400 hoặc (chia hết cho 4 nhưng không chia hết cho 100)
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
def day_of_year(day, month, year):
    # Số ngày của từng tháng
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:month-1]) + day
# Nhập dữ liệu
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
print("Số ngày tính từ đầu năm:", day_of_year(d, m, y))