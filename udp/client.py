import socket

# Client configuration
target_ip, target_port = "127.0.0.1", 80

socket_tuple = (target_ip, target_port)

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
message = "This is test data"
client.sendto(message.encode(), socket_tuple)

try:
    # Receive some response/data
    data, addr = client.recvfrom(4096)  # Buffer size: 4096

    # Decode the response to a string
    response_string = data.decode("utf-8")

    print(f"Received response from {addr}: {response_string}")
except socket.error as e:
    print(f"Socket error: {e}")
