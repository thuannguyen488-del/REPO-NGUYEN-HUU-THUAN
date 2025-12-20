# Bài tập 8: 
# Cho người dùng nhập vào họ và tên( tiếng việt không dấu) 
# , sau đó nhập vào ký tự cần kiểm tra. Hiển thị ký tự cần kiểm tra 
# có tồn tại trong họ và tên hay không
# ví dụ người dùng nhập họ và tên là : “nguyen van a”
# ký tự cần kiểm tra là : a
# a có tồn tại trong họ và tên của người dùng
Ten =input("Nhập vào tên người dùng: ")
kytu=input("Nhập vào ký tự cần kiểm tra: ")
solan=Ten.lower().count(kytu)
print("số lần xuất hiện chứ n là:",solan)