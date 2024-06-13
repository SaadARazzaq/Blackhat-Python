import socket

target_host, target_port = "google.com", 80

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to our target
client.connect((target_host, target_port))

# Once connected, GET HTTP request
client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")

# RECIEVE the HTTP respose
response = client.recv(4096)  # Buffer size: 4096

# Decode the response to a string
response_string = response.decode("utf-8")

print(response_string)
