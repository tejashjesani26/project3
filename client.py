import socket

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8765))

# Send data to the server
message = "Hello from Client!"
client_socket.send(message.encode())

# Receive the response from the server
response = client_socket.recv(1024)
print("Server response:", response.decode())

# Close the connection
client_socket.close()