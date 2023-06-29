#ElGamal Encryption

from sage.all import*
import random
class elGamal :
    def __init__ (self,g,p) :
        self.g=g
        self.p=int(random_prime(2**p,False,2**(p-1)+1))
        self.d=random.randint(2,p-2)
    def get_public_key(self) :
        self.h=pow(self.g,self.d,self.p)
        public_key=(self.p,self.g,self.h)
        return public_key
    def encrypt(self,plaintext,public_key) : #plaintext is in bytes
        plaintext=plaintext.hex()
        message=int(plaintext,16)
        p=public_key[0]
        g=public_key[1]
        h=public_key[2]
        if message < p :
            a=random.randint(2,self.p-2)
            key=pow(g,a,p)
            session_key=pow(h,a,p)
            ciphertext=mod(message*session_key , p)
            ciphertext=hex(ciphertext)[2:]
            if len(ciphertext)%2!=0 :
                ciphertext='0'+ciphertext
            ciphertext=bytes.fromhex(ciphertext)
            cipher_key=(ciphertext,key)
            return cipher_key
        else :
            return "error"
    def decrypt(self,cipher_key) :
        ciphertext=cipher_key[0]
        ciphertext=ciphertext.hex()
        ciphertext=int(ciphertext,16)
        key=cipher_key[1]
        session_key=pow(key,self.d,self.p)
        message=mod(int(inverse_mod(session_key,self.p))*ciphertext , self.p) #got our message back
        hex_message=hex(message)[2:]
        if len(hex_message)%2!=0 :
            hex_message='0'+hex_message
        byte_val=bytes.fromhex(hex_message)
        return byte_val