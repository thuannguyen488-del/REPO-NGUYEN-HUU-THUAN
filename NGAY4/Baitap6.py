#Bài tập 6: Tìm tổng các chữ số của một số
#Viết chương trình:Nhập vào số nguyên 3 chữ số
#Tính tổng các chữ số Ví dụ: 123 → 1 + 2 + 3 = 6
a=int(input("nhập vào số a:"))
sohangtram=int(a/100)
sohangchuc=int((a-sohangtram*100)/10)
sohangdonvi=a%10
tong=sohangtram+sohangchuc+sohangdonvi
print("tổng các chữ số của số a là: ",tong)