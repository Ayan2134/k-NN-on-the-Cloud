index=10 #just change the value of index to get more amicable numbers
i=2
num=0
while True :
    sum_i=sigma(i,1)-i
    sum_div=sigma(sum_i,1)-sum_i
    if i==sum_div and sum_i!=i and sum_i>i :
        print(f"{num+1}. {i} and {sum_i}")
        num+=1
    if num==index :
        break
    i+=1
    
