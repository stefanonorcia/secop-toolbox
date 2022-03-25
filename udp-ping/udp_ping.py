import socket
UDP_IP = input("Insert address: ")
UDP_PORT = input("Insert port: ")
MESSAGE = input("Insert Message: ").encode('utf-8')
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE), (UDP_IP, int(UDP_PORT)))