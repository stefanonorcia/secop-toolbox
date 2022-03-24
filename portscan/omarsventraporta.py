import socket

host = input("Insert address: ")
port= range(1,65535)
global indice
indice=0
for unit in range(len(port)):
    porta=port[indice]
    def portScanner(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((host, porta))
        if result == 0:
            print("This port is open " + str(porta))

    indice=indice + 1
    portScanner(port)