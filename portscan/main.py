import socket
for port in range(1, 100 ):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    risultati = sock.connect_ex(("192.168.1.98", port))
    if risultati == 0:
        print("La porta " + str(port) + " è aperta ")
    else:
        print("La porta " + str(port) + " è chiusa ")
    sock.close()