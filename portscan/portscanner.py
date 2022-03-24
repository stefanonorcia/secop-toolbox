import socket
indirizzo_ip = input("inserisci indirizzo ip :")
porta_iniziale= input("numero porta iniziale :")
porta_finale= input("numero porta finale : ")
porta_iniziale= int(porta_iniziale)
porta_finale = int(porta_finale)
for porta in range(porta_iniziale, porta_finale):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    risultati = sock.connect_ex((indirizzo_ip, porta))
    if risultati == 0:
        print("La porta " + str(porta) + " è aperta ")
    else:
        print("La porta " + str(porta) + " è chiusa ")
    sock.close()