import sys
import scapy.all as scapy

def arp(ip):
    print(ip)
    arp_r = scapy.ARP(pdst=ip)
    br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    request = br / arp_r
    answered, unanswered = scapy.srp(request, timeout=1)
    print('\tIP\t\t\t\t\tMAC')
    print('_' * 37)
    for i in answered:
        ip, mac = i[1].psrc, i[1].hwsrc
        print(ip, '\t\t' + mac)
        print('-' * 37)


arp(sys.argv[1])  # call the method
