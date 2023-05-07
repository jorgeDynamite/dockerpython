import time
import socket
import tensorflow as tf


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected\n".encode())
    client.send(f"{tf.__version__}".encode())
    print("1")
    time.sleep(2)
    client.send("Dissconnect\n".encode())
    print("2")
    client.close()


"""
from sklearn.datasets import load_iris
data = load_iris()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected\n".encode())
    client.send(f"{data['data'][:, 0]}a\n".encode())
    print("1")
    time.sleep(2)
    client.send("Dissconnect\n".encode())
    print("2")
    client.close()
"""
