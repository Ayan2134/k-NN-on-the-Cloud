n=int(input("Enter the number till which Carmichael Numbers are to be printed : "))
counter=0
def modulus(i) :
    num=0
    for k in range(1,i) :
        rem=pow(k , i-1 , i)
        if rem==1 :
            num+=1
    return num
    
for i in range(3,n+1,2) : #step of 2 as carmichael numbers are odd composite numbers
    if is_prime(i)==False :
        if modulus(i)==euler_phi(i) :
            print(i)
            counter+=1
if counter==0 :
    print("No such numbers in the specified range")
        