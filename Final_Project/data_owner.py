import socket
import json
import numpy as np
import random

def permutation(items) :
    random.seed(1234)
    perm=random.sample(items,len(items))
    return perm

HOST="127.0.0.1"
PORT=3000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("____Data Owner Server On____")
    try :
        data=np.loadtxt('./database.txt').reshape(10000,1,50)
        m=10000
        d=50
        c=5
        e=7
        n=d+1+c+e
        while True :            
            conn , addr = s.accept()
            print(f"Connected to Client : {addr}")
            print("Accepting query :")
            json_query=conn.recv(8192).decode()
            query=json.loads(json_query)
            query=np.array(query).reshape(1,d)
            conn.send(b'True')
            scale_fac=conn.recv(1024).decode()
            scale_fac=json.loads(scale_fac)
            matrix_m = np.random.randn(n,n)
            s_vector=np.random.uniform(-50,50,(1,d+1))
            t_vector=np.random.uniform(-40 , 40 , (1,c))
            inverse_m = np.linalg.inv(matrix_m)
            data_dash=[]
            for p in data :
                v_vector=np.random.uniform(-70,70,(1,e))
                p_dash=np.concatenate((s_vector[0,:d].reshape(1,50)-2*p,(s_vector[0][d]+np.sum(p**2)).reshape(1,1),t_vector,v_vector),axis=1).reshape(n) #permutation function 
                p_dash=np.array(permutation(p_dash.tolist())).reshape(1,n)
                p_dash=np.dot(p_dash,inverse_m)
                data_dash.append(p_dash)
            data_dash=np.vstack(data_dash).reshape(m,1,n)
            print(data_dash.shape)
    except Exception as e:
        print("!!!   Request not Completed   !!!")
        print(f"An error occured : {e}")
    