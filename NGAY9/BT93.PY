# Bài tập 3: 
# Trò chơi "Đoán số" là một trò chơi số học với luật chơi rất đơn giản. 
# Có hai người chơi, quản trò viết một số trong phạm vi 0-10 
# (phạm vi có thể thay đổi) ra giấy, người chơi sẽ đoán một số 
# trong phạm vi trên. Quản trò sẽ trả lời là Đúng hay Sai, nếu đáp án
#  là sai thì quản trò sẽ đưa ra một gợi ý để người chơi đoán tiếp.
#  Trò chơi sẽ dừng lại nếu đoán đúng hoặc đoán sai 3 lần.
# Sử dụng Python làm game đoán số trên. 
# Gợi ý: 
# import random
# Sử dụng hàm random.randint(0, 10) để random 1 số bí mật từ 0 đến 10
# Sử dụng vòng lặp cho người dùng nhập vào số dự đoán
# Nếu số dự đoán là đúng: thông báo chúc mừng người thắng cuộc và
#  kết thúc trò chơi
# Nếu số dự đoán không đúng : thông báo số đã dự đoán đang nhỏ hơn hoặc lớn hơn số bí mật
# Sau 3 lần dự đoán không chính xác thì kết thúc trò chơi và thông báo người dùng thua cuộc

import random
canduoi=int(input("nhập vào giá trị cận dưới vùng dự đoán"))
cantren=int(input("nhập vào giá trị cận trên vùng dự đoán"))
socuamay=random.randint(canduoi,cantren)
dem=0
for i in range(3):
   sodudoan = int(input("Nhập số dự đoán: "))
   if sodudoan==socuamay:
      dem+=1
      print("thông báo chúc mừng người thắng cuộc")
      break
   elif sodudoan>socuamay:
      print("Gợi ý: số của bạn lớn hơn số cần dự đoán")
   elif sodudoan<socuamay:
      print("Gợi ý: số của bạn nhỏ hơn số cần dự đoán")
if dem==0:
   print("bạn đoán không đúng, số đúng là:",socuamay)