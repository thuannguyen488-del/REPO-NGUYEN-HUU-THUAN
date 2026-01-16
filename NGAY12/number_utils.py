# Tạo module number_utils.py chứa các hàm:
# ●	is_even(n)        # trả về True nếu n chẵn
# ●	is_odd(n)		# trả về True nếu n lẻ
# ●	is_prime(n)       # trả về True nếu n là số nguyên tố
def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!=0
def is_prime(n) :
     if n < 2:
        return False
     for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
     return True
a= int(input("nhập vào số a"))
if is_prime(a):
   print(f"số {a} là số nguyen to")
else:
   print(f"số {a} là số kong nguyen to")