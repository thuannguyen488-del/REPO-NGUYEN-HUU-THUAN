#Bài tập 8: Tính lãi suất ngân hàng
#Yêu cầu: Viết chương trình Python cho phép người dùng nhập vào: :
#Nhập số tiền gửi (float) Nhập số năm gửi (int)
#Nhập lãi suất năm (%)
#Tính tiền lãi và tổng tiền sau số năm với lãi suất gộp hàng năm thông qua công thức: 
#Tổng tiền = gốc * (1 + lãi suất/100)^năm
sonam=int(input("nhập vào số năm:"))
sotiengui=float(input("nhập vào số tiền gửi: "))
laisuat=float(input("nhập vào slãi suất: "))
tongtien=sotiengui*(1+laisuat/100)**sonam
tienlai=tongtien-sotiengui
print("so năm",sonam)
print("sotiengui",sotiengui)
print("số tiền lãi trong:",sonam,"năm là:",tienlai)
print("tổng số tiền lãi trong",sonam,"năm là: ",tongtien)