import socket
HOST="127.0.0.1"
PORT=3001
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.bind((HOST,PORT))
    s.listen()
    print("____Cloud Server On____")
    try :
        while True :
            conn , addr = s.accept()
            print(f"Connected to Client : {addr}")
        
    except :
        print("!!!   Connection not established   !!!")