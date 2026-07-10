import socket

HOST = "127.0.0.1"
PORT = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input("Enter a string: ")

client.send(message.encode())

response = client.recv(1024).decode()

print("Response from Program B:")
print(response)

client.close()
