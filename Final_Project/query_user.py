import socket
import numpy as np
from sage.all import*
import random
import json
import sys

sys.set_int_max_str_digits(0)

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
            while True :
                self.g = int(random.randint(1, (self.n**2) - 1))
                if int(gcd(self.g,self.n))==1 :
                    break
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
    query=np.random.randint(-10,10,(1,d))
    scale_fac=10**scale_pow
    enc_query=[]
    
    for dim in query[0] : # encrypting each query dimension
        num=(int(dim*scale_fac))
        enc_dim=cryptosystem.encrypt(num,pub_key)
        enc_query.append(enc_dim)
    print("Waiting for Response from Data Owner.......")
    json_query=json.dumps(enc_query).encode()   
    s.sendall(json_query)
    status=s.recv(1024).decode()
    info={"scale" : scale_fac , "key" : pub_key}
    info=json.dumps(info).encode()
    s.sendall(info)
    print("Query sent successfully to Data Owner")
    if status == "True" :
        print("Query Request Approved from Data Owner")
        do_query=s.recv(64000).decode()
        do_query=json.loads(do_query)
        print("Encrypted Query recieved from Data Owner")
        
        dec_query=[]
        for point in do_query :
            dec_query.append(int(cryptosystem.decrypt(int(point))))
        with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as cloud :
            HOST_cloud = "127.0.0.1"
            PORT_cloud = 3001 # port of cloud server for query user
            cloud.connect((HOST_cloud,PORT_cloud))
            cloud_query=json.dumps(dec_query).encode()
            cloud.sendall(cloud_query)
            print("Sent query to cloud")
            index = cloud.recv(6400).decode()
            index = json.loads(index)
            print("\n\tRequested Indexes from the Database :",index)
    else :
        print("!!!! Your Query Request has been declined by Data Owner !!!!")
        
        