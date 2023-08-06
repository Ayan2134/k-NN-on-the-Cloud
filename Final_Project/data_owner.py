import socket
import json
import numpy as np
import random 
from sage.all import random_prime ,LCM, gcd, inverse_mod , mod
import sys
from decimal import *
import gmpy2

sys.set_int_max_str_digits(0)
class paillier:
    def __init__(self, k):
        while True:
            self.p = int(random_prime(2**k, False, 2**(k-1)+1))
            self.q = int(random_prime(2**k, False, 2**(k-1)+1))
            if self.p != self.q:
                break
        
    def get_public_key(self):
        self.n = int(self.p * self.q)
        self.prk = int(LCM(self.p - 1, self.q - 1))
        while True:
            while True :
                self.g = int(random.randint(1, (self.n**2) - 1))
                if int(gcd(self.g,self.n))==1 :
                    break
            L = int((pow(self.g, self.prk, self.n**2) - 1) // self.n)
            if int(gcd(L, self.n)) == 1:
                break
        self.meu = int(inverse_mod(L, self.n))
        public_key = (self.n, self.g)
        return public_key
        
    def encrypt(self, plaintext, public_key):
        message = int(plaintext)
        n = int(public_key[0])
        g = int(public_key[1])
        if message < n:
            while True:
                r = int(random.randint(1, n-1))
                if int(gcd(r, n)) == 1:
                    break
            ciphertext = pow(g, message, n**2) * pow(r, n, n**2)
            return ciphertext
        else:
            return "error"
    
    def decrypt(self, ciphertext):
        L_decrypt = (pow(int(ciphertext), self.prk, self.n**2) - 1) // self.n
        de_message = mod(L_decrypt * self.meu, self.n)
        return de_message
    
def permutation(items) :
    perm=items.copy() #np.shuffle does in place operations
    np.random.seed(1234)
    np.random.shuffle(perm)
    return perm

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("____Data Owner Server On____")
    m = 10000
    d = 50
    c = 3
    e = 4
    k = 5  # bits in paillier
    batch_size=4096
    n = d + 1 + c + e
    database = np.loadtxt('./database.txt').reshape(m, 1, d)
    cryptosystem = paillier(k)
    try :
        while True:
            conn, addr = s.accept()
            print(f"\nConnected to User : {addr}")
            print("\tAccepting query:")
            json_query = conn.recv(64000).decode()
            query = json.loads(json_query)
            print("\tQuery sent by Query User :",query)
            print("Approve Query User Request.....")
            choice = int(input("\tEnter 1 for 'YES' 0 for 'NO' : "))
            if choice==1 :
                query = np.array(query).reshape(1, d)
                conn.send(b'True')
                user = conn.recv(1024).decode()
                user = json.loads(user)
                matrix_m = np.random.randint(1, 5, (n, n))
                s_vector = np.random.randint(-30, 30, (1, d + 1))
                t_vector = np.random.randint(-20, 20, (1, c))
                inverse_m = np.linalg.inv(matrix_m)
                final_data = []
                for p in database:
                    v_vector = np.random.randint(1, 5, (1, e))
                    p_dash = np.concatenate((s_vector[0, :d].reshape(1, d) - 2 * p,
                                            (s_vector[0][d] + np.sum(p ** 2)).reshape(1, 1), t_vector, v_vector),
                                            axis=1).reshape(n)
                    p_dash = np.array(permutation(p_dash.tolist())).reshape(1, n)
                    p_dash = np.dot(p_dash, inverse_m).tolist()
                    final_data.append(p_dash)
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cloud:
                    PORT_cloud=3001
                    HOST_cloud="127.0.0.1"
                    cloud.connect((HOST_cloud,PORT_cloud))
                    print("Connected to Cloud Server")
                    offset=0
                    print("\tSending Encrypted data to cloud......")
                    json_data=json.dumps(final_data).encode()
                    while offset < len(json_data) :
                        data=json_data[offset : (offset+batch_size)]
                        cloud.send(data)
                        offset+=len(data)
                print("\tEncrypted data sent to cloud")
                print("Disconnected Cloud Server")
                final_data = np.vstack(final_data).reshape(m, 1, n)
                r_vector = np.random.randint(1, 4, (1, c))
                ek0 = cryptosystem.encrypt(0, user['key'])
                zero_vec = np.zeros((1, e))
                one_vec = np.ones((1, 1))
                query_dash = np.concatenate((query, one_vec, r_vector, zero_vec), axis=1).reshape(n)
                index = {}
                count = 0
                query_dash = query_dash.tolist()
                for num in query_dash:        #original index of the numbers in array 
                    index[num] = count
                    count += 1
                query_perm = permutation(query_dash)
                A = np.full(n, ek0, dtype=object)
                b = Decimal(random.randint(1, 5))
                for i in range(n):
                    for j in range(n):
                        t = index[query_perm[j]]
                        if t < d:
                            psi = int(b * matrix_m[i][j])
                            A[i] = float(A[i]) * pow(int(query_dash[t]),int(psi),user["key"][0])
                        elif t == d:
                            psi = int(b * matrix_m[i][j])
                            A[i] = float(A[i]) * (int(cryptosystem.encrypt(psi, user["key"])))
                        elif t < (d + 1 + c):
                            omega = t - d - 1
                            psi = b * matrix_m[i][j] * r_vector[0][omega]
                            A[i] = float(A[i]) * (int(cryptosystem.encrypt(psi, user["key"])))
                            
                query_send=A.tolist()
                json_query_send=json.dumps(query_send).encode()
                conn.sendall(json_query_send)
            else :
                conn.send(b'False')
                print("****** QUERY REQUEST DECLINED ******")
            
    except Exception as e:
        print("!!!   Request not Completed   !!!")
        print(f"An error occured : {e}")