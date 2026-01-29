# Bài tập 7: 
# Cho người dùng nhập vào họ và tên( tiếng việt không dấu) , 
# hiển thị số lần xuất hiện của ký tự ‘n’ trong họ và tên của người dùng 
# ví dụ người dùng nhập họ và tên là : “nguyen van a”
# Số lần xuất hiện của ký tự ‘n’ là: 3
Ten = input("Nhập vào tên người dùng (không dấu): ")
solan=Ten.lower().count('n')
print("số lần xuất hiện chứ n là:",solan)