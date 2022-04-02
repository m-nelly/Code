def tcp_client():    
    import socket

    # the socket module allows you to send network traffic from a python script. 

    # because the socket module operates at such a low level, programming complex networking functions is fairly difficult. 

    # the easiest way to manage the added complexity is to learn the basics of how socket works and then look for examples of the protocol you are trying to work with. In most cases, there is another module you can import for that protocol which would be easier to use than socket. 

    # in this scenario, we will be building a simple TCP client to do an HTTP request out to www.google.com.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'www.google.com'
    port = 80

    s.connect((host,port)) # this opens our connection to the host. 

    s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # here we are sending in bytes the http request headers. The \r\n you see in a couple places is a carriage return and a new line. 

    response = s.recv(4096) # this tells socket to receive the response with a buffer size of 4096 bytes. 

    print(response.decode()) # here we call the decode method to parse our response which is received in bytes to our default string encoding. 

    s.close() # this closes our connection to the host. 
    return()