import bluetooth
server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM) #Serverlistenstoacceptone connection at a time.
client_socket,address = server_socket.accept() #Server accepts client’s connection request and assign the mac address to the variable address, client_socket is the client’s socket
print("Accepted connection from ",address)
#Finally after all the programming, close the client and server connection using below code:
port=1
server_socket.bind(("",port))
server_socket.listen(1)
while 1:
    data = client_socket.recv(1024) # Receive data through the client socket client_socket and assign it to the variable data. Maximum 1024 characters can be received at a time.
    client_socket.close()
    server_socket.close()