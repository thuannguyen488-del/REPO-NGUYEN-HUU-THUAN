# Bài 8: Đếm phần tử
# Cho tuple:
# t = (1, 2, 2, 3, 2, 4, 5)
# 1.	Viết hàm kiểm tra 1 số xuất hiện bao nhiêu lần
# 2.	Viết hàm tìm kiếm 1 số và trả về vị trí cuối cùng của số 
# đó nếu xuất hiện nhiều lần trong Tuple
t = (1, 2, 2, 3, 2, 4, 5)
def kiemtraso(mang,a):
   return mang.count(a)
def last_index(mang, x):
        # tìm index từ cuối bằng cách đảo tuple rồi tính vị trí tương ứng
    try:
       return len(mang) - 1 - mang[::-1].index(x)
    except ValueError:
         return -1
print(last_index(t,2))