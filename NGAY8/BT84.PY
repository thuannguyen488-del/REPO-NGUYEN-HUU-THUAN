# Bài tập 4:: 
# Trò chơi đoán số Máy tính tự chọn một số ngẫu nhiên từ 1 đến 100. 
# Người dùng có tối đa 7 lần đoán.
# Nếu đoán đúng: In "Chúc mừng" và ngừng chương trình.
# Nếu hết 7 lần mà vẫn sai: Dùng else của while để in 
# "Rất tiếc, bạn đã thua. Số đúng là...".
i=1
import random
while i<=7:
   sodudoan = int(input("Nhập số dự đoán: "))
   somaychon=random.randint(1,100)
   if sodudoan==somaychon:
      print("Chúc mừng")
      i=8
   i=i+1
else:
    print("Rất tiếc, bạn đã thua. Số đúng là...",somaychon)
   
 