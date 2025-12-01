# import socket 
# import ssl

# HOST = 'main-device.tailbb3d90.ts.net'
# PORT = 12345

# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.load_verify_locations(cafile='server.crt')
# context.check_hostname = False

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     try:
#         with context.wrap_socket(sock, server_hostname=HOST) as ssock:
#             ssock.connect((HOST, PORT))
#             print(f'Connected to {HOST} : {PORT}')
#             ssock.sendall(b'Hello from client securely!')
#             data = ssock.recv(1024)
#             print(f'Received from server: {data.decode()}')
#     except ssl.SSLError as e:
#         print(f'SSL Error: {e}')
#     finally:
#         sock.close()

import socket

# Resolve the domain name
try:
    server_ip = socket.gethostbyname("main-device.tailbb3d90.ts.net")
except socket.gaierror:
    print("Could not resolve the domain name.")
    exit()

# Connect to the server using the resolved IP and port
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

print(f"Connected to {server_ip}:{server_port}")
# ... send/receive data ...
# client_socket.close()