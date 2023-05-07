import time
import socket 
import sklearn.datasets import load_iris

data = load_iris()
print("Hello World")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True: 
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected\n".encode())
    client.send(f"{data[0][:,0]}\n".encode())
    time.sleep(2)
    client.send("Dissconnect\n".encode())
    client.close()