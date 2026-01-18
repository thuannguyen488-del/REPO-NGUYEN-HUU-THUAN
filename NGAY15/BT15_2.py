# Bài tập 2(*): Bài tập lớn
# Chương trình quản lý quốc gia và thủ đô.
# ví dụ: {‘Viet Nam’:’Ha Noi’, ‘Indonesia’:’Jakarta’, USA:’Washington’}
# Chương trình cho phép người dùng có các tùy chọn thêm mới quốc gia và thủ đô, sửa tên thủ đô, xóa quốc gia và thủ đô, tìm kiếm thủ đô khi người dùng nhập vào quốc gia, hiển thị danh sách các quốc gia và thủ đô có trong chương trình
# Sử dụng ngôn ngữ Python để xây dựng ứng dụng với các chức năng sau:
# 1.Hiển thị menu tùy chọn
# 2.Hiển thị danh sách các quốc gia và thủ đô có trong chương trình
# 3.Cho phép thêm mới quốc gia và thủ đô
# 4.Cho phép chỉnh sửa tên thủ đô
# 5.Cho phép xóa quốc gia và thủ đô
# 6.Cho phép tìm kiếm thủ đô khi người dùng nhập tên quốc gia
# 7.Thoát chương trình
dic={}
def show_menu():
    print("===== Chương trình quản lý quốc gia và thủ đô =====")
    print("1.Hiển thị menu tùy chọn")
    print("2.Hiển thị danh sách các quốc gia và thủ đô có trong chương trình")
    print("3.Cho phép thêm mới quốc gia và thủ đô")
    print("4.Cho phép chỉnh sửa tên thủ đô")
    print("5.Cho phép xóa quốc gia và thủ đô")
    print("6.Cho phép tìm kiếm thủ đô khi người dùng nhập tên quốc gia")
    print("7. Thoát chương trình")
def show_QG_TD(dic):
    if not dic:
        print("Danh sách Quốc gia hiện đang trống.")
    else:
        print("Danh sách quốc gia và thủ đô:")
        for QG, TD in dic.items():
            print(QG, " : ", TD)
def add_dic(dic):
    QG=input("Gõ tên quốc gia cần thêm:")
    TD=input("Gõ tên Thủ đô của quốc gia cần thêm:")
    dic[QG]=TD
    print(f"Đã thêm/cập nhật: {QG} : {TD}")
    return dic
def edit_TD(dic):
    if not dic:
        print("Danh sách quốc gia hiện đang trống.")
    else:
        QG=input("Gõ tên quốc gia cần chỉnh thủ đô:")
        TD=input("Gõ tên Thủ đô của quốc gia cần chỉnh:")
        print("Danh sách quốc gia và thủ đô:")
        dic[QG]=TD
def delete_QG_TD(dic):
    QG=input("Gõ tên quốc gia cần xóa:")
    dic.pop(QG)  
def search_TD(dic) :
    QG=input("Gõ tên quốc gia cần tra thủ đô:")
    print(dic.get(QG))
show_menu()
show_QG_TD(dic)
# Vòng lặp chính
while True:
    show_menu()
    choice = input("Chọn chức năng (1-7): ")
    if choice == "1":
        show_menu()
    if choice == "2":
        show_QG_TD(dic)
    elif choice == "3":
        add_dic(dic)
    elif choice == "4":
        edit_TD(dic)
    elif choice == "5":
        delete_QG_TD(dic)
    elif choice == "6":
        search_TD(dic)
    elif choice == "7":
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-5.")