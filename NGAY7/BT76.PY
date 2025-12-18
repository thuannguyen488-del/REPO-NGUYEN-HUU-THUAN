# Hãy viết chương trình dùng vòng lặp while để giải bài toán sau:
# Vừa gà vừa chó# Bó lại cho tròn
# Ba mươi sáu con# Một trăm chân chẵn
# Hỏi gà bao con, chó bao con?
soga=0
while soga<=36:
   cho=36-soga
   tong=soga*2+cho*4
   if tong==100:
      print("số gà là:",soga,"số chó là:",cho)
   soga+=1