import time
import socket
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np
from scipy.spatial import distance
import requests

model_url = "https://tfhub.dev/tensorflow/efficientnet/lite0/feature-vector/2"

layer = hub.KerasLayer(model_url)

# tf.keras.saving.register_keras_serializable('KerasLayer')(hub.KerasLayer)
model = tf.keras.Sequential([layer])

# Register KerasLayer object before saving the model
# pickle.dumps(tf.keras.saving.register_keras_serializable('KerasLayer')(hub.KerasLayer))
# pickle.dump(model, open("model.pkl", "wb"))

# Load the model from the pickle file

IMAGE_SHAPE = (224, 224)


def extract(file):
    file = Image.open(file).convert("L").resize(IMAGE_SHAPE)
    # display(file)

    file = np.stack((file,) * 3, axis=-1)

    file = np.array(file) / 255.0
    print(file.shape)

    embedding = model.predict(file[np.newaxis, ...])
    # print(embedding)
    vgg16_feature_np = np.array(embedding)
    flattended_feature = vgg16_feature_np.flatten()

    # print(len(flattended_feature))
    # print(flattended_feature)
    # print('-----------')
    return flattended_feature


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected\n".encode())
    img_url_list = [
        "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTw4zCbTQoEtMJG6B5r46bVobPiiwdy8Qkv_bxbWjO3PoHAAK8yNyHNYx8L5JUMTMG5qB13Kit7_LoYUsBvxbciWg5XaXGZwSTi20Xv6gFsaPa5RFtY9_Wc&usqp=CAE",
        "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQ4ULSl2BKTkNuHmU4WLLNm8To97rSLnp1BpvaforG1i8LZr5IQnrXqKZteiKIejrcVX0BJbIv6_2T8H3PKSOemd7cSwwP1luKUe6xXQR4BOShf82byQZ7SbQ&usqp=CAE",
        "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQ8BvkOwrNkUCyqyIHQs0Ri7O74iEM0giBbOJ1LYqqffHqkPlHYE4uVG221iZ8qZWAb9zKZT-T2qlSjyimqsNlJQUdNlDa6jArqoASivgc&usqp=CAE",
        "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQi1yy_Or3169TtW5tapJpOzWB4roaU9SAbFxwMGtZALFc3jzsZZWwKCukJJq0bkCLNvVBtxfcmmbllHvH44r8ZHWJU7t1QrdL-EMP8AcAcTj7IJT1T2TO0ew&usqp=CAE",
        "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSfpanK66HKxvGvWflIAPvVrl-zoRY8mqXKzJeIeCdyMeWmccq2jIBVPvFM3E-ehFI7PcqwR0yPVdMYQpUyxYqEVinX93Vzf-EiHAwfnfCf&usqp=CAE",
        "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRjj9yqx7uW1GXhwTHUzDwmeC6FpEzLkjAWEUyy8xohhGvkyRZuyRfqSDMA_387bph7k0T-FSRAlZUHDZKq0yZ11O1vyTEzEJqUTX1HgSQaRBUq8ElsSZP0BA&usqp=CAE",
        "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcT6TanSk1iNHhZZk-0YdPXTEyXOe4cA40DrBeY_BYPJAWApeEU5ornEnuEiQNUZXHbrZN8fGX9-e1jSsLK7Szz5JXqB-MFX347pswVFmKaSDRRSfJIeLQgvNQ&usqp=CAE",
        "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcS7P4hitSD1Z0vB3hsX1l5B5Q95ziXfyfUmDTYGs0e1lfzZUypmiAYLjOyu00v9UOpBuoRqAXUV-k3bgQerWx_2ZXVcGgW0Hg&usqp=CAE",
        "https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/becc982c-2da5-46d9-8e54-bca71304341b._CR0,0,400,400_AC_SX130_SY60_QL70_.jpg",
        "https://m.media-amazon.com/images/I/61ZTszckgaL._AC_UL400_.jpg",
        "https://m.media-amazon.com/images/I/61-2dcga70L._AC_UL320_.jpg",
        "https://m.media-amazon.com/images/I/512EFncZ8fL._AC_UL400_.jpg",
        "https://m.media-amazon.com/images/I/71CXksHSSRL._AC_UL320_.jpg",
        "https://m.media-amazon.com/images/I/51zHPDgT1GL._AC_UL400_.jpg",
        "https://m.media-amazon.com/images/I/5120G1cUIwL._AC_UL320_.jpg",
        "https://m.media-amazon.com/images/I/71nFAjEg9+L._AC_UL400_.jpg",
        "http://ae01.alicdn.com/kf/Hfa8991764a5642b79bcad6ea252809506.jpg",
        "http://ae01.alicdn.com/kf/H13525dd1839f44f2a82719581d11ba7f1.jpg",
        "http://ae01.alicdn.com/kf/Se9f7e6deb0f54f66a87af9aa55791293o.png",
        "http://ae01.alicdn.com/kf/H0269e39de1ef4f50ad5daca29e75b9e9W.jpg",
        "http://ae01.alicdn.com/kf/H13525dd1839f44f2a82719581d11ba7f1.jpg",
        "http://ae01.alicdn.com/kf/Sfad9f6175a3b4e74afdf2565e7d77949p.jpg",
        "http://ae01.alicdn.com/kf/H4359c39af6484a44ad70ea70d40a45ffg.jpg",
        "http://ae01.alicdn.com/kf/H56612a0276e640f9b603a9fe0405bfd2z.jpg",
    ]
    for i in range(len(img_url_list)):
        img = Image.open(requests.get(img_url_list[i], stream=True).raw)
        img.save("./images/sample" + str(i) + ".png", "")
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
