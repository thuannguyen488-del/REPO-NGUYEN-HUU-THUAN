# Bài 2: Độ dài Tuple
# Cho tuple:
# t = (3, 7, 1, 9, 4)
# 1.	In ra số lượng phần tử của tuple.
# 2.	Kiểm tra xem số 7 có nằm trong tuple hay không.
t = (3, 7, 1, 9, 4)
print(len(t))
a=int(input("nhập phần tử cần kiểm tra:   "))
if t.count(a)>0:
    print(f"số {a} nằm trong tuple đã cho")
else:
    print(f"số {a} không nằm trong tuple đã cho")