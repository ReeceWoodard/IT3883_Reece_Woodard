# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Reece Woodard
# Assignment Number: Lab4
# Due Date: 7/10/2026
# Purpose: Basic Network Communication Program

import socket

HOST = "127.0.0.1"
PORT = 45000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Program B is waiting for a connection...")

connection, address = server.accept()
print("Connected by:", address)

message = connection.recv(1024).decode()

uppercase_message = message.upper()

print("Received and converted to uppercase:")
print(uppercase_message)

connection.send(uppercase_message.encode())

connection.close()
server.close()
