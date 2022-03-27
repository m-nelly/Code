def socket():
    import socket

    # the socket module allows you to send network traffic from a python script. 

    # because the socket module operates at such a low level, programming complex networking functions is fairly difficult. 

    # the easiest way to manage the added complexity is to learn the basics of how socket works and then look for examples of the protocol you are trying to work with. In most cases, there is another module you can import for that protocol which would be easier to use than socket. 

    # in this scenario, we will be building a simple listener that will output any traffic it receives to the terminal. 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostname()
    port = 4444

    s.bind((ip,port))

    s.listen(1)

    return()