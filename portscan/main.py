import socket
for port in range(1, 100 ):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    risultati = sock.connect_ex(("127.0.0.1", port))
    if risultati == 0:
        print("La porta " + str(port) + " è aperta ")
    else:
        print("La porta " + str(port) + " è chiusa ")
    sock.close()