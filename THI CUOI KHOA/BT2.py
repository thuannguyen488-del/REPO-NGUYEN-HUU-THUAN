# Câu 2: Viết chương trình kiểm tra năm nhuận dương lịch từ chuỗi người dùng nhập vào.
# Nội dung chương trình gồm 2 bước sau:
# Bước 1: Xây dựng hàm kiểm tra chuỗi người dùng nhập vào có đúng định dạng “dd/MM/yyyy”. 
# Hàm có kiểu trả về là boolean.
# ●	Nếu hàm trả về false thì hiển thị nội dung: “yêu cầu nhập đúng định dạng dd/MM/yyyy”.
# ●	Nếu hàm trả về true thì tiếp tục bước 2
# Bước 2: Xây dựng hàm kiểm tra năm nhuận.
# ●	Nếu đúng định dạng trên và “yyyy” là năm nhuận thì hiển thị nội dung: “yyyy là năm nhuận”.
# ●	Nếu đúng định dạng trên và “yyyy” không là năm nhuận thì hiển thị nội dung:
#  “yyyy không là năm nhuận”.

# Hàm kiểm tra định dạng ngày tháng năm
def KT_dinhdang(year):
    tach_nam = year.split("/") 
    ngay=int(tach_nam[0])
    thang=int(tach_nam[1])
    nam=int(tach_nam[2])
    if ngay<=31 and thang<=12 and nam>=1000:
        return True
    else:
        return False
# Hàm kiểm tra năm nhuận
def kt_nam_nhuan(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
ngay_kt=input("Nhập vào ngày tháng năm dd/mm/yyyy:")
if KT_dinhdang(ngay_kt):
    nam = int(ngay_kt.split("/")[-1])
    if kt_nam_nhuan(nam):
         print(f"Năm {nam} là năm nhuần")
    else:
        print(f"Năm {nam} không phải là năm nhuần")
else:
    print("Nhập lại cho đúng định dạng dd/MM/yyyy")