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
    d=5
    c = 2
    e = 2
    k = 5 
    n = d + 1 + c + e
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
        cloud_data=np.array(cloud_data)
        
        conn_user , addr_user = s.accept()
        print(f"Connected to Client : {addr_user}")
        cloud_query=conn_user.recv(64000).decode()
        cloud_query=json.loads(cloud_query)
        cloud_query=np.array(cloud_query).reshape(1,n)
        print(cloud_query)
        distance=np.dot(cloud_data,cloud_query.T)
        min_dist=np.min(distance)
        print(min_dist)
        index=0
        for dist in distance :
            if dist==min_dist :
                print("Index :",index)
                break
            index+=1
        print("Requested datapoint is :",cloud_data[index].tolist())
    # except Exception as e:
    #     print("!!!   Request not Completed   !!!")
    #     print(f"An error occured : {e}")