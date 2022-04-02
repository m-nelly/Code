def tcp_server():
    import socket
    import threading

    ip = '0.0.0.0'
    port = 4444

    def main():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip,port))
        server.listen(5)
        print(f'[*] Listening on {ip}:{port}')

        while True:
            client, addr = server.accept()
            print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
            client_handler = threading.Thread(target=handle_client, args = (client,))
            client_handler.start()

    def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')
            sock.send(b'ACK')

    return()