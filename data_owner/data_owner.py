import socket
import json
import random
HOST="127.0.0.1"
PORT=2000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("_____Data_Owner Server On_____")
    print(f"Listening on {HOST} : {PORT} \n")
    try :
        while True :
            conn , addr = s.accept()
            print(f"Connection established with {addr}")
            raw_data=conn.recv(1024).decode()
            data=json.loads(raw_data)
            factor=random.randrange(1,10001)
            new_num=factor*int(data["query"])
            new_dict={"query" : new_num , "factor" : factor}
            new_dict_json=json.dumps(new_dict).encode()
            conn.send(new_dict_json)
            signal=conn.recv(1024).decode()
            print("____Connection ended____\n")
    except :
        print("Could not establish connection !!!")

