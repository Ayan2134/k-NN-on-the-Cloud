from sage.all import*
class rsa :
    def __init__ (self,k,e=65537) :
        self.e=e
        while True :
            self.p=random_prime(2**k , False , 2**(k-1)+1)
            self.q=random_prime(2**k , False , 2**(k-1)+1)
            if self.p!=self.q :
                break
            
    def get_public_key(self) :
        n=self.p*self.q
        public_key=(self.e,n)
        return public_key
    
    def encrypt(self , plaintext , public_key) : 
        n=public_key[1]
        e=public_key[0]
        hex_value=plaintext.hex()
        message=int(hex_value,16)
        if message < n :
            ciphertext=mod(message**e,n)
            return ciphertext
        else :
            return("error")
            
    def decrypt(self,ciphertext) :
        if ciphertext!="error" :
            public_key=self.get_public_key()
            d=inverse_mod(self.e,(self.p-1)*(self.q-1))
            message=mod(ciphertext**d,public_key[1])
            hex_message=hex(message)[2:]
            byte_val=bytes.fromhex(hex_message)
            return byte_val
        else :
            return "error"
            
 
        
        