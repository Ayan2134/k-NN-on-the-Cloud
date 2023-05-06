import socket
import json
import math
HOST="127.0.0.1"
PORT=2002
def check_prime(num) :
    a=int(math.sqrt(num))
    flag=True
    for i in range(2,a+1) :
        if num%i==0 :
            flag=False
            break
    return flag
def prime_factorisation(num) :
    prime_factors=[]
    for i in range(2,num+1) :
        if num%i==0 and check_prime(i) :
            while num%i ==0 :
                prime_factors.append(i)
                num=num/i
    return prime_factors

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("_____Cloud Server On_____")
    print(f"Listening on {HOST} : {PORT} \n")
    try :
        while True :
            conn , addr =s.accept()
            print(f"Connection established with {addr}")
            raw_data=conn.recv(1024).decode()
            data=json.loads(raw_data)
            num=data["data"]
            primes = prime_factorisation(num)
            new_data={"data" : primes}
            conn.send(json.dumps(new_data).encode())
            print("____Connection ended____\n")
    except :
        print("Could not establish connection !!")



        