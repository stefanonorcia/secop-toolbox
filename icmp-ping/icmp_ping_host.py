"""#os https://docs.python.org/3/library/os.html#os.system
#da modificare per forza se no si arrabbia stefano
import os
hostname = input("Insert address: ")
response = os.system("ping -c 1 " + hostname)

if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')"""
import sys
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

p = sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()