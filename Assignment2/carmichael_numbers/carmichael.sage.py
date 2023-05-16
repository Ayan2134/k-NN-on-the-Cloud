

# This file was *autogenerated* from the file carmichael.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3)
import time
n=int(input("Enter the number till which Carmichael Numbers are to be printed : "))
start=time.time()
counter=_sage_const_0 
def modulus(i) :
    num=_sage_const_0 
    for k in range(_sage_const_1 ,i) :
        rem=pow(k , i-_sage_const_1  , i)
        if rem==_sage_const_1  :
            num+=_sage_const_1 
    return num
    
for i in range(_sage_const_3 ,n+_sage_const_1 ) : #step of 2 as carmichael numbers are odd composite numbers
    if is_prime(i)==False :
        if modulus(i)==euler_phi(i) :
            print(i)
            counter+=_sage_const_1 
if counter==_sage_const_0  :
    print("No such numbers in the specified range")
end=time.time()
print(end-start)
        

