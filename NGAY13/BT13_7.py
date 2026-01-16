# Bài tập 7(*): Bài tập lớn
# Viết chương trình quản lý bạn bè trên facebook 
# Chương trình cho phép người dùng lưu trữ tên bạn bè và thực hiện các 
# chức năng sau: 
# 1.Hiển thị menu tùy chọn
# 2.Hiển thị danh sách bạn bè : Hiển thị danh sách tất cả các bạn bè đang lưu trữ
# 3.Cho phép thêm mới bạn bè: Thực hiện thêm mới bạn bè vào danh sách
# 4.Cho phép chỉnh sửa tên bạn bè: Cho phép chỉnh sửa tên bạn bè
# 5.Cho phép xóa bạn bè: cho phép xóa bạn bè ra khỏi danh sách
# Chương trình quản lý bạn bè trên "Facebook"

friends = []  # danh sách bạn bè
def show_menu():
    print("===== CHƯƠNG TRÌNH QUẢN LÝ BẠN BÈ FACEBOOK =====")
    print("1. Hiển thị danh sách bạn bè")
    print("2. Thêm mới bạn bè")
    print("3. Chỉnh sửa tên bạn bè")
    print("4. Xóa bạn bè")
    print("5. Thoát chương trình")
def show_friends():
    if not friends:
        print("Danh sách bạn bè hiện đang trống.")
    else:
        print("Danh sách bạn bè:")
        for i, name in enumerate(friends, start=1):
            print(f"{i}. {name}")

def add_friend():
    name = input("Nhập tên bạn bè muốn thêm: ")
    friends.append(name)
    print(f"Đã thêm {name} vào danh sách.")
def edit_friend():
    show_friends()
    if friends:
        index = int(input("Nhập số thứ tự bạn bè muốn chỉnh sửa: "))
        if 1 <= index <= len(friends):
            new_name = input("Nhập tên mới: ")
            old_name = friends[index-1]
            friends[index-1] = new_name
            print(f"Đã đổi tên {old_name} thành {new_name}.")
        else:
            print("Số thứ tự không hợp lệ.")

def delete_friend():
    show_friends()
    if friends:
        index = int(input("Nhập số thứ tự bạn bè muốn xóa: "))
        if 1 <= index <= len(friends):
            removed = friends.pop(index-1)
            print(f"Đã xóa {removed} khỏi danh sách.")
        else:
            print("Số thứ tự không hợp lệ.")

# Vòng lặp chính
while True:
    show_menu()
    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        show_friends()
    elif choice == "2":
        add_friend()
    elif choice == "3":
        edit_friend()
    elif choice == "4":
        delete_friend()
    elif choice == "5":
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-5.")
