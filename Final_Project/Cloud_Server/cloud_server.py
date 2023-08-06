import socket
import json
import numpy as np
import random 

HOST="0.0.0.0"
PORT=3001

def knn(cloud_data,cloud_query,neighbour) :
    distance=np.dot(cloud_data,cloud_query.T)
    distance=np.abs(distance).reshape(-1).tolist()
    temp=np.sort(distance).reshape(-1).tolist()
    index = []
    for i in range(neighbour) :
        for j in range(m) :
            if distance[j] == temp[i] :
                index.append(j)
    return index

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("____Cloud Server On____")
    try :
        m=10000
        d=50 
        c = 3
        e = 4
        k = 5 
        n = d + 1 + c + e
        batch_size=4096
        while True :
            conn , addr = s.accept()
            print(f"\nConnected to Data Owner : {addr}")
            print("\tReceiving encrypted data from Data Owner......")
            recv_data=b""
            while True :
                data=conn.recv(batch_size)
                if not data :
                    break
                recv_data+=data
            data=recv_data.decode()
            cloud_data=json.loads(data)
            cloud_data=np.array(cloud_data)
            
            #Accepting query from client
            
            conn_user , addr_user = s.accept()
            print(f"\nConnected to User : {addr_user}")
            print("\tReceiving query from user......")
            cloud_query = conn_user.recv(64000).decode()
            print("\tReceived query")
            cloud_query=json.loads(cloud_query)
            cloud_query=np.array(cloud_query).reshape(1,n)
            neighbour = int(input("\tEnter number of k-NN of the dataset : "))
            index=knn(cloud_data , cloud_query , neighbour)
            print("\tRequested datapoint indexes  are :",index)
            send_index = json.dumps(index).encode()
            conn_user.sendall(send_index)
            print("\tSent the indexes to Query User")
    except Exception as e:
        print("!!!   Request not Completed   !!!")
        print(f"An error occured : {e}")