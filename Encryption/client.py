import socket 
import ssl

HOST = 'main-device.tailbb3d90.ts.net'
PORT = 12345

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='server.crt')
context.check_hostname = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            ssock.connect((HOST, PORT))
            print(f'Connected to {HOST} : {PORT}')
            ssock.sendall(b'Hello from client securely!')
            data = ssock.recv(1024)
            print(f'Received from server: {data.decode()}')
    except ssl.SSLError as e:
        print(f'SSL Error: {e}')
    finally:
        sock.close()

