import socket 
import ssl

HOST = 'main-device.tailbb3d90.ts.net'
PORT = 12345

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f'Server listening on {HOST} : {PORT}')

    while True:
        conn, addr = sock.accept()
        print(f'Accepted connection from {addr}')
        
        try:
            with context.wrap_socket(conn, server_side=True) as ssock:
                data = ssock.recv(1024)
                print(f'Received from client: {data.decode()}')
                ssock.sendall(b'Hello from server securely!')

        except ssl.SSLError as e:
            print(f'SSL Error: {e}')
        finally:
            conn.close()
