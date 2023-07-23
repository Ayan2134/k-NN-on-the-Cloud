import socket
import numpy as np
from sage.all import*
import random
import json
class paillier :
    def __init__ (self,k) :
        while True :
            self.p=int(random_prime(2**k , False, 2**(k-1)+1)) #gcd(pq,(p-1)(q-1))=1 but if p and q is of equal size this is always true
            self.q=int(random_prime(2**k , False, 2**(k-1)+1))
            if self.p!=self.q :
                break
        
    def get_public_key(self) :
        self.n=int(self.p*self.q)
        self.prk=int(LCM(self.p-1,self.q-1))
        while True :
            self.g=int(random.randint(1,(self.n**2)-1))
            L=int((pow(self.g,self.prk,self.n**2)-1)//self.n)
            if int(gcd(L,self.n))==1 :
                break
        self.meu=int(inverse_mod(L,self.n))
        public_key=(self.n,self.g)
        return public_key
        
    def encrypt(self,plaintext,public_key) : #plaintext in int
        message=plaintext
        n=int(public_key[0])
        g=int(public_key[1])
        if message < n :
            while True :
                r=int(random.randint(1,n-1))
                if int(gcd(r,n)) == 1:
                    break
            ciphertext=pow(g,message,n**2)*pow(r,n,n**2)
            return ciphertext
        
        else :
            return "error"
    def decrypt(self,ciphertext) : #ciphertext in int
        L_decrypt=(pow(ciphertext,self.prk,self.n**2)-1)//self.n
        de_message=mod(L_decrypt*self.meu , self.n)
        return de_message
    
HOST="127.0.0.1"
PORT=3000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    k=5 #number of bits in the key 
    d=50
    batch_size=4096
    scale_pow=0
    cryptosystem=paillier(k)
    pub_key=cryptosystem.get_public_key()
    query=np.random.randint(1,10,(1,d))
    scale_fac=10**scale_pow
    enc_query=[]
    
    for dim in query[0] : # encrypting each query dimension
        num=(int(dim*scale_fac))
        enc_dim=cryptosystem.encrypt(num,pub_key)
        enc_query.append(enc_dim)
    print(enc_query)
    json_query=json.dumps(enc_query).encode()   
    s.sendall(json_query)
    status=s.recv(1024).decode()
    info={"scale" : scale_fac , "key" : pub_key}
    info=json.dumps(info).encode()
    s.sendall(info)
    if status == "True" :
        print("Query sent successfully")