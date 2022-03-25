import time
import logging

from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # Disable the annoying No Route found warning !


def reset_half_open(ip, part):
    # Reset the connection to stop half-open connections from pooling up
    sr(IP(dst=ip) / TCP(dport=part, flags='AR'), timeout=1)


def is_open(ip, ports, timeout=0.2):
    results = {porta: None for porta in ports}
    to_reset = []
    p = IP(dst=ip) / TCP(dport=ports, flags='S')  # Forging SYN packet
    answers, un_answered = sr(p, timeout=timeout)  # Send the packets
    for req, resp in answers:
        if not resp.haslayer(TCP):
            continue
        tcp_layer = resp.getlayer(TCP)
        if tcp_layer.flags == 0x12:
            to_reset.append(tcp_layer.sport)
            results[tcp_layer.sport] = True
        elif tcp_layer.flags == 0x14:
            results[tcp_layer.sport] = False
    # Bulk reset ports
    reset_half_open(ip, to_reset)
    return results


def chunks(ps, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(ps), n):
        yield ps[i:i + n]


start_time = time.time()
ips = input("Ciao inserisci la subnet : ")
print(f"Host is up, start scanning {ips}")
for port in chunks(range(1, 1024), 100):
    result = is_open(ips, port)
    for d, r in result.items():
        print(f"{d}:{r}")
        duration = time.time() - start_time
        print(f"{ips} scan completed in {duration}")
