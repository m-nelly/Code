def udp_client():
    import socket

    host = '127.0.0.1'
    port = 4422

    # create the socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # sends data to the host we specified
    s.sendto(b"Junk!", (host, port))

    # receives 4096 bytes of data from the host
    response = s.revfrom(4096)

    print(response.decode())

    s.close()
    return()