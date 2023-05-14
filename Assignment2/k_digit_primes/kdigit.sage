k=int(input("Enter the number of digits for the prime numbers : "))
class coeff :
    a=0
    b=0

def solver(p,q) :
    if p==0 :
        c_end=coeff()
        c_end.a=0
        c_end.b=1
        return c_end
    c_end=coeff()
    c_end=solver(q%p,p)
    c_ans=coeff()
    c_ans.b=c_end.a
    c_ans.a=c_end.b - c_end.a * (q//p)
    return c_ans

while True : #to make sure both random primes are distinct
    p=random_prime(10^k , True , 10^(k-1)+1)
    q=random_prime(10^k , True , 10^(k-1)+1)
    if p!=q :
        break
if p>q : #to make sure that p < q as my solver function is using that condition in (q%p) part
    p,q=q,p
print(f"Prime numbers are {p} and {q}")
ans=coeff()
ans=solver(p,q)
soln=(p,q,ans.a,ans.b)
print(f"After solving a*{p} + b*{q} = 1 ")
print(f"The solution in the format of (p,q,a,b) is {soln}") 



    
