import socket
import json
import numpy as np
import random 
from sage.all import random_prime ,LCM, gcd, inverse_mod , mod
HOST="127.0.0.1"
PORT=3001
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("____Cloud Server On____")
    # try :
    m=10000
    d=50
    batch_size=4096
    while True :
        conn , addr = s.accept()
        print(f"Connected to Client : {addr}")
        recv_data=b""
        while True :
            data=conn.recv(batch_size)
            if not data :
                break
            recv_data+=data
        data=recv_data.decode()
        cloud_data=json.loads(data)
    # except Exception as e:
    #     print("!!!   Request not Completed   !!!")
    #     print(f"An error occured : {e}")