import socket
import json
HOSTd="127.0.0.1"
PORTd=2001
new_num=0
x=int(input("Enter a positive integer : "))
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.connect((HOSTd,PORTd))
    print("___Connected to the Data Owner___")
    input={"query": x}
    query=json.dumps(input).encode()
    s.send(query)
    output=s.recv(1024).decode()
    received_data=json.loads(output)
    new_num=received_data["query"]
    factor=received_data["factor"]
    print(f"Entered number = {x}")
    print(f"Random number = {factor}")
    print(f"Recieved data = {new_num}\n")
HOSTc="127.0.0.1"
PORTc=2002
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
    s.connect((HOSTc,PORTc))
    print("___Connected to the Cloud Server___")
    input={"data" : new_num}
    s.send(json.dumps(input).encode())
    received_data_json=s.recv(1024).decode()
    received_data=json.loads(received_data_json)
    print("Prime Factorisation gives :")
    print(received_data["data"])

    

