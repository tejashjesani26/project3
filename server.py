import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8765))
server_socket.listen(1)  # Listen for one incoming connection

print("Waiting for connection...")
client_socket, addr = server_socket.accept()
print("Connection from", addr)

# Receive data from the client
data = client_socket.recv(1024)
print("Received:", data.decode())

# Send a response back to the client
response = "Hello from Server!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()