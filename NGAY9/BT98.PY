# VẼ HÌNH CHỮ NHẬT RỖNG RUỘT, với chiều dài và rộng tự nhập vào
dai=int(input("nhập bào chiều dài hình chữ nhật cần vẽ"))
rong=int(input("nhập bào chiều rộng hình chữ nhật cần vẽ"))
for i in range(rong):
   for j in range(dai):
       if (i>=1) and (i<rong-1):
          if j==0 or j==dai-1:
             print("*",end=" ")
          else:
             print(" ",end=" ")
       elif (i==0) or i==rong-1:
          print("*",end=" ")
   print()