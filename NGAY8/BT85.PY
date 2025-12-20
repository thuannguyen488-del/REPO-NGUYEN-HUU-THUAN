# Bài tập 5* (không bắt buộc):: 
# Dãy số Fibonacci:  In ra n số đầu tiên của dãy Fibonacci 
# (0,1,1,2,3,5,8,...) bằng vòng lặp while. Với n nhập vào từ bàn phím
n = int(input("Nhập số nguyên dương n: "))
if n==1:
   print("số hạng thứ 1 là: 0")
if n==2:
   print("số hạng thứ 1 là: 0")
   print("số hạng thứ 2 là: 1")
else:
   i=3
   sotruoc2=0
   sotruoc1=1
   print("số hạng thứ 1 là: 0")
   print("số hạng thứ 2 là: 1")
   while i<=n:
      so=sotruoc1+sotruoc2
      print("số hạng thứ",i,"là:",so)
      sotruoc2=sotruoc1
      sotruoc1=so
      i=i+1