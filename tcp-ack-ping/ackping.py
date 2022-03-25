import sys
import scapy.all as scapy


def tcp_ping(host, port):
    ''' TCP Ping '''
    ans, unans = scapy.sr(scapy.IP(dst=host) / scapy.TCP(dport=port, flags="S"), timeout=0.1)
    for snd, rcv in ans:
        rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\")


tcp_ping(sys.argv[1], int(sys.argv[2]))
