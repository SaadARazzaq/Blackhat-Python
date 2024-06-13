import socket
import threading  #  To accept multiple connections simultaneously

IP = '0.0.0.0'  # 0.0.0.0 is to Listen on all interfaces
PORT = 9988
socket_tuple = (IP, PORT)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(socket_tuple)
    
    server.listen(5)  #  This indicates how many connections it can support. In this case it will listen upto 5 connections
    print(f'[*] Listening on {IP}:{PORT}')

    # Continuously accept new connections
    while True:
        # Accept a new connection
        # CLIENT is a new socket object usable to send and receive data on the connection
        # ADDR is the address bound to the socket on the other end of the connection
        CLIENT, ADDR = server.accept()
        print(f'[*] Accepted connection from {ADDR[0]}:{ADDR[1]}')

        # Create a new thread to handle the client connection
        client_handler = threading.Thread(target= handle_client, args= (CLIENT, ))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        # Receive data from the client
        # The buffer size is 1024 bytes
        request = sock.recv(1024)
        print(f'[*] Recieved: {request.decode("utf-8")}')

        sock.send(b'ACK')

if __name__ == '__main__':
    main()
