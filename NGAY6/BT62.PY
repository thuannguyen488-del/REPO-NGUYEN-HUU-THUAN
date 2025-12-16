# Bài tập 2: 
# Viết một chương trình Python để tìm nghiệm của phương trình bậc hai
#  ax2 + bx + c = 0. Biết rằng:
# Nếu a và b cùng bằng 0 thì phương trình vô nghiệm.
# Nếu a=0 thì phương trình có một nghiệm là (-c/b).
# Nếu b2-4ac < 0, thì phương trình vô nghiệm.
# Nếu không, phương trình có hai nghiệm, dùng công thức tính nghiệm 
# để tính.
import math
a=float(input("nhập vào hệ số a: "))
b=float(input("nhập vào hệ số b: "))
c=float(input("nhập vào hệ số c: "))
if a==0 and b!=0:
   x=-c/b
   print("nghiệm của phương trình là x=",x)
elif a==0 and b==0:
   print("Phương trình vô nghiệm=")
else:
   delta=b**2-4*a*c
   if delta<0:
      print("Phương trình vô nghiệm=")
   elif delta==0:
       x=-b/(2*a)
       print("phương trình có nghiệm kép là x1=x2",x)
   else:
      x1=(-b-math.sqrt(delta))/(2*a)
      x2=(-b+math.sqrt(delta))/(2*a)
      print("nghiệm của phương trình là x1=",x1)
      print("nghiệm của phương trình là x2=",x2)