import socket

# Server configuration
server_ip, server_port = "127.0.0.1", 80

# Create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server.bind((server_ip, server_port))

print(f"UDP server listening on {server_ip}:{server_port}")

while True:
    # Receive data from client
    data, addr = server.recvfrom(4096)
    print(f"Received data from {addr}: {data}")

    # Echo the received data back to the client
    server.sendto(data, addr)
