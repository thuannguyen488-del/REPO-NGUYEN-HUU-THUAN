# Câu 3: Xây dựng ứng dụng quản lý xe máy trong bãi đỗ xe của trung tâm codeGym.
# Thông tin của Xe bao gồm:
# ●	Biển số xe: chuỗi tối đa 20 ký tự
# ●	Họ tên sinh viên: chuỗi tối đa 40 ký tự
# ●	Chứng minh nhân dân: Kiểu số
# ●	Hãng xe máy: chọn từ danh sách có sẵn [Honda, Yamaha, Sym, Piaggio, Suzuki, Ducati, Hãng khác]
# ●	Phí gửi xe đã đóng: kiểu số 
# Yêu cầu chương trình thực hiện được các chức năng sau:
# -	Hiển thị được danh sách xe máy trong bãi xe của trung tâm.
# -	Thêm mới một Xe vào danh sách.
# -	Kiểm tra được nội dung hợp lệ trước khi thêm mới.
# -	Xóa một Xe ra khỏi danh sách.
ds_xe = []
thongtin_xe = []
loai_xe=["Honda","Yamaha","Sym","Piaggio","Suzuki","Ducati","Hãng khác"]
def show_menu():
    print("===== CHƯƠNG TRÌNH QUẢN LÝ XE TRUNG TÂM CODEGYM =====")
    print("1. Hiển thị được danh sách xe máy trong bãi xe của trung tâm")
    print("2. Thêm mới một Xe vào danh sách")
    print("3. Xóa một Xe ra khỏi danh sácH")
    print("4. Thoát chương trình")
def show_ds_xe():
    if not ds_xe:
        print("Danh sách xe hiện đang trống.")
    else:
        print("Danh sách xe:")
        for i, thongtin_xe in enumerate(ds_xe, start=1):
            print(f"{i}. Biển số: {thongtin_xe[0]} | Họ tên sinh viên: {thongtin_xe[1]}| Chứng minh nhân dân: {thongtin_xe[2]}| Hãng xe: {thongtin_xe[3]}| Phí gửi xe đã đóng: {thongtin_xe[4]}| ")
def kt_hople(bien_so,ten_sv,cmnd, hang_xe, phi_gui):
    if len(bien_so) > 20 or len(ten_sv) > 40:
        return False
    if not cmnd.isdigit() or not str(phi_gui).isdigit():
        return False
    if hang_xe not in loai_xe:
        return False
    return True
def add_xe():
    bien_so = input("Nhập vào biển số (chuỗi tối đa 20 ký tự) muốn thêm: ")
    ten_sv = input("Nhập tên sinh viên (chuỗi tối đa 40 ký tự): ")
    cmnd = input("Nhập chứng minh nhân dân: ")
    hang_xe = input("Nhập loại xe [Honda, Yamaha, Sym, Piaggio, Suzuki, Ducati, Hãng khác]: ")
    phi_gui = input("Nhập tiền phí đã đóng: ")
    if kt_hople(bien_so,ten_sv,cmnd, hang_xe, phi_gui):
        thongtin_xe=[bien_so,ten_sv,int(cmnd),hang_xe,int(phi_gui)]
        ds_xe.append(thongtin_xe)
        print(f"Đã thêm thông tin bạn{thongtin_xe} vào danh sách.")
    else:
        print("Thông tin nhập không hợp lệ, vui lòng nhập lại.")
def xoa_xe():
    bien_so = input("Nhập biển số xe cần xóa: ")
    for xe in ds_xe:
        if xe[0] == bien_so:
            ds_xe.remove(xe)
            print("Xóa xe thành công!")
            return
    print("Không tìm thấy xe với biển số này.")
# Vòng lặp chính
while True:
    show_menu()
    choice = input("Chọn chức năng (1-5): ")
    if choice == "1":
        show_ds_xe()
    elif choice == "2":
        add_xe()
    elif choice == "3":
        xoa_xe()
    elif choice == "4":
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-4.")
