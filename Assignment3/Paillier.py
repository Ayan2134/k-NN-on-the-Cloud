from sage.all import*
import random
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
            return ciphertext
        else :
            return "error"
        
    def decrypt(self,ciphertext) :
        if ciphertext!="error" :
            L_decrypt=(pow(ciphertext,self.prk,self.n**2)-1)//self.n
            de_message=mod(L_decrypt*self.meu , self.n)
            hex_message=hex(de_message)[2:]
            byte_val=bytes.fromhex(hex_message)
            return byte_val
        else :
            return "error"
    
