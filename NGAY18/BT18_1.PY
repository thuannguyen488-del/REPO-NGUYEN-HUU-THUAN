# Bài tập 1: 
# Viết chương trình cho người dùng nhập vào 5 phần tử của list, mỗi phần tử là thông tin cá nhân của 1 người, ví dụ:
#  [
# [“Nguyễn Văn A”,20, “Đà Nẵng”], 
# [“Nguyễn Văn B”,22, “Nghệ An”], 
# [“Nguyễn Văn C”,40, “Quãng Nam”], 
# [“Nguyễn Văn D”,16, “Huế”], 
# [“Nguyễn Văn E”, 28, “Hà Nội”]
# ]
# Viết hàm đọc và ghi dữ liệu đã nhập vào file data.csv
# studen=[
# ["Nguyễn Văn A","20", "Đà Nẵng"], 
# ["Nguyễn Văn B","22", "Nghệ An"], 
# ["Nguyễn Văn C","40", "Quãng Nam"], 
# ["Nguyễn Văn D",16, "Huế"], 
# ["Nguyễn Văn E", 28, "Hà Nội"]
# ]
# with open("data.csv","w") as f:
#     f.writelines(["stu","ccđ"])
# Danh sách sẵn có
ds_nguoi = [
    ["Nguyễn Văn A", 20, "Đà Nẵng"],
    ["Nguyễn Văn B", 22, "Nghệ An"],
    ["Nguyễn Văn C", 40, "Quảng Nam"],
    ["Nguyễn Văn D", 16, "Huế"],
    ["Nguyễn Văn E", 28, "Hà Nội"]
]

# Hàm ghi dữ liệu vào file
def ghi_file_csv(ten_file, ds):
    with open(ten_file, mode="w", encoding="utf-8") as f:
        f.write("Họ và tên,Tuổi,Địa chỉ\n")
        for row in ds:
            dong = f"{row[0]},{row[1]},{row[2]}\n"
            f.write(dong)
    print(f"Đã ghi dữ liệu vào file {ten_file}")

# Hàm đọc dữ liệu từ file CSV (không dùng import csv)
def doc_file_csv(ten_file):
    with open(ten_file, mode="r", encoding="utf-8") as f:
        for line in f:
            # loại bỏ ký tự xuống dòng và tách theo dấu phẩy
            row = line.strip().split(",")
            print(row)

# Chạy chương trình
if __name__ == "__main__":
    ghi_file_csv("NGAY18\data.csv", ds_nguoi)
    print("\nNội dung file data.csv:")
    doc_file_csv("NGAY18\data.csv")