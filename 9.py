import socket
from http.client import responses

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

responses = client.recv(4096)

print(responses.decode())
client.close()