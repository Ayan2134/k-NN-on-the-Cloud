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
        
    def encrypt(self,plaintext,public_key) : #plaintext in bytes
        plaintext=plaintext.hex()
        message=int(plaintext,16)
        n=int(public_key[0])
        g=int(public_key[1])
        if message < n :
            while True :
                r=int(random.randint(1,n-1))
                if int(gcd(r,n)) == 1:
                    break
            ciphertext=pow(g,message,n**2)*pow(r,n,n**2)
            ciphertext=hex(ciphertext)[2:]
            if len(ciphertext)%2!=0 :
                ciphertext='0'+ciphertext
            ciphertext=bytes.fromhex(ciphertext)
            return ciphertext
        
        else :
            return "error"
    def decrypt(self,ciphertext) :
        ciphertext=ciphertext.hex()
        ciphertext=int(ciphertext,16)
        L_decrypt=(pow(ciphertext,self.prk,self.n**2)-1)//self.n
        de_message=mod(L_decrypt*self.meu , self.n)
        hex_message=hex(de_message)[2:]
        if len(hex_message)%2!=0 :
            hex_message='0'+hex_message
        byte_val=bytes.fromhex(hex_message)
        return byte_val
    
HOST="127.0.0.1"
PORT=3000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    k=50 #number of bits in the key 
    d=50
    scale_pow=8
    cryptosystem=paillier(k)
    pub_key=cryptosystem.get_public_key()
    query=np.random.randn(1,d)
    scale_fac=10**scale_pow
    enc_query=[]
    
    for dim in query[0] : # encrypting each query dimension
        num=str(int(dim*scale_fac))
        num_byte=num.encode()
        enc_dim=cryptosystem.encrypt(num_byte,pub_key)
        enc_dim=enc_dim.hex()
        enc_dim=int(enc_dim,16)
        enc_query.append(enc_dim)
        
    json_query=json.dumps(enc_query).encode()   
    s.sendall(json_query)
    status=s.recv(1024).decode()
    enc_scale={"scale" : scale_fac}
    enc_scale=json.dumps(enc_scale).encode()
    s.sendall(enc_scale)
    if status == "True" :
        print("Query sent successfully")