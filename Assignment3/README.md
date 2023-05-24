RSA :
1. Create an object of class rsa using obj=rsa(k,e) where k is the number of bits in prime numbers and e is the part of the public key which is default set to 65537
2. Call get_public_key function using public_key=obj.get_public_key() //here public_key is a tuple(e,n) 
3. Give this key as an argument to the encrypt() function as ciphertext=obj.encrypt(plaintext,public_key) //plaintext is in bytes
4. Now the ciphertext contains the cipher value of the plaintext 
5. Give this ciphertext as an argument to the decrypt() function as message=obj.decrypt(ciphertext) //we get the plaintext back here in form of "message" in bytes
6. Convert message to text using message.decode() . 
7. Now you get the message back.
//The message and ciphertext should be less than n if not then encrypt and decrypt will return error

ElGamal :
1. Create an object of the class elGamal using obj=elGamal(g,p) where g is the primitive root of p and p is a large prime number
2. Call get_public_key function using public_key=obj.get_public_key() //here public_key is a tuple(p,g,h) 
3. Give this key as an argument to the encrypt() function as cipher_key=obj.encrypt(plaintext,public_key) //plaintext is in bytes
4. Now the cipher_key is a tuple (ciphertext,public_key_of_the_sender)
5. Give this cipher_key as an argument to the decrypt() function as message=obj.decrypt(cipher_key) //we get the plaintext back here in form of "message" in bytes
6. Convert message to text using message.decode() . 
7. Now you get the message back.
//The message and ciphertext should be less than p if not then encrypt and decrypt will return error

Paillier :
1. Create an object of the class paillier using obj=paillier(k) where k is the number of bits in the prime numbers p and q
2. Call get_public_key function using public_key=obj.get_public_key() //here public_key is a tuple(n,g) where g is such that gcd(L((g^prk)mod(n^2)),n)==1 and n=p*q
3. Give this key as an argument to the encrypt() function as ciphertext=obj.encrypt(plaintext,public_key) //plaintext is in bytes
4. Now the ciphertext contains the cipher value of the plaintext 
5. Give this ciphertext as an argument to the decrypt() function as message=obj.decrypt(ciphertext) //we get the plaintext back here in form of "message" in bytes
6. Convert message to text using message.decode() . 
7. Now you get the message back.
//The message should be less than n if not then encrypt and decrypt will return error