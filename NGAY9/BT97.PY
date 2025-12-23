# Bài tập 4: 
# Sử dụng vòng lặp for trong  Python để in ra hình sau: 
# * * * * * * * * * * * * * * * * * * * *
# *                                            *
# *                                            *
# *                                            *
# *                                            *
# *                                            *
# * * * * * * * * * * * * * * * * * * * *
for i in range(7):
   for j in range(20):
       if (i>=1) and (i<6):
          if j==0 or j==19:
             print("*",end=" ")
          else:
             print(" ",end=" ")
       elif (i==0) or i==6:
          print("*",end=" ")
   print()